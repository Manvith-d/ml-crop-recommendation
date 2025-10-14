# 🌾 ML Crop Recommendation System

A Flask web app that recommends the best crop to grow based on soil & weather inputs using ML.

## ✨ What it does
- Takes N, P, K, pH, temperature, humidity, rainfall as inputs
- Loads a trained model (`model.pkl`)
- Predicts the recommended crop

## Models tried
Logistic Regression, Decision Tree, Random Forest ✅ (best), XGBoost.

## 💻 Tech
Python (Flask, scikit-learn, pandas, numpy), HTML/CSS.

## ▶️ Run locally
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py

## 📄 Publication

- **Paper:** [Crop Recommendation using ML](docs/crop_recommendation_paper.pdf)
- **Certificate:** [Publication Certificate](docs/crop_recommendation_certificate.pdf)
