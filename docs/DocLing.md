# DocLing

> تاريخ هذه المذكرة: 2026-06-04
>
> الهدف: فهم Docling كأداة لمعالجة المستندات، استيعاب قدراتها، معرفة متى نستخدمها، هل تعمل محلياً، متى نحتاج استضافة، وكيف يمكن تحويلها إلى جزء من نظام RAG أو أرشفة أو استخراج بيانات.

## الخلاصة السريعة

 ان Docling هي أداة مفتوحة المصدر لمعالجة المستندات وتحويلها إلى بيانات منظمة. ليست مجرد OCR وليست مجرد PDF-to-Markdown. الفكرة الأساسية أنها تأخذ مستنداً فوضوياً أو معقداً، مثل PDF أو DOCX أو PPTX أو XLSX أو صورة أو ملف صوت، وتحوّله إلى تمثيل موحد اسمه `DoclingDocument`. من هذا التمثيل يمكن التصدير إلى Markdown أو JSON أو HTML أو Text أو DocTags أو WebVTT.

قيمة Docling تظهر عندما لا يكفي استخراج النص الخام. مثلاً:

- PDF متعدد الأعمدة.
- جداول معقدة.
- صور ورسوم بيانية.
- معادلات رياضية.
- كود داخل المستند.
- مستند ممسوح يحتاج OCR.
- وثائق تحتاج أن تدخل إلى RAG مع الحفاظ على البنية.
- ملفات Office أو HTML أو XML خاصة تريد تحويلها إلى بنية واحدة.

الإجابة العملية على سؤال التشغيل:

- نعم، يمكن تشغيل Docling على جهازك محلياً.
- لا تحتاج استضافة خارجية للاستخدام الشخصي أو الملفات الحساسة أو التجارب.
- تحتاج استضافة فقط إذا أردت API لفريق أو تطبيق ويب أو معالجة كثيفة أو تشغيل GPU مركزي.
- يمكن تشغيله كـ CLI، أو كمكتبة Python، أو كخدمة API عبر `docling-serve`، أو كأداة Agent عبر `docling-mcp`.

## ما المشكلة التي تحاول Docling حلها؟

المشكلة ليست "كيف أقرأ PDF؟" فقط. المشكلة الأكبر هي: كيف أحول مستنداً غير منظم إلى بيانات تصلح للذكاء الاصطناعي؟

الملفات الواقعية ليست نصاً مستقيماً:

- العنوان قد يكون أعلى الصفحة.
- الترويسة والتذييل قد يتكرران في كل صفحة.
- النص قد يكون في عمودين.
- الجدول قد يحتوي خلايا مدمجة ورؤوس متعددة المستويات.
- الصورة قد يكون لها caption.
- المعادلة قد تظهر كرموز رسومية.
- الترتيب البصري للقراءة قد لا يساوي ترتيب النص الداخلي في PDF.
- بعض الصفحات قد تكون ممسوحة بالكامل ولا تحتوي نصاً رقمياً.

لو استخدمت أداة بسيطة لاستخراج النص، قد تحصل على نص طويل، لكنه مكسور:

- جدول يتحول إلى أسطر غير مفهومة.
- عنوان ينفصل عن الفقرة.
- أرقام الصفحات تدخل في chunks.
- الأعمدة تختلط.
- الصور تختفي.
- المراجع والتذييلات تلوث النص.

Docling تحاول معالجة هذه الطبقة: تحويل المستند إلى كائن غني بالبنية، لا مجرد نص.

## ما هو DoclingDocument؟

`DoclingDocument` هو التمثيل الداخلي المنظّم للمستند داخل Docling.

بدلاً من أن يتعامل Docling مع الملف كـ PDF أو DOCX أو صورة أو HTML فقط، يقوم بتحويله إلى كائن موحّد اسمه `DoclingDocument`. هذا الكائن يحتوي بنية المستند بعد الفهم والمعالجة.

يعني يمكن أن يحتوي على:

- النصوص والفقرات
- العناوين
- الجداول
- الصور
- المعادلات
- كتل الكود
- القوائم
- ترتيب القراءة
- الصفحات
- مواقع العناصر داخل الصفحة
- بيانات وصفية عن المستند
- علاقات بين العناصر مثل caption وصورة أو جدول وعنوانه

الفكرة المهمة: `DoclingDocument` ليس مجرد نص مستخرج. هو نسخة منظّمة من المستند.

مثلاً لو عندك PDF فيه عنوان وفقرة وجدول، الاستخراج البسيط قد يعطيك نصاً مسطحاً. أما `DoclingDocument` فيحاول أن يحتفظ بأن هذا الجزء عنوان، وهذا جدول، وهذه خلية داخل الجدول، وهذه فقرة تحت العنوان.

بعد ذلك يمكنك تصديره إلى:

```python
result.document.export_to_markdown()
```

أو JSON أو HTML أو نص عادي.

قيمته تظهر خصوصاً في RAG، لأنك تستطيع تقسيم المستند بناءً على بنيته، لا مجرد تقطيع نص طويل عشوائياً.

بمعنى آخر، أهمية `DoclingDocument` أنه يجعل كل الملفات المختلفة قابلة للتعامل معها بطريقة واحدة. بدلاً من أن يكون لكل صيغة منطق خاص، مثل PDF أو DOCX أو PPTX أو HTML أو صورة تحتاج OCR، تحاول Docling تحويلها إلى شكل واحد يمكن تصديره أو تقسيمه أو إثراؤه.

هذه البنية تمنحك فرصة أفضل لبناء chunks مفهومة واسترجاع أدق، خصوصاً عندما تريد حفظ العناوين والجداول والصفحات ومواقع العناصر في نظام معرفة أو RAG.

## الصيغ التي تدعمها Docling

حسب التوثيق الرسمي، Docling تدعم إدخال صيغ كثيرة، منها:

- PDF.
- DOCX.
- XLSX.
- PPTX.
- Markdown.
- AsciiDoc.
- LaTeX.
- HTML و XHTML.
- CSV.
- صور: PNG, JPEG, TIFF, BMP, WEBP.
- صوت: WAV, MP3, M4A, AAC, OGG, FLAC.
- فيديو: MP4, AVI, MOV، حيث يتم استخراج المسار الصوتي وتفريغه، ويتطلب ذلك `asr` و `ffmpeg`.
- WebVTT.
- XML خاص مثل USPTO patents و JATS articles و XBRL financial reports.
- Docling JSON.

والمخرجات المدعومة تشمل:

- Markdown.
- HTML.
- JSON.
- Text.
- DocTags.
- WebVTT.

الفكرة هنا أن Docling يمكن أن تكون بوابة موحدة للمواد غير المتجانسة. لو عندك مشروع فيه PDF و Word و PowerPoint وصور وتسجيلات، يمكن وضعها ضمن pipeline واحد بدلاً من كتابة محول منفصل لكل صيغة.

## أهم القدرات

### 1. تحويل المستندات إلى Markdown

الاستخدام الأول والبسيط: تحويل PDF أو DOCX أو غيره إلى Markdown.

مثال CLI:

```powershell
docling "C:\path\to\file.pdf"
```

أو:

```powershell
docling https://arxiv.org/pdf/2206.01062
```

هذا مناسب عندما تريد قراءة الملف، إدخاله إلى Obsidian، أو استخدامه في pipeline لاحق.

لكن يجب الانتباه: Markdown هو مخرج مريح، لكنه قد يفقد بعض التفاصيل التي تبقى محفوظة في JSON أو `DoclingDocument`.

### 2. تحويل إلى JSON غني

لو كنت تبني تطبيقاً أو RAG أو نظام أرشفة، JSON غالباً أهم من Markdown. لأن JSON يمكن أن يحتفظ بالبنية والعناصر والصفحات والجداول والمواقع.

الاستخدام المحتمل:

- استخراج الجداول برمجياً.
- معرفة أين توجد الصورة.
- ربط chunk برقم الصفحة.
- حفظ metadata.
- تحويل المستند إلى قاعدة بيانات.
- بناء واجهة تعرض النص وتحدد مكانه في الصفحة الأصلية.

### 3. فهم تخطيط الصفحة

ان Docling تستخدم نماذج layout detection لاكتشاف عناصر الصفحة مثل:

- النص.
- العناوين.
- الجداول.
- الصور.
- captions.
- footnotes.
- page headers.
- page footers.
- formulas.
- list items.

هذه القدرة مهمة جداً في PDF. كثير من مشاكل PDF تأتي من أن الملف مرئي أكثر مما هو منطقي. الإنسان يرى الصفحة ويعرف ترتيب القراءة، لكن البرنامج قد يرى صناديق نصية متناثرة. Docling تحاول بناء ترتيب قراءة منطقي.

### 4. ترتيب القراءة

ترتيب القراءة مهم في:

- المقالات العلمية.
- التقارير ذات الأعمدة.
- ملفات الشركات.
- العروض.
- الوثائق القانونية.

لو دخل النص إلى LLM بترتيب خاطئ، قد تصبح الإجابة خاطئة حتى لو كان كل النص موجوداً. Docling تحاول ترتيب المكونات حسب القراءة، وليس فقط حسب موضعها الخام داخل PDF.

### 5. الجداول

الجداول من أصعب أجزاء المستندات. Docling تتضمن TableFormer وخيارات fast/accurate. يمكن أن تلتقط بنية الجدول مثل:

- الصفوف.
- الأعمدة.
- الخلايا.
- الرؤوس.
- الرؤوس متعددة المستويات.
- محتوى الخلية المعقد مثل القوائم.

هذا مهم لأن الجدول لا ينبغي أن يتحول فقط إلى نص مسطح. في RAG، الجداول المسطحة قد تعطي نتائج سيئة لأن العلاقة بين العمود والصف تضيع.

تفكير عملي:

- لو المستندات عندك تعتمد كثيراً على الجداول، اجعل اختبار الجداول أولوية.
- لا تكتف بأن "النص ظهر". افحص هل الجدول مفهوم.
- جرّب table accurate mode عند الملفات الصعبة.
- إن وجدت أعمدة مدمجة خطأ، جرّب إعدادات cell matching.

### 6. OCR للمستندات الممسوحة

 ان Docling تدعم عدة OCR engines، منها:

- EasyOCR.
- Tesseract.
- Tesseract CLI.
- OcrMac على macOS.
- RapidOCR.
- OnnxTR عبر plugin.
- SuryaOCR مذكور في model catalog.

هذا يعني أن Docling ليست مقيدة بمحرك OCR واحد. تستطيع اختيار المحرك حسب اللغة والجودة والسرعة والبيئة.

بالنسبة للعربية، يجب الاختبار عملياً. دعم OCR العربي يعتمد غالباً على المحرك المختار وملفات اللغة وجودة المسح. Tesseract يدعم العربية، لكن الجودة تختلف كثيراً حسب الخط، الدقة، التشويش، واتجاه النص.

### 7. المعادلات

 و ايضا Docling يمكنها اكتشاف المعادلات وتحويلها إلى LaTeX عبر enrichment خاص. هذا مهم في:

- الأوراق العلمية.
- كتب الرياضيات.
- الفيزياء.
- الهندسة.
- مواد تعليمية.

الميزة ليست دائماً مفعلة افتراضياً لأنها تضيف وقت معالجة. إذا كانت المعادلات مهمة في مشروعك، يجب تفعيلها واختبارها.

### 8. الكود

و Docling يمكنها التعرف على كتل الكود وتصنيف لغة البرمجة ضمن enrichment. هذا مهم في:

- الوثائق التقنية.
- الكتب البرمجية.
- ملفات التعليم.
- و الpapers فيها pseudo-code أو snippets.

### 9. الصور والرسوم

كما ان Docling يمكنها:

- استخراج الصور.
- حفظها داخل DoclingDocument أو كملفات خارجية.
- ربط captions بالصور.
- تصنيف الصور مثل chart أو diagram أو natural image.
- توليد وصف للصورة عبر VLM محلي أو remote API.

هذه نقطة مهمة في RAG متعدد الوسائط. إذا كان المستند يحتوي diagrams أو charts، النص وحده غير كاف. يمكن استخدام Docling لاستخراج الصورة ووصفها أو تصنيفها أو حفظها للرجوع البصري.

### 10. Chart understanding

حسب GitHub، من الميزات الحديثة فهم بعض الرسوم مثل bar chart و pie chart و line plot، وتحويلها إلى جداول أو كود أو إضافة أوصاف تفصيلية. هذا يفتح مجالاً مهماً:

- تقارير مالية.
- و dashboards مطبوعة.
- أوراق بحثية فيها plots.
- عروض شركات.

لكن هذه ميزة يجب اختبارها بصرامة. قراءة الرسم البياني آلياً أصعب من استخراج نص، ولا ينبغي افتراض الدقة دون عينة اختبار.

### 11. الصوت والفيديو

ان Docling تدعم الصوت عبر ASR عند تثبيت extra:

```powershell
pip install "docling[asr]"
```

والفيديو عبر استخراج الصوت، مع الحاجة إلى `ffmpeg`.

هذا يعني أن Docling يمكن أن تدخل في pipeline تعليمي أو أرشيفي:

- تفريغ محاضرات.
- تحويل فيديو إلى WebVTT.
- استخراج نص من تسجيلات.
- دمج مخرجات الصوت مع ملفات PDF أو slides.

### 12. Information Extraction

توجد ميزة structured information extraction في beta. الفكرة: تعطي Docling قالباً أو schema، مثلاً Pydantic model، وهي تحاول استخراج البيانات المطلوبة من PDF أو صورة.

مثال مفاهيمي:

- invoice_number.
- total_amount.
- sender.
- receiver.
- date.
- tax_id.

هذا يختلف عن "حوّل المستند إلى Markdown". هنا تريد حقولاً منظمة مباشرة.

الاستخدامات:

- فواتير.
- نماذج.
- عقود.
- إيصالات.
- مستندات مالية.

لأنها beta، يجب التعامل معها كتجربة واختبار، لا كشيء مضمون في الإنتاج دون validation.

## كيف تعمل Docling مع RAG؟

و Docling مناسبة جداً كمرحلة ingest/preprocessing قبل RAG.

في الPipeline ممكن:

1. إدخال ملفات PDF/DOCX/PPTX/صور.
2. تحويلها بـ Docling إلى `DoclingDocument`.
3. تصدير Markdown أو JSON.
4. استخدام chunker مناسب.
5. إضافة metadata: اسم الملف، الصفحة، العنوان، نوع العنصر.
6. عمل embeddings.
7. تخزين في vector database.
8. ثم retrieval.
9. وعمل generation مع citations.

النقطة الأهم: الموضوع ليس مجرد ملفات "Markdown فقط". لو لديك مستندات معقدة، فكر في حفظ JSON أو DoclingDocument أيضاً. Markdown مريح للقراءة، لكن JSON أفضل للمراجعة والمعالجة.

## Chunking داخل Docling

ان Docling توفر chunkers أصلية تعمل على `DoclingDocument`، وليس فقط على النص بعد تحويله إلى Markdown.

الفكرة:

- يمكن البدء من البنية الهرمية للمستند.
- يمكن مراعاة حدود tokens.
- يمكن دمج chunks صغيرة.
- يمكن تقسيم chunks كبيرة.
- يمكن تكرار headers عند تقطيع الجداول الطويلة.

هذا مهم لأن تقطيع النص الخام قد يكسر المعنى:

- عنوان منفصل عن فقرته.
- جدول مقطوع بدون رؤوس.
- ال chunk يحتوي تذييل الصفحة فقط.
- فقرة من عمودين مختلطة.

بالنسبة لـ RAG، جودة chunking قد تكون أهم من جودة embedding نفسها في بعض الحالات.

## هل تشغلها محلياً أم تحتاج استضافة؟

### تشغيل محلي

مناسب عندما:

- تعمل وحدك.
- تريد التجربة.
- لديك ملفات حساسة.
- تريد تجنب إرسال البيانات إلى طرف ثالث.
- عدد الملفات محدود أو متوسط.
- لا تحتاج API عامة.

أوامر البداية:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install docling
docling "C:\path\to\file.pdf"
```

أو Python:

```python
from docling.document_converter import DocumentConverter

source = r"C:\path\to\file.pdf"
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())
```

### تشغيل محلي مع extras

حسب الحاجة:

```powershell
pip install "docling[vlm]"
pip install "docling[asr]"
pip install "docling[rapidocr]"
pip install "docling[easyocr]"
```

يمكن أيضاً استخدام:

```powershell
pip install "docling[vlm,asr,rapidocr]"
```

لكن لا تثبت كل شيء من البداية إذا لم تكن تحتاجه. بعض extras تزيد الحجم والتعقيد.

### تشغيل Offline

تقوم Docling بتنزل النماذج تلقائياً عند أول استخدام. إذا أردت بيئة بلا إنترنت، يمكن تنزيل النماذج مسبقاً:

```powershell
docling-tools models download
```

ثم تحديد المسار:

```powershell
docling --artifacts-path="C:\path\to\models" FILE
```

أو عبر متغير:

```powershell
$env:DOCLING_ARTIFACTS_PATH = "C:\path\to\models"
```

هذا مهم للبيئات الحساسة أو air-gapped.

### متى تحتاج استضافة؟

تحتاج استضافة عندما:

- عندك تطبيق ويب يحتاج تحويل مستندات.
- عندك فريق يستخدم نفس الخدمة.
- تريد API موحدة.
- تريد عزل المعالجة عن جهازك.
- تريد queue ومعالجة batch.
- تريد GPU مركزي.
- تريد تشغيل داخل Kubernetes أو OpenShift.
- تريد قياس الأداء والمراقبة.

هنا استخدم `docling-serve`.

## Docling Serve

ال`docling-serve` يحول Docling إلى API service.

تشغيل محلي:

```powershell
pip install "docling-serve[ui]"
docling-serve run --enable-ui
```

ثم عادة تكون الخدمة على:

- API: `http://127.0.0.1:5001`
- Docs: `http://127.0.0.1:5001/docs`
- UI: `http://127.0.0.1:5001/ui`

ويمكن تشغيلها عبر container images. توجد صور CPU وصور CUDA حسب البيئة. هذا مناسب للإنتاج أكثر من تشغيل CLI عشوائياً.

استخدامات Docling Serve:

- واجهة داخلية لتحويل الملفات.
- خدمة ingest لمشروع RAG.
- API يستقبل ملفات ويرجع JSON/Markdown.
- دمج مع backend أو workflow automation.

## Docling MCP

`ان docling-mcp` يجعل قدرات Docling متاحة لوكلاء AI عبر Model Context Protocol.

الفكرة:

- المساعد أو العميل الذي يدعم MCP يستطيع استدعاء أدوات Docling.
- يمكن تشغيله local أو remote.
- الإصدار الحديث يدعم remote mode عبر Docling Serve أو local mode مع extra.

هذا مفيد إذا أردت أن يكون لدى agent قدرة على:

- تحويل PDF.
- قراءة مستند.
- استخراج محتوى.
- العمل على مستندات داخل workflow.

لكن إذا كان هدفك الآن هو فهم الأداة أو بناء pipeline عادي، ابدأ بـ CLI/Python. MCP يصبح مهماً عندما تريد دمج Docling داخل agents.

## VLM Pipeline و Granite-Docling

ان Docling تدعم مساراً يستخدم Vision-Language Models لتحويل الصفحات end-to-end.

نماذج مذكورة في التوثيق أو model catalog:

- Granite-Docling-258M.
- SmolDocling-256M.
- Granite Vision.
- Pixtral.
- Qwen2.5-VL.
- Nanonets OCR2.
- Phi-4 multimodal.
- Gemma عبر MLX.
- وغيرها.

الفكرة:

- بدلاً من pipeline متخصص لكل عنصر، يمكن لنموذج رؤية-لغة أن يرى الصفحة وينتج DocTags أو Markdown.
- ال  Granite-Docling مصمم خصيصاً لتحويل المستندات، وليس VLM عام فقط.
- اما DocTags صيغة مهمة لأنها تمثل عناصر الصفحة ومواقعها وبنيتها بشكل أكثر غنى من Markdown.

متى تستخدم VLM؟

- صفحات شديدة التعقيد.
- مستندات فيها charts/diagrams/forms.
- عندما يفشل parsing التقليدي.
- عندما تريد فهم بصري، لا نص فقط.

متى لا تبدأ بـ VLM؟

- إذا المستندات بسيطة.
- إذا العدد كبير جداً وتريد سرعة.
- إذا لا تملك GPU أو endpoint سريع.
- إذا كان standard pipeline يعطي نتيجة كافية.

نهج عملي: استخدم standard pipeline أولاً، ثم استخدم VLM فقط للصفحات التي تحتاجه.

## GPU والأداء

يمكن لDocling ان تعمل على CPU، لكنها قد تستفيد من GPU حسب المرحلة والنموذج.

في standard pipeline:

- يمكن ضبط accelerator device مثل CUDA أو AUTO.
- يمكن ضبط batch sizes لبعض المراحل مثل OCR/layout/table.
- ال OCR GPU يعتمد على المحرك المختار.

في VLM pipeline:

- الأفضل غالباً تشغيل inference server محلي مثل vLLM أو LM Studio أو Ollama، ثم جعل Docling يتصل به عبر OpenAI-compatible endpoint.
- ان vLLM مذكور كخيار قوي، لكنه غالباً Linux-focused.
- و LM Studio وOllama متاحان على Windows وLinux.

نصيحة أداء:

- لا تستخدم VLM لكل صفحة دون سبب.
- ابدأ بفحص نوع المستند.
- الصفحات النصية: standard pipeline.
- الصفحات الممسوحة: OCR.
- الصفحات البصرية المعقدة: VLM أو picture description.
- الملفات الكبيرة: batch + limits + queue.

## هل Docling آمنة للبيانات الحساسة؟

الفكرة الأساسية في Docling حسب التوثيق أنها تعمل محلياً ولا ترسل بياناتك إلى remote services افتراضياً. إذا استخدمت remote service، يجب تفعيل:

```python
enable_remote_services=True
```

هذا قرار تصميم مهم. يعني:

- التشغيل المحلي ممكن.
- استخدام API خارجي يتطلب opt-in.
- تنزيل model weights شيء مختلف عن إرسال بيانات المستخدم.

لكن الأمان العملي يعتمد عليك:

- أين تحفظ الملفات؟
- هل تستخدم OCR/LLM خارجي؟
- هل تستخدم Docling Serve مفتوحاً على الشبكة؟
- هل تضبط authentication؟
- هل تسجل logs تحتوي محتوى المستند؟

## أين تتفوق Docling؟

تبدو قوية خصوصاً في:

- ال PDF parsing المتقدم.
- تحويل مستندات متعددة الصيغ إلى تمثيل موحد.
- و RAG preprocessing.
- التعامل مع الجداول.
- و layout-aware extraction.
- حفظ البنية بدل النص الخام فقط.
- تشغيل محلي.
- التكامل مع LangChain/LlamaIndex/Haystack/Crew AI وغيرها.
- وجود CLI وPython API وServe وMCP.
- مجتمع نشط جداً ومشروع مفتوح المصدر MIT.

## أين يجب الحذر؟

لا توجد أداة parsing مثالية. يجب الحذر في:

- المستندات العربية الممسوحة.
- الجداول المالية المعقدة جداً.
- الملفات ذات جودة scan سيئة.
- و الhand-written content.
- و الcharts التي تحتاج قراءة دقيقة للأرقام.
- آلاف الملفات يومياً دون خطة أداء.
- الاعتماد على Markdown وحده.
- افتراض أن output صحيح دون validation.
- استخدام VLM لكل شيء بسبب التكلفة/الوقت.

ان Docling ممتازة كبداية قوية، لكنها قد تحتاج post-processing.

## مقارنة ذهنية مع أدوات أخرى

هذه ليست مقارنة حاسمة، لكنها خريطة تفكير:

- اولا اداتي : PyMuPDF أو pdfplumber: جيدان للاستخراج والتحكم المنخفض المستوى، لكنهما لا يقدمان نفس طبقة AI/layout/table الشاملة.
- اداة OCR : Tesseract فقط، وليس pipeline مستند كامل.
- اداة MarkItDown: بسيط ومفيد لتحويلات مباشرة، لكنه أقل تركيزاً على الفهم البنيوي المعقد.
- ادوات مثل Marker/MinerU/DeepSeekOCR : منافسون في PDF-to-Markdown أو document parsing، ويجب اختبارهم حسب نوع الملفات.
- خدمات Azure Document Intelligence / Google Document AI / Amazon Textract: خدمات سحابية قوية، لكنها خارجية ومدفوعة ومغلقة نسبياً.
- ان Docling: خيار open-source محلي، غني بالبنية، مناسب لـ RAG والتجارب والخصوصية.

## سيناريوهات عملية لاستخدام Docling

### سيناريو 1: تحويل PDF إلى Markdown للقراءة

مناسب للملفات البسيطة أو المتوسطة.

```powershell
docling file.pdf
```

### سيناريو 2: تجهيز ملفات لـ Obsidian

1. تحويل PDF إلى Markdown.
2. مراجعة العناوين والجداول.
3. نقل markdown إلى vault.
4. إضافة ملاحظات بشرية وروابط.

### سيناريو 3: RAG على مستندات تقنية

1. تحويل إلى JSON/DoclingDocument.
2. استخراج headings وtables.
3. عمل chunking مع metadata.
4. ثم embeddings.
5. و vector DB.
6. اضافة citations بالصفحات.

### سيناريو 4: أرشفة وثائق مؤسسة

1. وضع Docling Serve داخل شبكة داخلية.
2. مع API لتحويل الملفات.
3. حفظ JSON + Markdown + صور.
4. فهرسة في search engine.
5. ربط النتائج بمصدرها الأصلي.

### سيناريو 5: استخراج بيانات من فواتير

1. استخدام information extraction.
2. schema بـ Pydantic.
3. validation.
4. fallback إلى مراجعة بشرية عند انخفاض الثقة.

### سيناريو 6: تحليل محاضرات

1. تحويل slides بـ Docling.
2. تفريغ الصوت بـ ASR.
3. دمج المخرجات.
4. إنشاء ملخصات أو RAG تعليمي.

### سيناريو 7: معالجة ملفات حساسة

1. تشغيل محلي.
2. تنزيل النماذج مسبقاً.
3. تعطيل remote services.
4. حفظ المخرجات داخلياً.
5. عدم استخدام LLM API خارجي.

## خطة تجربة عملية مقترحة

حتى نفهم Docling فعلاً، لا يكفي قراءة التوثيق. يجب اختبارها على ملفات حقيقية.

### المرحلة 1: تثبيت وتشغيل بسيط

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install docling
docling sample.pdf
```

الهدف: هل تعمل على الجهاز؟ هل تنزل النماذج؟ كم تستغرق؟

### المرحلة 2: اختبار أنواع ملفات

اختبر:

- PDF نصي واضح.
- PDF ممسوح.
- PDF فيه جداول.
- DOCX.
- PPTX.
- صورة.
- ملف عربي إن وجد.

لكل ملف، راقب:

- جودة النص.
- ترتيب القراءة.
- الجداول.
- العناوين.
- الترويسة والتذييل.
- زمن المعالجة.

### المرحلة 3: مقارنة Markdown و JSON

لا تكتف بمخرج Markdown. احفظ JSON وافحص:

- هل الجداول محفوظة كبنية؟
- هل الصفحات واضحة؟
- هل الصور لها metadata؟
- هل يمكن ربط chunk برقم الصفحة؟

### المرحلة 4: اختبار OCR

جرّب:

- OCR default.
- Tesseract إن كان مثبتاً.
- RapidOCR.
- EasyOCR.

قارن السرعة والجودة خصوصاً ==للغة العربية==.

### المرحلة 5: اختبار RAG صغير

خذ 3 ملفات فقط:

1. حوّلها بـ Docling.
2. chunk.
3. embeddings.
4. اسأل 20 سؤالاً.
5. راقب هل الأخطاء من parsing أو retrieval أو LLM.

### المرحلة 6: اختبار Docling Serve

إذا أردت API:

```powershell
pip install "docling-serve[ui]"
docling-serve run --enable-ui
```

افتح:

```text
http://127.0.0.1:5001/ui
```

## أسئلة عصف ذهني مهمة

هذه الأسئلة تساعدنا نقرر كيف نستفيد منها:

- هل نريد Docling للقراءة البشرية أم لـ RAG؟ كليهما 
- هل ملفاتنا PDFs نصية أم ممسوحة؟ الاثنين 
- هل اللغة العربية أساسية؟ نعم و يوجد تداخل بين العربي و الانجليزي اى انه يوجد نصوص عربية تحوي مصطلحات انجليزية او نصوص انجليزي تحوي تعليقات عربي عليها 
- هل الجداول أساسية أم ثانوية؟اساسية جدا لان الكثير من ما سنقوم بالعمل علية هو محتوى تعليمي علمي 
- هل الصور والرسوم مهمة؟جدا جدا لنفس السبب
- هل نحتاج citations دقيقة بالصفحة؟نعم ليكون من السهل للمستخدم النهائي الحصول على المصدر الاساسي اذا احتاج ذالك 
- هل نحتاج تشغيل محلي لأسباب خصوصية؟ السبب هو التوفير يمكن ان نستخدم vps
- هل نحتاج API لفريق؟ لا اعرف ربما لاحقا 
- هل حجم الملفات كبير؟نعم جدا كبير اكثر من 5T  وربما 10T 
- هل عندنا GPU؟ نعم لاكن 2VRAM 
- هل نحتاج تحويل يومي مستمر أم استخدام متقطع؟في البداية متقطع ثم لاحقا بشكل مستمر 
- هل نريد حفظ Markdown فقط أم JSON أيضاً؟ كل ما هو ممكن و DoclingDocument
- هل نريد إدخال المخرجات في Obsidian؟ ليس اهم شيء لاكن جيد ان يكون موجود 
- هل نريد بناء قاعدة معرفة كاملة؟نعم عملاقة 

## قرار عملي مبدئي

لو كان الهدف الآن فهم Docling واستيعاب قدراتها، أفضل مسار:

1. شغلها محلياً في المشروع.
2. لا تبدأ بـ Docling Serve.
3. لا تبدأ بـ VLM.
4. اختبر standard pipeline على ملفات حقيقية.
5. احفظ Markdown و JSON.
6. قيّم الجداول وOCR وترتيب القراءة.
7. بعد ذلك قرر هل تحتاج:
   - OCR engine معين.
   - VLM.
   - Serve API.
   - MCP.
   - GPU.
   - post-processing خاص.

## أوامر مفيدة كبداية

تثبيت:

```powershell
pip install docling
```

تحويل ملف:

```powershell
docling "C:\path\to\file.pdf"
```

تحويل رابط:

```powershell
docling https://arxiv.org/pdf/2206.01062
```

تثبيت دعم VLM:

```powershell
pip install "docling[vlm]"
```

تشغيل VLM pipeline:

```powershell
docling --pipeline vlm --vlm-model granite_docling "C:\path\to\file.pdf"
```

تثبيت Serve:

```powershell
pip install "docling-serve[ui]"
docling-serve run --enable-ui
```

تنزيل النماذج مسبقاً:

```powershell
docling-tools models download
```

## ملاحظات حول Windows

Docling تدعم Windows حسب التوثيق وPyPI. لكن بعض الأشياء قد تحتاج انتباه:

- PyTorch قد يثبت نسخة كبيرة.
- OCR engines قد تحتاج تثبيتات إضافية.
- Tesseract يحتاج تثبيت نظامي وملفات لغة.
- GPU على Windows قد يكون أسهل عبر CUDA لبعض المراحل، أما vLLM غالباً ليس الخيار الأول على Windows.
- LM Studio أو Ollama قد يكونان أسهل لتجربة endpoints محلية متوافقة مع OpenAI API.

## هل نحتاج Hugging Face؟

ليس بالضرورة كمستخدم عادي. لكن Hugging Face مهم لأن:

- نماذج Docling موجودة هناك.
- Granite-Docling وSmolDocling ونماذج أخرى يمكن تنزيلها.
- بعض النماذج تعمل عبر Transformers أو MLX.

إذا شغلت Docling لأول مرة، قد تنزل النماذج تلقائياً. إذا أردت offline، نزّلها مسبقاً.

## نقاط قوة المشروع كمنظومة

Docling ليست repo واحداً فقط. توجد منظومة:

- `docling`: المكتبة والـ CLI.
- `docling-core`: تمثيل ومكونات أساسية.
- `docling-serve`: API service.
- `docling-mcp`: أدوات MCP للـ agents.
- `docling-models`: نماذج Hugging Face.
- تكاملات مع LangChain وLlamaIndex وHaystack وCrew AI وOpen WebUI وApify وغيرها.

هذا يجعلها قابلة للتوسع من تجربة محلية صغيرة إلى خدمة إنتاجية.

## الخلاصة العملية

Docling مناسبة جداً إذا كان هدفك تحويل المستندات إلى مادة قابلة للفهم والمعالجة من أنظمة الذكاء الاصطناعي. قوتها ليست فقط في أنها تقرأ PDF، بل في أنها تفهم البنية: layout، tables، reading order، formulas، code، images، OCR، ثم تعطيك تمثيلاً موحداً قابلاً للتصدير والتقسيم.

للاستخدام الشخصي أو التجريبي: شغلها محلياً.

للتطبيقات والفِرق: شغل `docling-serve`.

للوكلاء: استخدم `docling-mcp`.

للصفحات البصرية المعقدة: جرّب VLM مثل Granite-Docling.

للـ RAG: لا تعتمد على Markdown فقط؛ احتفظ بـ JSON/DoclingDocument وفكر في chunking يحافظ على العناوين والجداول والصفحات.

أفضل خطوة تالية: اختيار 5 ملفات حقيقية من مشروعك واختبارها واحداً واحداً، ثم كتابة تقييم جودة لكل ملف: النص، الجداول، الصور، OCR، الزمن، والمخرجات المناسبة.

## دمج Mistral OCR مع Docling

السؤال هنا ليس فقط: "هل يمكن استخدام Mistral OCR؟" بل: أين نضعه داخل بنية Docling؟

النتيجة المختصرة: يمكن دمج Docling و Mistral OCR معاً بشكل ممتاز على مستوى workflow، لكن لا يبدو أن هناك تكاملاً native جاهزاً داخل Docling باسم `mistral-ocr`. الدمج الطبيعي ممكن، لكن درجته تختلف حسب الهدف:

- سهل جداً: استخدام Mistral OCR كمرحلة خارجية تنتج Markdown أو JSON، ثم استخدام الناتج في RAG أو Obsidian أو pipeline بجانب Docling.
- متوسط: تحويل مخرجات Mistral OCR إلى `DoclingDocument` عبر adapter خاص.
- أصعب: جعله OCR engine داخلي داخل Docling مثل RapidOCR أو Tesseract أو EasyOCR، لأن Docling يتوقع OCR stage متناسقة مع layout/page cells، بينما Mistral OCR يعطي مخرجات أعلى مستوى مثل Markdown وtables وimages وheaders وfooters وannotations وmetadata.

### ما الذي يقدمه Mistral OCR؟

Mistral OCR، خصوصاً OCR 3 أو `mistral-ocr-2512`، مصمم لاستخراج النص والصور والجداول من PDFs/images إلى Markdown أو structured JSON.

حسب صفحات Mistral الرسمية، قدراته تشمل:

- استخراج text و embedded images.
- الحفاظ على structure و hierarchy.
- دعم headers و paragraphs و lists و tables.
- دعم `table_format` بصيغ مثل `markdown` أو `html`.
- استخراج headers و footers في OCR 2512 أو أحدث.
- التعامل مع multi-column layouts.
- التعامل مع scanned documents وlow-quality scans.
- دعم forms وinvoices وreceipts وoperational documents.
- دعم handwriting بشكل أفضل في OCR 3.
- إعادة بناء الجداول المعقدة مع merged cells وmulti-row blocks وcolumn hierarchies.
- مخرجات تحتوي pages، markdown، images، tables، hyperlinks، header، footer، dimensions، confidence scores، وusage metadata.

هذا يجعله أقرب إلى document understanding service وليس OCR تقليدي فقط.

### هل يمكن تشغيل Mistral OCR محلياً؟

عملياً، ليس كأداة open-source متاحة لنا فوراً.

Mistral تذكر أن self-hosting متاح بشكل selective للمنظمات التي لديها متطلبات خصوصية عالية. كما أن صفحة model card الخاصة بـ OCR تذكر أن الوصول إلى weights يتطلب التواصل معهم. لذلك لا نتعامل معه مثل Tesseract أو RapidOCR أو EasyOCR أو SuryaOCR التي يمكن تثبيتها وتشغيلها مباشرة.

القرار الواقعي لنا:

- Docling محلياً على الجهاز.
- Mistral OCR عبر API key عند الحاجة.
- self-hosting لـ Mistral OCR فقط إذا كان لدينا اتفاق أو وصول مؤسسي من Mistral.

وبما أن الجهاز الحالي لديه GPU بذاكرة صغيرة تقريباً `2GB VRAM`، فلا ينبغي أن نبني الخطة على تشغيل Mistral OCR محلياً حتى لو أصبح الوصول إليه ممكناً. الأفضل أن يكون خيار Mistral عبر API أو batch API.

### أين يتناغم مع Docling؟

Docling قوي كمنظومة كاملة:

- يدعم صيغ كثيرة.
- يبني `DoclingDocument`.
- يملك chunkers.
- يصدّر Markdown وJSON وHTML.
- يدعم layout وtables وOCR engines وVLM pipeline.
- مناسب كطبقة ingest قبل RAG.

أما Mistral OCR فهو قوي كـ OCR/document understanding service:

- مناسب للمستندات الممسوحة.
- مناسب للجداول الصعبة.
- مناسب للعربية واللغات المتعددة إذا أعطى جودة أعلى من OCR المحلي.
- مناسب للنماذج والفواتير والـ forms.
- مناسب عندما نريد Markdown/JSON نظيف بسرعة عبر API.

التناغم الأفضل:

- Docling = الهيكل والمنظومة والتحويل وRAG/chunking.
- Mistral OCR = محرك خارجي ممتاز للصفحات الصعبة أو الملفات التي يفشل فيها OCR المحلي.

### هل يمكن استخدامهما كأداتين معاً بشكل native وطبيعي؟

يمكن استخدامهما معاً بشكل طبيعي جداً على مستوى workflow، لكن ليس بالضرورة native داخل Docling من اليوم الأول.

Docling لديه نظام plugins، وفيه OCR factory يسمح بإضافة OCR engines خارجية. حسب توثيق Docling، أي OCR engine جديد يحتاج أن يطبّق `BaseOcrModel` وأن يوفّر options class مشتقة من `OcrOptions`. ويمكن تفعيل plugins الخارجية عبر `allow_external_plugins`.

هذا يعني أن تكامل Mistral OCR كـ plugin ممكن نظرياً.

لكن عملياً هناك فرق مهم:

- Docling OCR stage غالباً تتعامل مع نصوص/خلايا/مواقع مرتبطة بالصفحة.
- Mistral OCR يعيد مخرجات document-level أعلى مستوى: Markdown، جداول، صور، headers، footers، annotations.

لذلك لو جعلناه OCR engine داخلياً فقط، قد نخسر جزءاً من قوته. ربما الأفضل أن نعامله كـ parser بديل أو enrichment/adapter وليس مجرد OCR engine.

### طرق الدمج الممكنة

#### 1. Side-by-side pipeline

هذه أبسط طريقة وأفضل نقطة بداية.

الفكرة:

1. نعالج الملفات العادية عبر Docling.
2. نعالج الملفات الصعبة عبر Mistral OCR.
3. نحفظ مخرجات الاثنين في صيغة موحدة داخل مشروعنا.
4. نستخدم الناتج في RAG أو Obsidian أو قاعدة معرفة.

متى نستخدمها؟

- في البداية.
- عندما نريد مقارنة الجودة.
- عندما لا نريد تعديل كود Docling.
- عندما نريد fallback سريع للملفات التي يفشل فيها Docling OCR.

مثال قرار:

- PDF نصي واضح: Docling.
- PDF ممسوح عربي: Mistral OCR.
- جدول صعب جداً: جرّب Docling وMistral وقارن.
- ملفات كثيرة: Docling محلياً، ومسترال للعينات الصعبة أو batch عند الحاجة.

#### 2. Mistral-to-DoclingDocument adapter

هذه هي الطريقة الأكثر توازناً.

الفكرة:

1. نرسل PDF أو image إلى Mistral OCR.
2. نستقبل response فيه `pages[].markdown` و`tables` و`images` و`header` و`footer` و`dimensions`.
3. نبني منها تمثيلاً داخلياً موحداً في مشروعنا.
4. إن أمكن، نحولها لاحقاً إلى `DoclingDocument` أو إلى Markdown/JSON قريب من بنية Docling.

هذه الطريقة تسمح لنا بالاستفادة من مخرجات Mistral القوية بدون إجبارها على أن تكون OCR engine منخفض المستوى.

هذا مناسب جداً إذا كان هدفنا:

- RAG.
- بناء قاعدة معرفة.
- حفظ الصفحات والجداول والصور.
- مقارنة مخرجات Mistral مع Docling.
- عمل pipeline خاص بنا فوق الأداتين.

#### 3. Docling OCR plugin

هذه أقرب طريقة للـ native integration.

الفكرة:

1. نكتب `MistralOcrOptions`.
2. نكتب `MistralOcrModel` يطبق `BaseOcrModel`.
3. نستدعي Mistral API داخله.
4. نحول response إلى الشكل الذي تتوقعه مرحلة OCR في Docling.
5. نسجل plugin عبر Python entrypoint.
6. نشغل Docling مع:

```python
pipeline_options.allow_external_plugins = True
pipeline_options.ocr_options = MistralOcrOptions(...)
```

أو من CLI بشكل شبيه:

```powershell
docling --allow-external-plugins --ocr-engine=NAME
```

هذه الطريقة ممكنة، لكنها تحتاج قراءة كود Docling الداخلي جيداً، خصوصاً `BaseOcrModel` ومخرجات OCR engines الافتراضية. هي ليست أول خطوة مناسبة.

#### 4. Mistral كـ VLM/API pipeline بديل

Docling يدعم VLM pipeline مع engines مثل `api` و`api_openai` و`api_ollama` و`api_lmstudio`. لكن Mistral OCR API ليست بالضرورة نفس شكل Chat Completions أو OpenAI-compatible VLM endpoint؛ لديها `/v1/ocr` ومخرجات خاصة.

لذلك لا ينبغي افتراض أنه يمكن توصيل `mistral-ocr-latest` مباشرة كـ VLM remote model داخل Docling بدون adapter. لو استخدمنا Mistral multimodal chat model مختلفاً عبر API قد يكون الأمر مختلفاً، لكن Mistral OCR نفسه API متخصص.

### ما هو أفضل مسار لنا؟

لا نبدأ بمحاولة دمج Mistral OCR داخل Docling كـ native OCR engine.

الأفضل:

1. نبني تجربة مقارنة بسيطة:
   - ملف PDF نصي.
   - ملف PDF ممسوح.
   - ملف عربي.
   - ملف فيه جدول صعب.
   - ملف فيه صور أو charts.

2. نمرر الملفات عبر:
   - Docling standard pipeline.
   - Docling مع OCR محلي مثل RapidOCR أو Tesseract أو EasyOCR.
   - Mistral OCR API.

3. نقارن:
   - جودة النص.
   - ترتيب القراءة.
   - الجداول.
   - العربية.
   - الصور.
   - المخرجات JSON/Markdown.
   - السرعة.
   - التكلفة.

4. بعد ذلك نقرر:
   - هل Mistral يكون fallback فقط؟
   - هل يكون parser أساسي للملفات الصعبة؟
   - هل نحتاج adapter؟
   - هل يستحق بناء plugin حقيقي؟

### قرار تقني مبدئي

القرار الأكثر عقلانية:

- استخدم Docling محلياً كأساس.
- استخدم Mistral OCR عبر API كمحرك premium/fallback للملفات الصعبة.
- لا تعتمد على self-hosting لـ Mistral OCR إلا إذا حصلنا على وصول رسمي.
- لا تحاول إدخاله كـ native plugin فوراً.
- ابنِ adapter خارجي أولاً.
- إذا أثبتت التجارب أن Mistral OCR ضروري ومتكرر، عندها نبني plugin داخل Docling.

### تصور architecture مبدئي

```text
Input files
    |
    v
Document router
    |
    +--> Docling local pipeline
    |        |
    |        +--> DoclingDocument
    |        +--> Markdown
    |        +--> JSON
    |
    +--> Mistral OCR API for hard cases
             |
             +--> OCR pages markdown
             +--> tables/images/header/footer
             +--> Mistral JSON
             |
             v
       Adapter / normalizer
             |
             +--> unified Markdown
             +--> unified JSON
             +--> possible DoclingDocument-like structure
```

### الخلاصة

Docling وMistral OCR متناغمان كمكوّنين في نظام واحد، لكن ليسا نفس الشيء.

Docling هو framework محلي ومفتوح المصدر لبناء document processing pipeline. Mistral OCR هو API قوي لفهم المستندات واستخراج Markdown/JSON من PDFs/images. يمكن أن يكون Mistral OCR إضافة ممتازة فوق Docling، خصوصاً للملفات العربية والممسوحة والجداول الصعبة.

أفضل دمج الآن ليس "نحشر Mistral داخل Docling"، بل "نستخدم Docling كمنظومة أساسية، ونستخدم Mistral OCR كمسار بديل أو premium parser، ثم نوحد المخرجات في طبقة adapter".

## مصادر وروابط

- [Docling official website](https://www.docling.ai/)
- [docling-project/docling on GitHub](https://github.com/docling-project/docling)
- [Docling documentation](https://docling-project.github.io/docling/)
- [Docling supported formats](https://docling-project.github.io/docling/usage/supported_formats/)
- [Docling installation](https://docling-project.github.io/docling/getting_started/installation/)
- [Docling advanced options](https://docling-project.github.io/docling/usage/advanced_options/)
- [Docling model catalog](https://docling-project.github.io/docling/usage/model_catalog/)
- [Docling GPU support](https://docling-project.github.io/docling/usage/gpu/)
- [Docling enrichments](https://docling-project.github.io/docling/usage/enrichments/)
- [Docling chunking](https://docling-project.github.io/docling/concepts/chunking/)
- [Docling models on Hugging Face](https://huggingface.co/docling-project/docling-models)
- [Docling on PyPI](https://pypi.org/project/docling/)
- [Docling Serve](https://github.com/docling-project/docling-serve)
- [Docling MCP](https://github.com/docling-project/docling-mcp)
- [IBM Research: Docling AAAI 2025 publication](https://research.ibm.com/publications/docling-an-efficient-open-source-toolkit-for-ai-driven-document-conversion)
- [IBM: Granite-Docling end-to-end document understanding](https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion)
- [arXiv: Docling technical report](https://arxiv.org/abs/2408.09869)
- [arXiv: Docling efficient open-source toolkit](https://arxiv.org/abs/2501.17887)
- [Mistral OCR announcement](https://mistral.ai/news/mistral-ocr/)
- [Mistral OCR 3 announcement](https://mistral.ai/news/mistral-ocr-3/)
- [Mistral Document AI](https://mistral.ai/solutions/document-ai/)
- [Mistral OCR Processor docs](https://docs.mistral.ai/studio-api/document-processing/basic_ocr)
- [Mistral OCR 3 model card](https://docs.mistral.ai/models/model-cards/ocr-3-25-12)
- [Mistral OCR data extraction cookbook](https://docs.mistral.ai/resources/cookbooks/mistral-ocr-data_extraction)
- [Mistral OCR batch cookbook](https://docs.mistral.ai/resources/cookbooks/mistral-ocr-batch_ocr)
- [Mistral OCR cookbook on GitHub](https://github.com/mistralai/cookbook/tree/main/mistral/ocr)
