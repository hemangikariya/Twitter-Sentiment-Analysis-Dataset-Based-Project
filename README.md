# Twitter-Sentiment-Analysis-Dataset-Based-Project

# 📊 Twitter-Sentiment-Analysis-Dataset-Based-Project

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
```
### 🔹 Step 2: Create & Activate Virtual Environment (optional but recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### ▶️ Run the App
```bash
streamlit run sentiment_dashboard.py
```

### 📄 Sample Input Format
Your CSV file should have at least one column named tweet:
```bash
tweet
"I love this product!"
"This is terrible."
"I'm feeling okay."
```

### 📦 Dependencies
streamlit
pandas
textblob
matplotlib
wordcloud
langdetect

### ❌ .gitignore (Recommended)
```bash
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.DS_Store
.env
```

### 📝 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Created by Hemangi Kariya

GitHub: www.github.com/hemangikariya

LinkedIn: www.linkedin.com/in/hemangikariya


