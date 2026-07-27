<div align="center">

# 🍿 Cinematic Matchmaker
**An End-to-End Content-Based Machine Learning Recommendation Engine**

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B.svg?style=for-the-badge&logo=streamlit)](https://movie-recommender-system-zzddpnc2fjnhy9fhasmu39.streamlit.app/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E.svg?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg?style=for-the-badge&logo=fastapi)](https://www.python.org/)

*Transforming raw cinematic metadata into highly accurate, personalized user recommendations.*

[**Launch Live Application**](https://movie-recommender-system-zzddpnc2fjnhy9fhasmu39.streamlit.app/) • [**Report Bug**](https://github.com/manojmulammagari/Movie-Recommender-System/issues) • [**Request Feature**](https://github.com/manojmulammagari/Movie-Recommender-System/issues)

</div>

---

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [System Architecture](#-system-architecture)
- [Technical Implementation](#-technical-implementation)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [Local Installation](#-local-installation)
- [Future Roadmap](#-future-roadmap)

---

## 📌 Project Overview
**Cinematic Matchmaker** is a production-grade recommendation system designed to solve the "what to watch next" problem. By leveraging Natural Language Processing (NLP) on over 5,000 cinematic records, the engine analyzes deep metadata—including genres, cast, crew, keywords, and plot overviews—to compute relational similarities between films.

This project was built to demonstrate a complete **Machine Learning Lifecycle**: from raw data ingestion and exploratory data analysis (EDA) in a Jupyter environment, to model serialization, and finally, cloud deployment via a low-latency Streamlit web interface.

---

## ⚙️ System Architecture

The recommendation pipeline follows a strict, modular data flow:

1. **Data Ingestion:** Merging the TMDB 5000 Movies and Credits datasets.
2. **Feature Engineering:** Extracting relevant tags (Director, Top 3 Cast, Genres, Keywords).
3. **Text Preprocessing:** Tokenization, lowercasing, and stemming (via `nltk.PorterStemmer`).
4. **Vectorization:** Transforming the textual corpus into a 5000-dimensional numeric space using `CountVectorizer` / `TfidfVectorizer`.
5. **Distance Computation:** Calculating the **Cosine Similarity** matrix to find the nearest neighbors in the multidimensional space.
6. **Deployment:** Serializing the matrix via `pickle` and serving it through a Streamlit UI (with a modular FastAPI backend available).

---

## 🧠 Technical Implementation

### The Mathematics of Matching
Instead of relying on user ratings (Collaborative Filtering), this engine uses **Content-Based Filtering**. 
Each movie is represented as a vector in an $N$-dimensional space. The similarity between two movies, $A$ and $B$, is calculated using the Cosine Similarity formula:

$$\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\Vert{}\mathbf{A}\Vert{} \Vert{}\mathbf{B}\Vert{}}$$

*   **Result:** A similarity score between 0 and 1, where 1 indicates identical content tags.

### Memory Optimization for Cloud
A full 4800x4800 float64 matrix consumes significant memory, causing standard cloud deployments to crash. This project implements **matrix downcasting to `float16`**, reducing the memory footprint by 75% without sacrificing recommendation accuracy, ensuring stable, free-tier cloud hosting.

---

## 🛠️ Tech Stack

| Category | Technologies Used |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Data Engineering** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn (Vectorization, Similarity), NLTK (Stemming) |
| **Model Serialization**| Pickle |
| **Frontend UI** | Streamlit |
| **Backend API** | FastAPI, Uvicorn, Pydantic |

---

## 📂 Repository Structure

```text
📦 Movie-Recommender-System
 ┣ 📜 Movie_Recommender_System_Project.ipynb  # Core ML notebook (Data Prep & Training)
 ┣ 📜 app.py                                  # FastAPI backend serving script
 ┣ 📜 ui.py                                   # Streamlit frontend deployment script
 ┣ 📜 requirements.txt                        # Cloud deployment dependencies
 ┣ 📜 tmdb_5000_credits.csv.zip               # Raw dataset 1
 ┣ 📜 tmdb_5000_movies.csv.zip                # Raw dataset 2
 ┗ 📜 README.md                               # Project documentation


## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/manojmulammagari/Movie-Recommender-System.git](https://github.com/manojmulammagari/Movie-Recommender-System.git)
   cd Movie-Recommender-System
