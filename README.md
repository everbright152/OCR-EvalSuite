# PolyOCR-Bench

PolyOCR-Bench is a multilingual OCR benchmarking and evaluation framework designed to compare traditional OCR engines and transformer-based document recognition models across different languages, scripts, image qualities, and document conditions.

The goal of this project is to support OCR/HTR cascade tuning for real-world document intelligence pipelines. Given a dataset of document images and ground-truth text, PolyOCR-Bench evaluates multiple OCR engines, measures accuracy and performance, tests robustness under degraded document conditions, and exports unified reports for model comparison.

This framework is especially useful for teams building document-AI systems where OCR quality directly affects downstream search, retrieval, citations, structured extraction, and knowledge infrastructure.

## Project Purpose

Real-world OCR is rarely solved by a single model. Different engines perform better depending on language, script, handwriting quality, scan resolution, noise, layout, and document type.

PolyOCR-Bench helps answer questions such as:

Which OCR engine performs best for a specific language or script?
Which model is most robust under noisy, blurred, rotated, or compressed images?
Which OCR engine offers the best accuracy vs. speed tradeoff?
How much does performance degrade under real-world document corruption?
Which OCR engine should be used as the first step, fallback, or specialty model in an OCR/HTR cascade?

---

## Supported Engines

**Traditional OCR:**
- Tesseract OCR
- EasyOCR

**Deep Learning / Transformer OCR:**
- TrOCR (Microsoft)
- Donut (Naver CLOVA)
- DocTR (Mindee)
- Nougat (Meta)

---

## What This Does

Given a dataset of images and ground truth text, the framework:

- Runs multiple selected OCR engines dynamically (lazy-loading).
- Computes comprehensive **Text Accuracy** metrics (CER, WER, Exact Match, Levenshtein Distance, Token Accuracy).
- Computes **Semantic Similarity** metrics (BLEU, ROUGE).
- Evaluates **Performance** (Inference Time per image, Memory RSS usage).
- Evaluates **Robustness** under synthetic image corruptions (Gaussian noise, Blur, Rotation, Compression, Low resolution).
- Exports results as comprehensive CSV and JSON reports.
- Generates automatic comparison plots (e.g., Accuracy vs. Speed, Robustness degradation curves, Metric comparisons).

---

## Evaluation Metrics

**Text Accuracy Metrics**
- Character Error Rate, CER
- Word Error Rate, WER
- Exact Match Accuracy
- Levenshtein Distance
- Token Accuracy
**Semantic Similarity Metrics**
- BLEU Score
- ROUGE Score
**Performance Metrics**
- Inference time per image
- Average processing time per engine
- Memory RSS usage
- Accuracy vs. speed comparison
**Robustness Metrics**

The framework can test OCR engines under synthetic document degradations including:

- Gaussian noise
- Blur
- Rotation
- JPEG compression
- Low-resolution scaling

These robustness tests are useful for simulating messy real-world material such as scanned archives, damaged documents, low-quality images, and historical records.

## Key Features
- Multilingual OCR benchmarking across languages and scripts
- Support for traditional and transformer-based OCR engines
- Modular engine interface for easy extension
- Accuracy, semantic, speed, and memory evaluation
- Robustness testing under degraded image conditions
- Unified CSV and JSON benchmark outputs
- Automatic visualization of model performance
- Useful foundation for OCR/HTR cascade tuning
- Designed for document-AI and ingestion pipeline workflows

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

*Note: Tesseract must be installed separately and available in your system PATH.*

---

## Usage

Run a standard benchmark with default engines (all engines):

```bash
python cli.py --dataset datasets/eng --lang eng
```

Specify exactly which engines to evaluate:

```bash
python cli.py --dataset tmp_dataset --engines easyocr,trocr,doctr
```

Enable **Robustness Evaluation** (tests engines under corrupted conditions):

```bash
python cli.py --dataset tmp_dataset --engines easyocr --corrupt
```

### Outputs

Results are saved in:
`results/reports/` (Contains `benchmark.csv` and `benchmark.json`)

Visualization plots are saved in:
`results/plots/` (Contains metric comparions, Speed vs Accuracy charts, and Robustness degradation graphs).

---

## Datasets

This project is designed to work with multilingual OCR datasets. Some publicly available datasets you can use include:

**English**
- ICDAR 2013 / ICDAR 2015 Scene Text datasets  
- IIIT5K Word Dataset

**Chinese**
- RCTW-17 (Reading Chinese Text in the Wild)

**Arabic**
- ALIF Arabic Scene Text Dataset

**Hindi / Devanagari**
- IIIT-HW Devnagari Handwritten Dataset

**Multilingual**
- MLT (ICDAR Multi-Lingual Text Dataset)

These datasets contain labeled text images that can be used as input for benchmarking OCR engines.

Dataset folders should follow this structure:

datasets/<lang>/
    images/
    ground_truth/

Each image should have a corresponding `.txt` file with the same name containing the ground truth text.

---

## Project Focus

- Modular OCR engine interface
- Integration of state-of-the-art transformer models (TrOCR, Donut, Nougat, DocTR) alongside traditional systems
- Deep evaluation pipeline covering exact extraction, semantics, time, and memory constraints
- Automated result reporting and graphical visualization
