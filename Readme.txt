# 🎯 UniRec – Unified Recommendation System

## 🚀 Overview

UniRec is a cross-domain recommendation system that provides personalized suggestions across **movies, books, and restaurants** in a single platform.

Unlike traditional recommenders limited to one domain, UniRec leverages **shared user preferences** to generate intelligent cross-domain recommendations.

---

## ✨ Features

* 🎬 Movie recommendation (MovieLens dataset)
* 📚 Book recommendation (genre-based)
* 🍽️ Restaurant recommendation (cuisine-based)
* 🔗 Cross-domain intelligence (e.g., Sci-Fi movie → Sci-Fi books + themed restaurants)
* ⚡ Fast recommendations using TF-IDF + cosine similarity
* 🌐 Interactive UI built with Streamlit

---

## 🧠 System Architecture

* Content-based filtering using TF-IDF
* Cosine similarity for ranking
* Modular design for multi-domain recommendation
* Extendable to collaborative filtering & deep learning

---

## 📊 Datasets Used

* MovieLens Dataset (movies)
* Custom lightweight datasets for books & restaurants

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/unirec.git
cd unirec
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🌐 Output

* Select a movie
* Get:

  * Similar movies
  * Related books
  * Restaurant suggestions

---

## 🧑‍💻 Author

Anant Kumar Singh

---


