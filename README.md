# فرع docling: خط أنابيب Docling للاستخراج والتنظيم

هذا الفرع مخصص فقط للجزء المتعلق بـ Docling وتنظيم الملفات غير المهيكلة قبل استخدامها في RAG.

الفرع لا يحتوي على تطبيق RAG الموجود في `main`، ولا يحتوي على ملفات PDF أو PPT أو صور أو Chroma index أو مخرجات ضخمة. الهدف هنا هو توثيق ورفع الكود الذي يشرح كيف تمت عملية الاستخراج والتنظيم.

الشرح هنا عربي بالأساس، لكن أسماء الأدوات والمفاهيم التقنية ستبقى بالإنجليزية عندما يكون ذلك أوضح، مثل: `Docling`, `DoclingDocument`, `OCR`, `RAG`, `metadata`, `chunks`, `pipeline`.

## ماذا يوجد في هذا الفرع؟

- `docling_extraction/build_slides_output.py`
  سكربت Python يقوم بفحص مجلد مواد خام مثل `Slides/` ثم ينشئ مجلد `Output/` منظم.

- `requirements.txt`
  الاعتمادات المطلوبة لتشغيل السكربت.

- `.gitignore`
  يستبعد المخرجات الضخمة مثل `Output/` وملفات الكاش.

- `docs/DocLing.md`
  مذكرة موسعة لفهم Docling، قدراته، تشغيله محلياً، علاقته بـ `DoclingDocument`، واستخدامه مع RAG.

- `docs/UnstructuredDataArchitecture.md`
  دراسة معمارية لحالة بيانات تعليمية ضخمة وغير مهيكلة، وكيف يمكن تنظيمها قبل RAG أو GraphRAG.

## الفكرة العامة

عند وجود مجلد كبير يحتوي ملفات غير مهيكلة مثل:

- PDF عادي.
- PDF ممسوح ضوئياً.
- PPTX.
- PPT قديم.
- صور.
- ملفات Markdown أو Text.

فالهدف هو عدم إدخال هذه الملفات مباشرة إلى RAG. الأفضل أولاً بناء طبقة منظمة تحتوي:

- فهرس كامل للملفات.
- سجل مصادر مع `sha256`.
- كشف التكرارات.
- استخراج نصوص.
- استخراج صور وصفحات ملتقطة.
- تصنيف أولي للمواضيع.
- طابور مراجعة للملفات الضعيفة أو التي تحتاج OCR.
- chunks مناسبة لاحقاً لـ RAG.

هذا السكربت هو الطبقة التي تقوم بذلك.

## ما علاقة Docling هنا؟

السكربت يستخدم أكثر من طريقة استخراج:

- `PyMuPDF` لاستخراج النصوص من PDF ورندر صفحات للمراجعة.
- `python-pptx` لاستخراج نصوص وصور PPTX.
- `Pillow` لمعالجة الصور وcontact sheets.
- `Docling` اختيارياً على الملفات الصغيرة لإنتاج `DoclingDocument` وتصديره إلى Markdown وJSON.

Docling هنا ليس بديلاً عن كل شيء، بل جزء من pipeline أوسع. السبب أن بعض الملفات كبيرة جداً، وتشغيل Docling عليها كلها قد يكون بطيئاً. لذلك الوضع الافتراضي يشغل Docling فقط على عدد محدود من الملفات الصغيرة.

## ما هو DoclingDocument؟

`DoclingDocument` هو التمثيل الداخلي المنظم للمستند داخل Docling.

بدلاً من التعامل مع الملف كـ PDF أو DOCX أو صورة فقط، يحاول Docling تحويله إلى كائن موحد يحتوي بنية المستند بعد الفهم والمعالجة، مثل:

- العناوين.
- الفقرات.
- الجداول.
- الصور.
- المعادلات.
- كتل الكود.
- القوائم.
- ترتيب القراءة.
- الصفحات.
- مواقع العناصر داخل الصفحة.
- metadata.
- علاقات مثل caption مع صورة أو جدول.

بعد ذلك يمكن تصديره إلى:

```python
result.document.export_to_markdown()
result.document.export_to_dict()
```

أهميته تظهر في RAG لأن التقسيم يصبح مبنياً على بنية المستند وليس على نص مسطح فقط.

## طريقة التشغيل

ثبت الاعتمادات:

```powershell
pip install -r requirements.txt
```

ثم شغل السكربت على مجلد مواد خام:

```powershell
python docling_extraction/build_slides_output.py Slides
```

هذا سينشئ:

```text
Slides/Output/
```

## بنية المخرجات

بعد التشغيل، ينتج السكربت بنية مثل:

```text
Output/
  00-catalog.md
  01-topic-map.md
  02-source-register.md
  03-assets-index.md
  04-review-queue.md
  05-processing-log.md
  06-deduplication-report.md
  sources/
  topics/
  assets/
  unresolved/
  docling-json/
  rag-chunks/
```

شرح سريع:

- `00-catalog.md`: فهرس كل الملفات الأصلية.
- `01-topic-map.md`: تصنيف أولي حسب الموضوع.
- `02-source-register.md`: سجل المصادر مع hash والحالة.
- `03-assets-index.md`: فهرس الصور والصفحات الملتقطة.
- `04-review-queue.md`: ما يحتاج OCR أو مراجعة.
- `05-processing-log.md`: سجل التشغيل.
- `06-deduplication-report.md`: تقرير التكرارات.
- `sources/`: ملف Markdown لكل مصدر.
- `docling-json/`: JSON منظم ونتائج Docling عند توفرها.
- `rag-chunks/`: chunks جاهزة ليستخدمها تطبيق RAG لاحقاً.

## أوامر مهمة

تعطيل Docling بالكامل:

```powershell
python docling_extraction/build_slides_output.py Slides --docling-mode off
```

تشغيل Docling على ملفات صغيرة فقط:

```powershell
python docling_extraction/build_slides_output.py Slides --docling-mode small --docling-max-mb 0.2 --docling-max-files 3
```

تقليل عدد صفحات PDF الملتقطة لكل ملف:

```powershell
python docling_extraction/build_slides_output.py Slides --max-captures-per-source 40
```

## ماذا يحدث مع ملفات PPT القديمة؟

ملفات `.ppt` القديمة لا يتم تجاهلها. السكربت يسجلها في الفهرس وسجل المصادر، لكنها تدخل في طابور المراجعة لأنها تحتاج غالباً إلى تحويل عبر LibreOffice أو معالجة يدوية.

## ماذا يحدث مع الصور وPDF الممسوح؟

الصور والصفحات ذات النص الضعيف يتم تسجيلها كمرشحات OCR داخل `04-review-queue.md`.

النسخة الحالية لا تستخدم Mistral OCR ولا أي API خارجي. هي محلية أولاً.

## هل هذا يؤثر على فرع main؟

لا. هذا branch منفصل باسم `docling`.

- فرع `main`: تطبيق RAG الجاهز للتشغيل.
- فرع `docling`: كود Docling/extraction والتنظيم فقط.

## اختبار سريع

افحص صحة السكربت:

```powershell
python -m py_compile docling_extraction/build_slides_output.py
```

ثم جربه على مجلد صغير:

```powershell
python docling_extraction/build_slides_output.py path\to\sample-folder --docling-mode off
```

بعدها افحص:

```text
path\to\sample-folder\Output\05-processing-log.md
path\to\sample-folder\Output\rag-chunks\
```


