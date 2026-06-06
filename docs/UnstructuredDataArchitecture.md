# Unstructured Data Architecture

> تاريخ المذكرة: 2026-06-04
>
> الهدف: دراسة حالة واقعية ضخمة فيها بيانات غير مهيكلة، PDFs، صور، Word، PowerPoint، فيديوهات، جداول، رسومات، معادلات، عربي/إنجليزي مختلط، وحجم قد يصل إلى 5TB أو أكثر. الغرض هو تصميم طريقة تفكير وبنية عمل لتحويل هذه الفوضى إلى معرفة منظمة قابلة للاستخدام في AI Agents وRAG وGraphRAG وربما التدريب لاحقاً.

## الخلاصة السريعة

الحالة هنا ليست مجرد "نحوّل PDF إلى Markdown". هذه حالة بناء نظام ingest كامل لمستودع معرفة ضخم وغير منظم.

نحتاج إلى pipeline يتعامل مع:

- ملفات PDF نصية.
- ملفات PDF ممسوحة ضوئياً.
- صور فيها نص عربي/إنجليزي.
- صور فيها شروحات علمية ورسومات أجهزة ودوائر كهربائية.
- جداول وcharts ورسوم بيانية.
- معادلات رياضية.
- PowerPoint وWord.
- فيديوهات بأسماء غير مفهومة أو أرقام فقط.
- ملفات غير مصنفة حسب المادة أو الموضوع.
- حجم كبير جداً: 5TB أو أكثر.

الهدف ليس استخراج النص فقط، بل بناء طبقة معرفة منظمة:

- تصنيف الملفات حسب المادة والموضوع.
- استخراج النصوص والجداول والصور والرسومات والمعادلات.
- حفظ metadata قوية.
- بناء فهرس قابل للبحث.
- تجهيز البيانات لـ RAG وGraphRAG وAI Agents.
- تجهيز نسخ منظمة يمكن لاحقاً استخدامها في training أو fine-tuning أو dataset curation.

القرار العملي المبدئي:

- Docling يكون الأساس المحلي للمعالجة والتحويل والبنية.
- Mistral OCR يستخدم كمسار premium أو fallback للملفات الصعبة: العربي، scanned PDFs، handwriting، الجداول الصعبة، والـ forms.
- لا نعالج 5TB دفعة واحدة.
- نبدأ بمرحلة inventory وsampling وclassification.
- نبني manifest لكل ملف قبل أي OCR ثقيل.
- نحفظ كل شيء كـ artifacts منظمة: original، extracted، normalized، metadata، QA notes.

## المشكلة الحقيقية

المشكلة ليست في وجود ملفات كثيرة فقط. المشكلة أن الملفات لا تحمل بنية واضحة.

قد يكون اسم الملف:

```text
1.pdf
22.pptx
scan_0045.jpg
IMG_20240103.png
lecture.mp4
```

ولا نعرف:

- ما المادة؟
- ما المحاضرة؟
- ما الموضوع؟
- هل الملف كامل أم جزء؟
- هل فيه نص قابل للاستخراج؟
- هل هو scan؟
- هل يحتوي جداول؟
- هل يحتوي رسومات مهمة؟
- هل فيه عربي أم إنجليزي أم خليط؟
- هل هو مصدر أساسي أم نسخة مكررة؟
- هل جودة النص كافية؟

لذلك يجب أن نفكر في النظام كأنه مشروع data engineering قبل أن يكون مشروع AI.

## الهدف النهائي

الهدف النهائي هو تحويل مستودع ملفات غير مهيكل إلى Knowledge Corpus منظم.

هذا corpus يجب أن يدعم:

- البحث النصي التقليدي.
- البحث الدلالي embeddings.
- RAG.
- GraphRAG.
- AI Agent يستطيع فتح الملفات وفهم السياق.
- توليد دروس أو ملخصات أو خرائط معرفة.
- استخراج صور وجداول ومعادلات كمصادر قابلة للاستدعاء.
- ربط كل معلومة بمصدرها الأصلي: الملف، الصفحة، الشريحة، timestamp، أو مكان الصورة.

القاعدة الأساسية:

> لا يكفي أن نستخرج النص. يجب أن نحفظ العلاقة بين النص ومصدره وبنيته وسياقه.

## لماذا metadata مهمة جداً؟

في مشروع بهذا الحجم، metadata ليست إضافة ثانوية. هي العمود الفقري.

بدون metadata، سنحصل على آلاف أو ملايين المقاطع النصية، لكن لن نعرف:

- من أين جاءت؟
- ما موثوقيتها؟
- ما المادة التي تنتمي إليها؟
- هل هي من PDF أو صورة أو فيديو؟
- هل جاءت من OCR أو نص أصلي؟
- هل فيها جدول؟
- هل فيها معادلة؟
- هل تم التحقق منها؟
- هل اللغة عربية أم إنجليزية؟
- هل الملف مكرر؟
- هل النص مستخرج بجودة عالية أم منخفضة؟

في RAG، ضعف metadata يجعل الإجابات تبدو صحيحة لكنها غير قابلة للتتبع. وفي GraphRAG، ضعف metadata يجعل العلاقات بين المفاهيم عشوائية.

## أنواع البيانات في هذه الحالة

### 1. PDFs نصية

هذه غالباً أسهل نوع. يمكن أن يعالجها Docling محلياً.

لكن حتى PDF النصي قد يحتوي:

- أعمدة.
- جداول.
- معادلات.
- صور.
- ترويسات وتذييلات.
- ترتيب قراءة غير صحيح.
- نص عربي/إنجليزي مختلط.

لذلك لا نستخدم extractor بسيط فقط. نستخدم Docling لأنه يحاول حفظ البنية.

### 2. PDFs ممسوحة ضوئياً

هذه تحتاج OCR.

المسارات الممكنة:

- Docling مع OCR محلي مثل RapidOCR أو Tesseract أو EasyOCR.
- Mistral OCR API للملفات الصعبة.
- ربما لاحقاً أدوات أخرى إذا فشل الاثنان.

الأولوية:

- العربية المختلطة مع الإنجليزية.
- scans منخفضة الجودة.
- handwriting.
- الجداول داخل scans.

هذه الملفات يجب أن تحصل على metadata توضّح أنها processed_by_ocr، وأن جودة OCR قد تحتاج مراجعة.

### 3. الصور

الصور ليست كلها نفس النوع.

قد تكون:

- صورة نص فقط.
- صورة شاشة slide.
- صورة جدول.
- صورة chart.
- صورة رسم دائرة كهربائية.
- صورة جهاز أو block diagram.
- صورة معادلات.
- صورة تعليق عربي على نص إنجليزي.

لا ينبغي أن نعامل كل الصور كـ OCR فقط. بعضها يحتاج image classification، وبعضها يحتاج captioning، وبعضها يحتاج extraction، وبعضها يجب حفظه كما هو وربطه بالنص.

### 4. PowerPoint

ملفات PowerPoint مهمة لأنها قد تحتوي:

- نصوص قصيرة لكنها عالية الكثافة.
- صور وdiagrams.
- جداول.
- charts.
- معادلات.
- speaker notes.
- ترتيب بصري لا يظهر جيداً عند التحويل النصي.

Docling يمكنه قراءة PPTX، لكن يجب اختبار جودة extraction. قد نحتاج أيضاً إلى rendering لكل slide كصورة ثم OCR/VLM عند الشرائح المعقدة.

### 5. Word

ملفات Word غالباً أسهل من PDF، لكنها قد تحتوي:

- جداول.
- صور.
- معادلات.
- تنسيق عناوين.
- تعليقات.
- مراجع.

Docling مناسب هنا لأنه يحولها إلى بنية موحدة.

### 6. الفيديوهات

الفيديوهات مشكلة مختلفة.

يجب استخراج:

- الصوت.
- transcript.
- timestamps.
- frames أو keyframes.
- slides الظاهرة في الفيديو إن وجدت.
- علاقة كل مقطع transcript بالزمن.

الهدف ليس فقط تفريغ الصوت. في المواد العلمية، قد يقول المحاضر "كما ترون هنا" ويشير إلى رسم أو معادلة. لذلك نحتاج ربط transcript بالـ frames أو slides.

## الفلسفة العامة للمعالجة

لا نعالج كل شيء بأقوى أداة من البداية. هذا سيكون مكلفاً وبطيئاً وغير مضبوط.

نستخدم routing:

- الملفات السهلة: Docling محلياً.
- الملفات الصعبة: Docling مع OCR.
- الملفات الأصعب: Mistral OCR.
- الفيديوهات: ASR + keyframes + OCR/VLM للشرائح.
- الصور العلمية: OCR + classification + caption/annotation عند الحاجة.

هذه ليست pipeline واحدة ثابتة. هي منظومة قرار.

## المرحلة 0: Inventory قبل أي AI ثقيل

قبل التحويل، يجب بناء manifest كامل لكل الملفات.

الهدف: معرفة ماذا نملك.

لكل ملف نسجل:

- `file_id`
- `original_path`
- `filename`
- `extension`
- `size_bytes`
- `created_time`
- `modified_time`
- `hash_sha256`
- `mime_type`
- `parent_folder`
- `relative_path`
- `suspected_course`
- `suspected_topic`
- `processing_status`
- `duplicate_group_id`
- `notes`

هذه المرحلة لا تحتاج AI ثقيل. يمكن تنفيذها بسرعة نسبية على 5TB.

لماذا مهمة؟

- اكتشاف التكرارات.
- معرفة الحجم الفعلي حسب النوع.
- معرفة عدد PDFs والصور والفيديوهات.
- معرفة الملفات التالفة.
- بناء خطة تكلفة ووقت.
- منع معالجة نفس الملف مرتين.

## المرحلة 1: Deduplication

في مستودعات كبيرة، التكرار شائع جداً.

قد يوجد:

- نفس PDF في أكثر من مجلد.
- نسخة scan ونسخة text من نفس الملف.
- صور مكررة بأسماء مختلفة.
- PowerPoint محفوظ كـ PDF أيضاً.
- فيديوهات مكررة بجودة مختلفة.

نحتاج نوعين من deduplication:

### Exact duplicates

باستخدام hash مثل SHA256.

إذا كان hash نفسه، الملف مطابق تماماً.

### Near duplicates

أصعب، ويحتاج:

- perceptual hash للصور.
- مقارنة عدد الصفحات والعناوين.
- embeddings للنصوص.
- مقارنة metadata.
- مقارنة أسماء الملفات والمسارات.

لا نحذف النسخ مباشرة. نسجل العلاقة:

```yaml
duplicate_status: exact_duplicate
canonical_file_id: file_123
```

أو:

```yaml
duplicate_status: near_duplicate_candidate
confidence: 0.82
```

## المرحلة 2: تصنيف أولي للملفات

نحتاج تصنيف الملفات حسب:

- المادة: Microwave، Circuits، Signals، Control، Electronics، Math، Physics، إلخ.
- النوع: lecture، notes، slides، exam، solution، lab، assignment، reference.
- اللغة: Arabic، English، Mixed.
- الصعوبة: easy، medium، hard.
- نوع المعالجة المطلوبة: text extraction، OCR، VLM، ASR، manual review.

التصنيف يمكن أن يعتمد على:

- اسم المجلد.
- اسم الملف.
- النص المستخرج سريعاً من أول صفحات.
- OCR لعينة صغيرة.
- embeddings.
- LLM classification بعد استخراج عينة.

لا نحتاج دقة 100% في البداية. نحتاج تصنيفاً أولياً يساعد على routing.

## المرحلة 3: Routing

Routing يعني تحديد الأداة المناسبة لكل ملف.

مثال قواعد:

```yaml
if file_type in [docx, pptx, xlsx]:
  route: docling_standard

if file_type == pdf and has_embedded_text == true:
  route: docling_standard

if file_type == pdf and has_embedded_text == false:
  route: docling_ocr_or_mistral

if image_contains_text == true and language in [arabic, mixed]:
  route: mistral_ocr_candidate

if file_type == video:
  route: asr_plus_keyframes

if contains_complex_tables == true:
  route: docling_accurate_table_and_compare_mistral

if contains_circuit_diagrams == true:
  route: image_extract_plus_caption_or_manual_review
```

Routing مهم لأنه يمنع استخدام Mistral OCR أو VLM على كل شيء. هذا يوفر وقتاً وتكلفة.

## دور Docling في هذه المنظومة

Docling يكون المحرك المحلي الأساسي.

نستخدمه في:

- تحويل PDF/DOCX/PPTX/XLSX/HTML/images إلى بنية.
- استخراج Markdown.
- استخراج JSON.
- بناء `DoclingDocument`.
- استخراج الجداول.
- حفظ الصور.
- التعامل مع layout وreading order.
- chunking لاحقاً.

Docling مناسب للمرحلة الأساسية لأنه:

- يعمل محلياً.
- مفتوح المصدر.
- يدعم صيغاً كثيرة.
- يعطي تمثيلاً موحداً.
- مناسب لـ RAG.
- لا يتطلب إرسال البيانات للخارج افتراضياً.

لكن لا نفترض أنه سيحل كل شيء وحده. الملفات العربية الممسوحة والجداول الصعبة والـ handwriting قد تحتاج Mistral OCR أو مسار آخر.

## دور Mistral OCR

Mistral OCR يكون مساراً اختيارياً للملفات الصعبة.

نستخدمه عندما:

- OCR المحلي ضعيف.
- النص عربي/إنجليزي مختلط.
- الملف scanned بجودة سيئة.
- فيه handwriting.
- الجداول معقدة.
- نريد structured JSON بسرعة.
- نريد استخراج images/tables/header/footer بطريقة أفضل.

لكن لا نستخدمه لكل شيء من البداية لأن:

- يحتاج API key.
- فيه تكلفة.
- البيانات تخرج إلى خدمة خارجية.
- self-hosting ليس متاحاً عاماً.
- يجب التعامل مع rate limits وbatching.

أفضل استخدام له:

- fallback.
- premium parser.
- benchmark against Docling.
- معالجة ملفات عالية القيمة.

## فكرة Adapter موحد

نحتاج طبقة اسمها مثلاً:

```text
Document Normalization Adapter
```

هذه الطبقة تأخذ مخرجات أدوات مختلفة:

- Docling JSON.
- Docling Markdown.
- Mistral OCR JSON.
- ASR transcript.
- image captions.
- manual annotations.

وتحولها إلى schema موحد داخل مشروعنا.

لماذا؟

لأننا لا نريد أن يصبح المشروع تابعاً لأداة واحدة. إذا تغير Docling أو Mistral أو أضفنا أداة ثالثة، تبقى طبقة البيانات موحدة.

## Schema مقترح للملف

كل ملف أصلي يحصل على record:

```yaml
file_id: "file_000001"
original_path: "raw/Microwave/1.pdf"
canonical_path: "corpus/files/file_000001/original.pdf"
file_type: "pdf"
size_bytes: 12345678
sha256: "..."
course:
  predicted: "Microwave"
  confidence: 0.91
  source: "folder_name + classifier"
topic:
  predicted: "Waveguides"
  confidence: 0.74
language:
  primary: "mixed"
  detected: ["ar", "en"]
document_kind: "lecture_notes"
processing:
  status: "processed"
  route: "docling_standard"
  tools:
    - name: "docling"
      version: "..."
      options: {}
quality:
  extraction_quality: "medium"
  needs_review: true
created_at: "..."
updated_at: "..."
```

## Schema مقترح للصفحة أو الشريحة

```yaml
page_id: "file_000001_page_003"
file_id: "file_000001"
page_number: 3
page_type: "content"
has_text: true
has_table: true
has_image: true
has_formula: false
has_chart: true
language: "mixed"
ocr_used: false
source_dimensions:
  width: 1024
  height: 768
```

## Schema مقترح للعنصر المستخرج

كل عنصر داخل الصفحة يمكن أن يكون:

- paragraph.
- heading.
- table.
- image.
- chart.
- formula.
- code.
- list.
- caption.
- footnote.

مثال:

```yaml
element_id: "elem_000001"
file_id: "file_000001"
page_id: "file_000001_page_003"
type: "table"
text: "..."
markdown: "..."
html: "..."
bbox:
  x1: 100
  y1: 200
  x2: 900
  y2: 500
language: "mixed"
source_tool: "docling"
confidence: 0.82
related_elements:
  caption_id: "elem_000002"
```

هذا النوع من schema مهم جداً لـ GraphRAG لاحقاً.

## تنظيم المخرجات على القرص

لا نريد مخرجات عشوائية بجانب الملفات الأصلية. نحتاج بنية ثابتة.

اقتراح:

```text
corpus/
  manifest/
    files.parquet
    files.jsonl
    duplicates.jsonl
  raw/
    ...
  processed/
    file_000001/
      original.pdf
      metadata.yaml
      docling.json
      mistral_ocr.json
      markdown.md
      normalized.json
      pages/
        page_001.json
        page_001.png
      images/
        img_001.png
        img_001.metadata.yaml
      tables/
        table_001.html
        table_001.md
        table_001.csv
      chunks/
        chunks.jsonl
      qa/
        review.md
  indexes/
    lexical/
    vector/
    graph/
```

النقطة المهمة: لا نخلط original مع processed. ولا نرمي المخرجات في مجلد واحد ضخم.

## استخراج الصور والرسومات

الصور ليست مجرد مرفقات. في المواد العلمية، الصورة قد تكون أهم من النص.

نحتاج حفظ:

- الصورة الأصلية أو crop من الصفحة.
- الصفحة التي جاءت منها.
- bbox.
- caption إن وجد.
- وصف آلي.
- تصنيف نوع الصورة.
- علاقة الصورة بالموضوع.

تصنيفات مفيدة:

- `text_image`
- `circuit_diagram`
- `device_diagram`
- `block_diagram`
- `chart`
- `plot`
- `table_image`
- `formula_image`
- `screenshot`
- `photo`
- `unknown`

الرسومات مثل الدوائر الكهربائية قد لا تفهمها OCR. يجب حفظها وربطها بسياقها، وربما لاحقاً استخدام VLM أو مراجعة بشرية.

## الجداول

الجداول يجب أن تحفظ بأكثر من صيغة:

- Markdown للقراءة.
- HTML للحفاظ على merged cells.
- CSV عندما يكون ممكناً.
- JSON كبنية.
- صورة أو crop للمرجع البصري.

لماذا؟

لأن جدولاً مع خلايا مدمجة قد يتكسر في Markdown. HTML قد يحفظ `rowspan` و`colspan` بشكل أفضل. CSV جيد للتحليل، لكنه لا يحفظ كل البنية.

في RAG، يجب أن ترتبط chunk الخاصة بالجدول بـ:

- عنوان الجدول.
- الصفحة.
- الأعمدة.
- الوحدات.
- caption.
- الصورة الأصلية أو crop.

## المعادلات

المعادلات تحتاج تعامل خاص.

نريد:

- استخراجها كـ LaTeX إن أمكن.
- حفظ الصورة الأصلية للمعادلة.
- ربطها بالفقرة المحيطة.
- تحديد هل هي equation رئيسية أم جزء من النص.
- استخراج رقم المعادلة إن وجد.

مثال metadata:

```yaml
type: "formula"
latex: "V = IR"
source_image: "formula_003.png"
page: 12
nearby_heading: "Ohm's Law"
```

في المواد العلمية، المعادلة بلا سياق قد تكون عديمة الفائدة. لذلك يجب ربطها بالنص قبلها وبعدها.

## charts والرسوم البيانية

Charts تحتاج طبقتين:

1. وصف بصري: ماذا يظهر الرسم؟
2. بيانات مستخرجة إن أمكن: المحاور، الوحدات، القيم، العلاقات.

ليس كل chart يمكن استخراجه بدقة. لذلك نحتاج metadata:

```yaml
chart_type: "line_plot"
x_axis: "frequency"
y_axis: "gain"
units:
  x: "GHz"
  y: "dB"
data_extraction_quality: "low|medium|high"
needs_review: true
```

إذا كان chart مهماً، قد نحتاج human review أو أداة متخصصة لاستخراج بيانات الرسم.

## الفيديوهات

الفيديوهات يجب ألا تعامل كملف نصي فقط.

Pipeline مقترح:

1. استخراج metadata: مدة، دقة، codec، حجم.
2. استخراج الصوت.
3. ASR transcript مع timestamps.
4. استخراج keyframes كل مدة معينة أو عند تغير المشهد.
5. OCR/VLM على keyframes التي تحتوي slides أو نص.
6. ربط transcript بالـ keyframes.
7. تصنيف الفيديو حسب المادة والموضوع.

مثال:

```yaml
video_id: "file_000900"
duration: "01:22:10"
transcript_language: "mixed"
segments:
  - start: "00:12:30"
    end: "00:13:20"
    text: "..."
    keyframes: ["frame_0012.png"]
    detected_topic: "Smith Chart"
```

هذا مهم جداً في المواد العلمية لأن المعلومة قد تكون في كلام المحاضر والصورة معاً.

## التصنيف حسب المواد والمواضيع

لا نريد فقط folders. نريد taxonomies.

مثال:

```yaml
course: "Microwave"
topics:
  - "Transmission Lines"
  - "Smith Chart"
  - "Waveguides"
  - "S-Parameters"
  - "Impedance Matching"
```

ومادة أخرى:

```yaml
course: "Signals"
topics:
  - "Fourier Transform"
  - "Laplace Transform"
  - "Sampling"
  - "Filters"
  - "Convolution"
```

التصنيف يمكن أن يبدأ آلياً، لكن يجب السماح بتصحيح بشري. النظام يجب أن يحفظ:

- التصنيف المتوقع.
- الثقة.
- هل تم تأكيده بشرياً؟
- من أين جاء التصنيف؟

## GraphRAG

GraphRAG يحتاج علاقات، وليس نصاً فقط.

العقد الممكنة:

- Course.
- Topic.
- Concept.
- Equation.
- Figure.
- Table.
- File.
- Page.
- Lecture.
- Video segment.
- Person/author إن وجد.
- Device.
- Circuit.

العلاقات الممكنة:

- file belongs_to course.
- page discusses topic.
- equation supports concept.
- figure illustrates concept.
- table contains measurement.
- video_segment explains slide.
- topic depends_on topic.
- concept equivalent_to concept.
- concept contrasts_with concept.

مثال:

```text
Microwave -> contains_topic -> Smith Chart
Smith Chart -> used_for -> Impedance Matching
Figure_221 -> illustrates -> Smith Chart
Equation_045 -> belongs_to -> Transmission Line Theory
VideoSegment_003 -> explains -> Figure_221
```

هذه العلاقات يمكن استخراج بعضها آلياً، لكن لا يجب الوثوق بها كلها دون مراجعة أو confidence.

## RAG العادي

بالنسبة لـ RAG، نحتاج chunks جيدة.

chunk الجيد يجب أن يحتوي:

- نص واضح.
- heading path.
- course.
- topic.
- source file.
- page/slide/timestamp.
- نوع المصدر.
- اللغة.
- جودة الاستخراج.
- روابط للصور والجداول المرتبطة.

مثال chunk:

```json
{
  "chunk_id": "chunk_0001",
  "text": "...",
  "course": "Microwave",
  "topic": "Waveguides",
  "source_file": "file_000123",
  "page": 7,
  "heading_path": ["Chapter 3", "Rectangular Waveguides"],
  "contains_formula": true,
  "related_images": ["img_004"],
  "extraction_tool": "docling",
  "quality": "high"
}
```

## التدريب لاحقاً

إذا أردنا استخدام البيانات للتدريب لاحقاً، يجب أن ننتبه من الآن.

التدريب يحتاج بيانات أنظف من RAG.

نحتاج:

- إزالة التكرار.
- تنظيف النص.
- حفظ المصدر.
- حفظ اللغة.
- فصل النصوص الضعيفة.
- فصل OCR منخفض الجودة.
- استخراج Q/A pairs فقط من مصادر موثوقة.
- عدم إدخال بيانات مشكوك بها في dataset التدريب.

لذلك يجب أن تحتوي metadata على:

```yaml
training_candidate: true
training_quality: "high"
requires_human_review: false
copyright_status: "unknown"
```

## Quality Assurance

لا يمكن الوثوق بالمعالجة الآلية بالكامل. نحتاج QA.

مقاييس جودة:

- هل النص مقروء؟
- هل ترتيب القراءة صحيح؟
- هل الجداول مفهومة؟
- هل العربية سليمة؟
- هل الإنجليزية داخل العربية محفوظة؟
- هل المعادلات صحيحة؟
- هل الصور مستخرجة؟
- هل الصفحة مرتبطة بمصدرها؟
- هل التصنيف صحيح؟

نحتاج sampling:

- نراجع 20 ملفاً من كل مادة.
- نراجع 10 PDFs ممسوحة.
- نراجع 10 جداول صعبة.
- نراجع 10 صور عربية/إنجليزية.
- نراجع 5 فيديوهات.

ثم نحسب أين يفشل النظام.

## Human-in-the-loop

في مشروع بهذا الحجم، المراجعة البشرية يجب أن تكون ذكية وليست شاملة.

نراجع فقط:

- الملفات عالية القيمة.
- الملفات التي confidence منخفض.
- الملفات التي تحتوي أخطاء OCR واضحة.
- الملفات التي لم يستطع النظام تصنيفها.
- الجداول والمعادلات المهمة.
- المواد الأساسية لكل كورس.

يجب أن يكون هناك review queue:

```yaml
review_reason:
  - low_ocr_confidence
  - unknown_course
  - complex_table
  - arabic_mixed_text
  - possible_duplicate
priority: high
```

## التعامل مع الحجم الكبير 5TB+

5TB تعني أن أي قرار خاطئ سيكلف وقتاً كبيراً.

لا نبدأ هكذا:

```text
process everything with best model
```

نبدأ هكذا:

1. Inventory كامل.
2. Deduplication.
3. Sampling.
4. Benchmark صغير.
5. Routing rules.
6. Batch processing.
7. QA.
8. Incremental improvement.

يجب أن تكون المعالجة قابلة للاستئناف. إذا توقف الجهاز بعد 3 أيام، لا نعيد من الصفر.

كل ملف له status:

```yaml
status: pending | processing | processed | failed | needs_review | skipped
```

## التخزين

نحتاج التفكير في التخزين من البداية.

المخرجات قد تزيد الحجم:

- JSON.
- Markdown.
- صور مستخرجة.
- crops.
- page renders.
- transcripts.
- embeddings.
- indexes.

5TB أصلية قد تتحول إلى أكثر من 5TB إذا استخرجنا كل الصور والصفحات.

لذلك:

- لا نرندر كل صفحة كصورة إلا عند الحاجة.
- لا نحفظ base64 داخل JSON كبير إلا إذا كان ضرورياً.
- نحفظ الصور كملفات، ونربطها بمسارات.
- نستخدم JSONL أو Parquet للبيانات الضخمة.
- نحفظ metadata منفصلة عن النصوص الكبيرة.

## privacy والتكلفة

إذا استخدمنا Mistral OCR API، يجب أن نسأل:

- هل الملفات يمكن إرسالها إلى API خارجي؟
- هل يوجد مواد خاصة أو حساسة؟
- هل التكلفة مقبولة؟
- هل نستخدم batch discount؟
- هل نرسل كل شيء أم الملفات الصعبة فقط؟

القرار المبدئي:

- Docling محلياً لكل شيء ممكن.
- Mistral OCR للعينات الصعبة أو الملفات عالية القيمة.
- عدم إرسال ملفات حساسة إلا بعد قرار واضح.

## خطة مراحل مقترحة

### المرحلة A: خريطة الملفات

الهدف: معرفة ما لدينا.

المخرجات:

- `files.jsonl`
- `files.parquet`
- إحصائيات حسب النوع والحجم والمجلد.
- قائمة التكرارات الدقيقة.
- قائمة الملفات التالفة.

### المرحلة B: عينة اختبار

نختار عينة صغيرة لكنها ممثلة:

- 10 PDFs نصية.
- 10 PDFs scanned.
- 10 صور عربية.
- 10 صور مختلطة عربي/إنجليزي.
- 5 PowerPoints.
- 5 Word.
- 3 فيديوهات.
- ملفات من كل مادة مهمة.

### المرحلة C: Benchmark أدوات

نقارن:

- Docling standard.
- Docling OCR local.
- Mistral OCR.
- ربما أدوات أخرى لاحقاً.

نكتب تقرير:

- أين نجح كل مسار؟
- أين فشل؟
- ما تكلفة Mistral؟
- ما زمن Docling؟
- ما جودة العربية؟
- ما جودة الجداول؟

### المرحلة D: بناء schema وnormalizer

نثبت شكل المخرجات:

- file metadata.
- page metadata.
- element metadata.
- chunks.
- image metadata.
- table metadata.
- transcript metadata.

### المرحلة E: معالجة batch أولى

نبدأ بمادة واحدة فقط، مثلاً Microwave.

لا نعالج كل المواد. نثبت النظام على مادة واحدة.

### المرحلة F: RAG صغير

نبني RAG على مادة واحدة.

نختبر:

- أسئلة مباشرة.
- أسئلة تحتاج جدول.
- أسئلة تحتاج صورة.
- أسئلة تحتاج معادلة.
- أسئلة عربية وإنجليزية.

### المرحلة G: GraphRAG أولي

نستخرج concepts وrelationships لمادة واحدة.

نرى هل العلاقات مفيدة أم ضجيج.

### المرحلة H: التوسع

بعد نجاح مادة واحدة، نوسع إلى مواد أخرى.

## قرار عملي لهذه الحالة

المسار الأكثر واقعية:

1. لا نبدأ بـ training.
2. لا نبدأ بـ GraphRAG.
3. لا نبدأ بمعالجة 5TB دفعة واحدة.
4. نبدأ بـ inventory وdeduplication.
5. نختار عينة ممثلة.
6. نختبر Docling ومسترال OCR.
7. نبني schema موحد.
8. نعالج مادة واحدة.
9. نبني RAG صغير.
10. بعد ذلك نقرر التوسع.

## لماذا لا نبدأ بالتدريب؟

لأن التدريب على بيانات غير منظمة وضعيفة قد ينتج نموذجاً يتعلم الفوضى.

قبل التدريب يجب أن نمتلك:

- corpus نظيف.
- مصادر موثقة.
- جودة OCR مقبولة.
- إزالة تكرار.
- تقسيم حسب مواضيع.
- labels أو تعليمات واضحة.

RAG وGraphRAG أفضل كبداية لأنهما يسمحان باستخدام البيانات مع traceability.

## الأسئلة التي يجب حسمها

- ما المواد الأساسية أولاً؟
- هل نبدأ بـ Microwave كمادة تجريبية؟
- هل الملفات حساسة أم يمكن إرسال بعضها إلى Mistral OCR؟
- هل نريد Obsidian كمخزن قراءة أم فقط كمكان ملاحظات؟
- أين سنخزن 5TB والمخرجات؟
- هل نريد قاعدة بيانات محلية؟
- هل نريد vector DB مثل Qdrant أو Chroma أو Milvus؟
- هل نريد graph DB مثل Neo4j؟
- هل نريد تشغيل مستمر أم batches؟
- هل نحتاج واجهة مراجعة بشرية؟
- هل الأولوية للغة العربية أم الجداول أم الصور؟

## تصور النظام النهائي

```text
Raw data lake 5TB+
    |
    v
Inventory + hashing + file manifest
    |
    v
Deduplication + file type detection
    |
    v
Sampling + quality benchmark
    |
    v
Document router
    |
    +--> Docling local
    |       +--> DoclingDocument
    |       +--> Markdown / JSON / tables / images
    |
    +--> Mistral OCR API
    |       +--> OCR markdown / JSON / images / tables
    |
    +--> Video pipeline
    |       +--> ASR transcript / keyframes / OCR
    |
    v
Normalizer
    |
    +--> normalized metadata
    +--> normalized elements
    +--> normalized chunks
    +--> extracted assets
    |
    v
Indexes
    |
    +--> lexical search
    +--> vector search
    +--> graph index
    |
    v
Applications
    |
    +--> RAG
    +--> GraphRAG
    +--> AI Agents
    +--> lesson generation
    +--> dataset curation
```

## ملف المعرفة المنظم

المخرج النهائي ليس ملف Markdown واحداً. المخرج النهائي منظومة.

لكن يمكن أن يكون لكل مادة ملف MOC في Obsidian:

```markdown
# Microwave MOC

## Topics

- [[Transmission Lines]]
- [[Smith Chart]]
- [[Waveguides]]
- [[S-Parameters]]

## Key Documents

- [[Microwave Lecture 01]]
- [[Microwave Lab Notes]]

## Extracted Figures

- [[Smith Chart Figure]]
- [[Waveguide Diagram]]

## Tables

- [[S-Parameter Measurement Table]]

## Questions

- ما الملفات التي تحتاج مراجعة؟
- ما المواضيع غير المغطاة؟
```

Obsidian هنا ليس قاعدة البيانات الرئيسية، لكنه واجهة تفكير ممتازة.

## الخلاصة

هذه الحالة تحتاج نظاماً، لا أداة واحدة.

Docling مهم جداً لأنه يعطي أساساً محلياً ومفتوح المصدر لتحويل المستندات إلى بنية قابلة للاستخدام. Mistral OCR مهم كمسار قوي للملفات الصعبة، خصوصاً العربية والممسوحة والجداول والـ handwriting. لكن القيمة الحقيقية ستكون في الطبقة التي نبنيها حولهما:

- manifest.
- metadata.
- routing.
- normalization.
- QA.
- chunking.
- indexing.
- graph relationships.

أفضل خطوة تالية ليست معالجة كل شيء. أفضل خطوة تالية هي بناء تجربة صغيرة على عينة ممثلة من 30 إلى 50 ملفاً، ثم قياس الجودة. بعد ذلك نثبت schema ونبدأ بمادة واحدة كاملة، ثم نوسع.

قاعدة العمل:

> كل معلومة مستخرجة يجب أن تعرف مصدرها، صفحتها أو زمنها، أداة استخراجها، درجة الثقة، وعلاقتها بالموضوع.

