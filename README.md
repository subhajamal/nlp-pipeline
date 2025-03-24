# 🧠 NLP Pipeline for SDOH Extraction from Clinical Notes

This project implements a full pipeline for extracting Social Determinants of Health (SDOH) from clinical notes using BioLinkBERT + BioBERT. It includes:

- NLM Scrubber de-identification
- Cleaning & preprocessing
- Entity extraction with BioLinkBERT
- BIO tagging format conversion
- BioBERT model fine-tuning
- Final inference on new notes

---

## 📁 Folder Structure

| Folder | Description |
|--------|-------------|
| `notebooks/` | Jupyter Notebooks for EDA, NER, and SDOH |
| `scripts/` | Python scripts for automation |
| `data/` | Intermediate CSVs: extracted SDOH, BIO dataset |
| `biobert_ner_trained/` | Trained NER model outputs |
| `Cleaned_Notes/` | De-identified clinical notes (after Scrubber) |

---

## 🧪 Run the Pipeline
```bash
python scripts/pipeline_polished.py
