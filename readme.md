# 📧 Email / SMS Spam Classifier

A Machine Learning–based Email/SMS Spam Classifier that predicts whether a given message is **Spam** or **Not Spam**.  
The project uses **TF-IDF vectorization** with a trained ML model and exposes predictions via a **FastAPI backend**, along with a simple frontend UI.

---

## 🚀 Features

- Text preprocessing and vectorization using **TF-IDF**
- Pre-trained ML model loaded using **pickle**
- Input validation using **Pydantic**
- Simple and responsive frontend (HTML + CSS + JS)
- Handles real-world spam patterns (offers, phishing, urgency, scams)
---

## 🧠 Machine Learning Pipeline

1. Text Cleaning (lowercasing, tokenization, filtering)
2. TF-IDF Vectorization
3. Classification using trained Naive Bayes (Mutinomial) model
4. Prediction output: `Spam` or `Not Spam`

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn
- Pandas
- Pydantic
- Uvicorn

### Frontend
- HTML
- CSS (Bootstrap)
- JavaScript (Fetch API)

---



