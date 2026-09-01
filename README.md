# Project 2: Data Classification Using AI

## Overview
This project implements a Supervised Learning classification pipeline using the K-Nearest Neighbors (KNN) algorithm on the classic Iris dataset.

## Workflow
1. **Data Loading**: Loaded 150 samples across 3 flower species.
2. **Preprocessing**: Applied `StandardScaler` to normalize feature scales.
3. **Data Splitting**: 80/20 train-test split (`random_state=42`, stratified).
4. **Model Training**: K-Nearest Neighbors (`n_neighbors=5`).
5. **Evaluation**: Evaluated using Confusion Matrix, Accuracy, and F1-Score.

## Results
* **Accuracy**: 93.33%
* **Macro Average F1-Score**: 0.93

## Directory Structure
- `data/`: Dataset details and documentation
- `notebooks/`: Jupyter Notebook containing code execution
- `requirements.txt`: Environment dependencies
- `README.md`: Project overview and results
- ---

## Project 3: AI Recommendation Engine (Content-Based Filtering)

### Overview
Developed a content-based recommendation engine using TF-IDF vectorization and Cosine Similarity to match user technical skills to relevant career paths. The pipeline processes multi-variable inputs and provides real-time match accuracy scores while gracefully handling Cold Start scenarios.

### Technical Implementation
* **Vectorization:** Implemented `TfidfVectorizer` to map text feature spaces into high-dimensional numerical arrays.
* **Similarity Mathematics:** Calculated angular orientation using `cosine_similarity` to rank top 3 matching roles based on vector direction.
* **Cold Start Handling:** Configured input validation to trigger popular role fallback suggestions whenever fewer than 3 skills are provided.

### Key Results
* **Input Test Case:** `['Python', 'Machine Learning', 'Deep Learning']`
* **Top Output Match:** AI/ML Engineer (74.22% Match Score)
* **Secondary Match:** Data Scientist (39.98% Match Score)
