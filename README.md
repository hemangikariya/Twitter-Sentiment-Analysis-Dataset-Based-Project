# Twitter-Sentiment-Analysis-Dataset-Based-Project

# 📊 Tweet Sentiment & Language Analyzer

A simple yet powerful **Streamlit-based web app** that performs **sentiment analysis** and **language detection** on tweets from a CSV file.

---

## 🚀 Features

- 📤 Upload CSV file with tweets
- 😊 Sentiment Analysis (`Positive`, `Neutral`, `Negative`) using TextBlob
- 🌍 Language Detection using `langdetect`
- 📈 Visualizations: Bar Chart (Sentiment), Pie Chart (Language)
- ☁️ Word Cloud generation for all or selected sentiment types
- 📄 View tweets in a structured DataFrame
- ⬇️ Download analyzed results as CSV

---

## 🗂️ Project Structure
├── sentiment_dashboard.py # Main Streamlit app
├── requirements.txt # Dependencies
├── sample_tweets.csv # Sample input file
└── README.md # Project description

---

## 🛠️ Installation

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/tweet-sentiment-analyzer.git
cd tweet-sentiment-analyzer
```bash

🔹 Step 2: Create & Activate Virtual Environment (optional but recommended)
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/Mac
python3 -m venv venv
source venv/bin/activate

