# Spam Detection & Email Summarizer

# Project Overview

Spam Detection & Email Summarizer is a Hybrid AI application that combines Machine Learning and Generative AI.

The system first analyzes an email or message and classifies it as **Spam** or **Legitimate** using Natural Language Processing (NLP) techniques. If the message is legitimate, the application uses **Google Gemini AI** to generate a concise summary, helping users quickly understand important information without reading the entire message.

This project demonstrates the integration of traditional Machine Learning models with modern Large Language Models (LLMs).

---

# Features

* Detects Spam and Legitimate Messages
* Displays Spam Probability Score
* Uses TF-IDF for text vectorization
* Uses Logistic Regression for classification
* Generates AI-powered summaries for legitimate messages
* Interactive Streamlit web interface
* Real-time message analysis
* Beginner-friendly NLP and GenAI project

# Tech Stack

# Programming Language

* Python

# Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression

# Generative AI

* Google Gemini API

# Frontend

* Streamlit

# Data Processing

* Pandas

# Dataset

* SMS Spam Collection Dataset

# Workflow

Message Input
↓
TF-IDF Vectorization
↓
Logistic Regression Classifier
↓
Spam / Legitimate Detection
↓
If Legitimate
↓
Google Gemini AI
↓
Summary Generation

# Installation

# Clone Repository

```bash
git clone https://github.com/keval-sit/SpamDetection-Email-Summarizer.git
cd SpamDetection-Email-Summarizer
```

# Install Dependencies

```bash
pip install -r requirements.txt
```

# Add Gemini API Key

Open the Python file and replace:

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

with your Gemini API Key.

# Run Application

```bash
streamlit run app.py
```

# Model Performance

* Classification Algorithm: Logistic Regression
* Text Representation: TF-IDF
* Accuracy: 94.44%

---

# Screenshots

# Spam Detection

(Add spam detection screenshot here)

# Legitimate Message Detection

(Add legitimate message screenshot here)

# AI Generated Summary

(Add summary screenshot here)

---

# Future Improvements

* Email Attachment Analysis
* Multi-language Support
* Advanced Deep Learning Models
* Email Priority Classification
* Dashboard Analytics

# Author

Keval Jatakia

AI/ML Enthusiast | First-Year Engineering Student
