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