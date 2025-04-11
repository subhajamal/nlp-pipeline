# NLP Pipeline for Extracting Social Determinants of Health (SDOH)

This project implements a complete Natural Language Processing pipeline to identify **Social Determinants of Health (SDOH)** from clinical notes. It includes automated **de-identification**, **NER-based entity extraction**, **BIO-tag formatting**, and **fine-tuning of BioBERT** for named entity recognition (NER).

> Ideal for researchers working with clinical text and looking to extract sensitive non-medical context (e.g. housing, employment, transportation, relationships).

---

## Pipeline Overview

| Step | Description |
|------|-------------|
| 🧽 **De-identification** | Uses NLM Scrubber to remove PHI |
| 🧹 **Text Preprocessing** | Cleans metadata, formatting, and artifacts |
| 🧠 **Entity Extraction** | Extracts SDOH phrases using BioLinkBERT |
| 🧾 **BIO Tagging** | Converts extracted phrases into BIO format |
| 📊 **Model Training** | Fine-tunes BioBERT on BIO-tagged data |
| 🚀 **Inference** | Applies model to new notes for SDOH prediction |

---

## 🗂️ Folder Structure

nlp-pipeline/ ├── data/ │ ├── sdoh_aria_results.csv │ ├── sdoh_bio_dataset_corrected.csv │ └── keywords_nli_train.json ├── notebooks/ │ ├── PIPELINE_NER.ipynb │ ├── sdoh_aria_outputs.ipynb │ └── biobert_ner_trained(small).ipynb ├── scripts/ │ ├── pipeline_polished.py │ └── bio_convert_sentence_id.py ├── biobert_ner_trained/ │ └── [Trained BioBERT model files] ├── Cleaned_Notes.zip ├── Overview.md ├── MASTER_NOTEBOOK_STRUCTURE.md ├── requirements.txt └── README.md


---

## 📦 Dependencies

Install required packages:

```bash
pip install -r requirements.txt

Sample Output
sdoh_aria_results.csv → Extracted phrases like lives alone, no job, rides metro

sdoh_bio_dataset_corrected.csv → BIO tags for training (e.g. B-Housing, I-Housing)

biobert_ner_trained/ → Fine-tuned model weights


🧠 Model Used
BioLinkBERT

BioBERT

Feel free to reach out or raise an issue! 
Developed by Subha Jamal

