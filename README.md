# DecodeLabs AI & Data Science Internship Portfolio

Welcome to my project repository for the DecodeLabs Internship! This repository contains all my completed engineering tasks, showcasing end-to-end applications across NLP, workflow automation, machine learning recommendations, and computer vision / OCR.

---

## 🛠️ Project Portfolio Overview

| Project | Scope & Domain | Key Technologies | Location |
| :--- | :--- | :--- | :--- |
| **Project 1** | Rule-Based AI Chatbot | Python, Tkinter, Regex | [`/Project_1_Rule_Based_Chatbot`](./Project_1_Rule_Based_Chatbot) |
| **Project 2** | Automated Workflow | n8n, Webhooks, Gemini API | [`/Project_2_Automation_Workflow`](./Project_2_Automation_Workflow) |
| **Project 3** | Skill Recommendation System | Scikit-Learn, TF-IDF, Cosine Similarity | [`/Project_3_ML_Model`](./Project_3_ML_Model) |
| **Project 4** | OCR & Image Text Recognition | OpenCV, PyTesseract, Gaussian Blur | [`/notebooks`](./notebooks/Project_4_Image_Text_Recognition.ipynb) |

---

## 📂 Detailed Breakdown

### Project 1: Rule-Based AI Chatbot
- **Goal:** Developed a desktop GUI chatbot for automated entity extraction and structured conversation logging.
- **Tech Stack:** Python, Tkinter, Regular Expressions (`re`).

### Project 2: Dynamic Lead Automation Workflow
- **Goal:** Built an automated lead notification pipeline triggering email alerts upon web form submissions.
- **Tech Stack:** n8n, Webhooks, Gemini API.

### Project 3: Technical Role Recommendation System
- **Goal:** Built a vector space similarity engine mapping skill sets to relevant tech roles.
- **Implementation:**
  - **Vectorization:** `TfidfVectorizer` to project text feature spaces.
  - **Similarity Math:** `cosine_similarity` angular orientation scoring.
  - **Cold Start Handling:** Dynamic fallback suggestions when fewer than 3 skills are supplied.

### Project 4: Image & Text Recognition (OCR)
- **Goal:** Computer vision pipeline to extract text from images with automated quality filtering.
- **Implementation:**
  - **Pre-Processing:** Grayscale conversion, $5\times5$ Gaussian Blur, and Otsu's Binarization.
  - **Extraction:** PyTesseract OCR with `--psm 3` layout analysis.
  - **Confidence Gate:** Applied strict $80\%$ thresholding (`conf >= 0.80`) to filter out false detections and render bounding boxes.
- **Notebook File:** [`Project_4_Image_Text_Recognition.ipynb`](./notebooks/Project_4_Image_Text_Recognition.ipynb)

---

## ✍️ Author
**Dua Zia**  
*BS Artificial Intelligence Candidate | Emerson University Multan*  
*Intern at Decode Labs*
