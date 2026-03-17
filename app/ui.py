from __future__ import annotations

import queue
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText

from app.config import APP_NAME, load_environment, load_settings, save_settings
from app.models import AnswerResult, BuildResult, ChatTurn
from app.rag_service import RagService


class MarkdownRagApp:
    def __init__(self) -> None:
        load_environment()
        self.service = RagService()
        self.chat_history: list[ChatTurn] = []
        self.events: queue.Queue[tuple[str, object]] = queue.Queue()

        self.root = tk.Tk()
        self.root.title(APP_NAME)
        self.root.geometry("1100x760")
        self.root.minsize(900, 650)

        self.selected_file_var = tk.StringVar()
        self.chunk_size_var = tk.IntVar(value=350)
        self.chunk_overlap_var = tk.IntVar(value=60)
        self.top_k_var = tk.IntVar(value=5)
        self.status_var = tk.StringVar(value="Select a Markdown file, build the database, then ask questions.")
        self.source_info_var = tk.StringVar(value="No vector database has been built yet.")

        self._build_layout()
        self._load_state()
        self.root.after(100, self._poll_events)

    def _build_layout(self) -> None:
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        controls = ttk.Frame(self.root, padding=12)
        controls.grid(row=0, column=0, sticky="ew")
        controls.columnconfigure(1, weight=1)

        ttk.Label(controls, text="Markdown file").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
        file_entry = ttk.Entry(controls, textvariable=self.selected_file_var)
        file_entry.grid(row=0, column=1, sticky="ew", pady=(0, 8))
        ttk.Button(controls, text="Browse...", command=self._select_markdown_file).grid(
            row=0, column=2, sticky="ew", padx=(8, 0), pady=(0, 8)
        )

        ttk.Label(controls, text="Chunk size").grid(row=1, column=0, sticky="w", padx=(0, 8))
        ttk.Spinbox(controls, from_=50, to=4000, textvariable=self.chunk_size_var, width=10).grid(
            row=1, column=1, sticky="w"
        )

        ttk.Label(controls, text="Overlap").grid(row=1, column=1, sticky="w", padx=(140, 8))
        ttk.Spinbox(controls, from_=0, to=2000, textvariable=self.chunk_overlap_var, width=10).grid(
            row=1, column=1, sticky="w", padx=(200, 0)
        )

        ttk.Label(controls, text="Top-k").grid(row=1, column=1, sticky="w", padx=(320, 8))
        ttk.Spinbox(controls, from_=1, to=15, textvariable=self.top_k_var, width=8).grid(
            row=1, column=1, sticky="w", padx=(370, 0)
        )

        self.build_button = ttk.Button(controls, text="Build / Rebuild DB", command=self._start_build)
        self.build_button.grid(row=1, column=2, sticky="ew", padx=(8, 0))

        self.clear_button = ttk.Button(controls, text="Clear Chat", command=self._clear_chat)
        self.clear_button.grid(row=2, column=2, sticky="ew", padx=(8, 0), pady=(8, 0))

        ttk.Label(
            controls,
            textvariable=self.source_info_var,
            foreground="#2f4f4f",
        ).grid(row=2, column=0, columnspan=2, sticky="w", pady=(8, 0))

        chat_frame = ttk.Frame(self.root, padding=(12, 0, 12, 12))
        chat_frame.grid(row=1, column=0, sticky="nsew")
        chat_frame.columnconfigure(0, weight=1)
        chat_frame.rowconfigure(0, weight=1)

        self.chat_log = ScrolledText(chat_frame, wrap="word", font=("Segoe UI", 10))
        self.chat_log.grid(row=0, column=0, sticky="nsew")
        self.chat_log.configure(state="disabled")

        input_frame = ttk.Frame(chat_frame, padding=(0, 10, 0, 0))
        input_frame.grid(row=1, column=0, sticky="ew")
        input_frame.columnconfigure(0, weight=1)

        self.question_input = ScrolledText(input_frame, height=5, wrap="word", font=("Segoe UI", 10))
        self.question_input.grid(row=0, column=0, sticky="ew")
        self.question_input.bind("<Control-Return>", self._send_with_shortcut)

        self.send_button = ttk.Button(input_frame, text="Send", command=self._start_chat)
        self.send_button.grid(row=0, column=1, sticky="ns", padx=(8, 0))

        ttk.Label(self.root, textvariable=self.status_var, padding=(12, 0, 12, 12)).grid(
            row=2, column=0, sticky="ew"
        )

    def _load_state(self) -> None:
        settings = load_settings()
        self.selected_file_var.set(settings.selected_markdown)
        self.chunk_size_var.set(settings.chunk_size)
        self.chunk_overlap_var.set(settings.chunk_overlap)
        self.top_k_var.set(settings.top_k)

        manifest = self.service.load_manifest()
        if manifest is None:
            return

        self.source_info_var.set(
            f"Indexed source: {manifest.source_name} | "
            f"chunks: {manifest.chunk_count} | "
            f"built: {manifest.built_at}"
        )

    def _select_markdown_file(self) -> None:
        selected = filedialog.askopenfilename(
            title="Choose a Markdown file",
            filetypes=[("Markdown files", "*.md *.markdown"), ("All files", "*.*")],
        )
        if not selected:
            return

        self.selected_file_var.set(selected)
        settings = self.service.settings
        settings.selected_markdown = selected
        save_settings(settings)

    def _set_busy(self, busy: bool, status: str) -> None:
        state = "disabled" if busy else "normal"
        self.build_button.configure(state=state)
        self.send_button.configure(state=state)
        self.clear_button.configure(state=state)
        self.status_var.set(status)

    def _start_build(self) -> None:
        markdown_file = self.selected_file_var.get().strip()
        if not markdown_file:
            messagebox.showerror("Missing file", "Choose a Markdown file first.")
            return

        chunk_size = int(self.chunk_size_var.get())
        chunk_overlap = int(self.chunk_overlap_var.get())

        self._set_busy(True, "Building Chroma database from the selected Markdown file...")
        thread = threading.Thread(
            target=self._build_worker,
            args=(markdown_file, chunk_size, chunk_overlap),
            daemon=True,
        )
        thread.start()

    def _build_worker(self, markdown_file: str, chunk_size: int, chunk_overlap: int) -> None:
        try:
            result = self.service.rebuild_database(markdown_file, chunk_size, chunk_overlap)
            self.events.put(("build_success", result))
        except Exception as exc:
            self.events.put(("error", exc))

    def _start_chat(self) -> None:
        question = self.question_input.get("1.0", "end").strip()
        if not question:
            messagebox.showerror("Missing question", "Enter a question before sending.")
            return

        top_k = int(self.top_k_var.get())
        self.service.update_top_k(top_k)

        self.question_input.delete("1.0", "end")
        self._append_message("You", question)
        self.chat_history.append(ChatTurn(role="user", content=question))
        self._set_busy(True, "Retrieving relevant chunks and generating a grounded answer...")

        thread = threading.Thread(
            target=self._chat_worker,
            args=(question, top_k, list(self.chat_history)),
            daemon=True,
        )
        thread.start()

    def _chat_worker(self, question: str, top_k: int, history: list[ChatTurn]) -> None:
        try:
            result = self.service.answer_question(question, top_k, history)
            self.events.put(("chat_success", result))
        except Exception as exc:
            self.events.put(("error", exc))

    def _poll_events(self) -> None:
        while True:
            try:
                event, payload = self.events.get_nowait()
            except queue.Empty:
                break

            if event == "build_success":
                self._handle_build_success(payload)
            elif event == "chat_success":
                self._handle_chat_success(payload)
            elif event == "error":
                self._handle_error(payload)

        self.root.after(100, self._poll_events)

    def _handle_build_success(self, result: object) -> None:
        build_result = result if isinstance(result, BuildResult) else None
        if build_result is None:
            self._handle_error(RuntimeError("Unexpected build result."))
            return

        manifest = build_result.manifest
        self.source_info_var.set(
            f"Indexed source: {manifest.source_name} | "
            f"chunks: {manifest.chunk_count} | "
            f"built: {manifest.built_at}"
        )
        self._clear_chat()
        self._append_message(
            "System",
            f"Database rebuilt from {manifest.source_name} with {manifest.chunk_count} chunks.",
        )
        self._set_busy(False, "Vector database built successfully.")

    def _handle_chat_success(self, result: object) -> None:
        answer_result = result if isinstance(result, AnswerResult) else None
        if answer_result is None:
            self._handle_error(RuntimeError("Unexpected chat result."))
            return

        rendered = self._format_answer(answer_result)
        self.chat_history.append(ChatTurn(role="assistant", content=rendered))
        self._append_message("Assistant", rendered)
        self._set_busy(False, "Answer ready.")

    def _handle_error(self, error: object) -> None:
        message = str(error)
        self._set_busy(False, "The last operation failed.")
        messagebox.showerror("Operation failed", message)

    def _append_message(self, speaker: str, message: str) -> None:
        self.chat_log.configure(state="normal")
        self.chat_log.insert("end", f"{speaker}:\n{message}\n\n")
        self.chat_log.see("end")
        self.chat_log.configure(state="disabled")

    def _format_answer(self, result: AnswerResult) -> str:
        lines = [result.answer.strip()]
        if result.citations:
            lines.append("")
            lines.append("Citations:")
            for item in result.citations:
                lines.append(item.citation_label())
        else:
            lines.append("")
            lines.append("Citations: none")
        return "\n".join(lines)

    def _clear_chat(self) -> None:
        self.chat_history.clear()
        self.chat_log.configure(state="normal")
        self.chat_log.delete("1.0", "end")
        self.chat_log.configure(state="disabled")
        self.status_var.set("Chat cleared.")

    def _send_with_shortcut(self, _: tk.Event) -> str:
        self._start_chat()
        return "break"

    def run(self) -> None:
        self.root.mainloop()


def launch() -> None:
    app = MarkdownRagApp()
    app.run()
