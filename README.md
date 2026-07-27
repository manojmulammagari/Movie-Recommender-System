# 🍿 Cinematic Matchmaker: Content-Based Recommendation Engine

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red.svg)](https://movie-recommender-system-zzddpnc2fjnhy9fhasmu39.streamlit.app/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

**Live Application:** [Click here to view the deployed app](https://movie-recommender-system-zzddpnc2fjnhy9fhasmu39.streamlit.app/)

## 📌 Overview
Cinematic Matchmaker is a production-ready, content-based movie recommendation system. It utilizes Natural Language Processing (NLP) to analyze over 4,800 cinematic records and recommends the top 5 most similar movies based on a user's selection. 

This project demonstrates a complete end-to-end machine learning lifecycle, from data wrangling and feature engineering in a Jupyter Notebook to model serialization and cloud deployment via Streamlit.

## 🚀 Key Features
* **Advanced Text Preprocessing:** Engineered a robust NLP pipeline using `nltk.PorterStemmer` to clean, tokenize, and stem multi-dimensional metadata (genres, cast, crew, keywords, overview).
* **Vectorization & Similarity:** Utilized Scikit-Learn's `TfidfVectorizer` to convert text tags into a 5000-dimensional feature space, computing relational distances using **Cosine Similarity**.
* **Memory Optimization:** Reduced the similarity matrix memory footprint by 75% via `float16` downcasting and efficient `.pkl` serialization for cloud constraints.
* **Interactive UI:** Deployed a low-latency frontend using Streamlit Community Cloud.
* **API Backend (Optional):** Includes a `FastAPI` script (`app.py`) demonstrating how to serve the model as a scalable REST API.

## 🛠️ Technology Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn, NLTK
* **Serialization:** Pickle
* **Web Framework / API:** Streamlit, FastAPI, Uvicorn
* **Dataset:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/manojmulammagari/Movie-Recommender-System.git](https://github.com/manojmulammagari/Movie-Recommender-System.git)
   cd Movie-Recommender-System
