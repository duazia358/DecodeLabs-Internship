
# DecodeLabs AI & Data Science Internship Portfolio

Welcome to my project repository for the DecodeLabs Internship! This repository contains all four completed engineering tasks, showcasing end-to-end applications across natural language processing, automated classification, machine learning recommendation systems, and computer vision / OCR.

---

## 🛠️ Project Portfolio Overview

| Project | Scope & Domain | Main File / Path | Key Technologies |
| :--- | :--- | :--- | :--- |
| **Project 1** | Rule-Based AI Chatbot | [`chatbot.py`](./chatbot.py) | Python, Tkinter, Regex |
| **Project 2** | Data Classification | [`Project_2_Data_Classification.ipynb`](./Project_2_Data_Classification.ipynb) | Python, Pandas, Scikit-Learn |
| **Project 3** | AI Recommendation Engine | [`Project_3_AI_Recommendation_Engine.ipynb`](./Project_3_AI_Recommendation_Engine.ipynb) | TF-IDF Vectorizer, Cosine Similarity |
| **Project 4** | OCR & Image Text Recognition | [`Project_4_Image_Text_Recognition.ipynb`](./notebooks/Project_4_Image_Text_Recognition.ipynb) | OpenCV, PyTesseract, Gaussian Blur |

---

## 📂 Detailed Project Breakdown

### Project 1: Rule-Based AI Chatbot
- **Goal:** Built a desktop GUI chatbot for automated entity extraction and structured conversation logging.
- **Implementation:** Custom Python Tkinter interface powered by regular expressions (`re`) for pattern-matching and input handling.
- **File Link:** [`chatbot.py`](./chatbot.py)

### Project 2: Data Classification
- **Goal:** Trained and evaluated an end-to-end data classification pipeline adhering to structured evaluation criteria.
- **Implementation:** Data cleaning, feature scaling, model training, and performance evaluation metrics.
- **File Link:** [`Project_2_Data_Classification.ipynb`](./Project_2_Data_Classification.ipynb)

### Project 3: AI Recommendation Engine
- **Goal:** Built a vector space similarity engine mapping skill sets to target technical roles.
- **Implementation:**
  - **Vectorization:** `TfidfVectorizer` to map text feature spaces into high-dimensional numerical arrays.
  - **Similarity Math:** `cosine_similarity` angular orientation scoring to rank top matches.
  - **Cold Start Handling:** Configured input validation to trigger popular role fallback suggestions whenever fewer than 3 skills are provided.
- **File Link:** [`Project_3_AI_Recommendation_Engine.ipynb`](./Project_3_AI_Recommendation_Engine.ipynb)

### Project 4: Image & Text Recognition (OCR)
- **Goal:** Computer vision pipeline to extract text from image documents with dynamic confidence filtering.
- **Implementation:**
  - **Pre-Processing:** Grayscale conversion, $5\times5$ Gaussian Blur filtering, and Otsu's Binarization.
  - **Extraction Engine:** PyTesseract OCR utilizing `--psm 3` automatic page layout analysis.
  - **Confidence Gate:** Applied strict $80\%$ thresholding (`conf >= 0.80`) to filter out low-confidence detections and draw bounding boxes.
- **File Link:** [`notebooks/Project_4_Image_Text_Recognition.ipynb`](./notebooks/Project_4_Image_Text_Recognition.ipynb)

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/duazia358/DecodeLabs-Internship.git](https://github.com/duazia358/DecodeLabs-Internship.git)
   cd DecodeLabs-Internship

## ✍️ Author
**Dua Zia**  
*BS Artificial Intelligence Candidate | Emerson University Multan*  
*Intern at Decode Labs*
