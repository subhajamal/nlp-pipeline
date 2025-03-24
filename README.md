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


---

---

### ✅ **Step 3: Push to GitHub**
1. Go to your `nlp-pipeline/` folder.
2. Run the following Git commands:

```bash
git init
git remote add origin https://github.com/subhajamal/nlp-pipeline.git
git add .
git commit -m "Upload full NLP SDOH extraction pipeline"
git push -u origin main
