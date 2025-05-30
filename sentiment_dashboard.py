# import pandas as pd
# from textblob import TextBlob
# import matplotlib.pyplot as plt
# from collections import Counter

# # Load dataset
# data = pd.read_csv('sample_tweets.csv')

# # Function to analyze sentiment polarity
# def analyze_sentiment(tweet):
#     analysis = TextBlob(tweet)
#     polarity = analysis.sentiment.polarity
#     if polarity > 0:
#         return 'Positive'
#     elif polarity == 0:
#         return 'Neutral'
#     else:
#         return 'Negative'

# # Apply sentiment analysis
# data['sentiment'] = data['tweet'].apply(analyze_sentiment)

# # Count sentiments
# counts = Counter(data['sentiment'])

# # Plot bar chart
# plt.bar(counts.keys(), counts.values(), color=['green', 'grey', 'red'])
# plt.title('Sentiment Distribution')
# plt.xlabel('Sentiment')
# plt.ylabel('Number of Tweets')
# plt.show()

import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

st.set_page_config(page_title="Tweet Sentiment Analyzer", layout="wide")
st.title("📊 Tweet Sentiment & Language Analysis")

uploaded_file = st.file_uploader("📤 Upload CSV File (must have 'tweet' column)", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    if 'tweet' not in data.columns:
        st.error("❌ CSV file must contain a 'tweet' column.")
    else:
        with st.spinner("Analyzing sentiment and language..."):
            def analyze_sentiment(tweet):
                analysis = TextBlob(str(tweet))
                polarity = analysis.sentiment.polarity
                if polarity > 0:
                    return 'Positive'
                elif polarity == 0:
                    return 'Neutral'
                else:
                    return 'Negative'

            def detect_language(tweet):
                try:
                    return detect(str(tweet))
                except LangDetectException:
                    return "Unknown"

            data['Sentiment'] = data['tweet'].apply(analyze_sentiment)
            data['Language'] = data['tweet'].apply(detect_language)
            counts = Counter(data['Sentiment'])

        st.success("✅ Analysis Complete!")

        # Sentiment Bar Chart
        st.subheader("📈 Sentiment Distribution")
        col1, col2 = st.columns(2)
        with col1:
            st.write(counts)

        with col2:
            fig, ax = plt.subplots()
            ax.bar(counts.keys(), counts.values(), color=['green', 'grey', 'red'])
            ax.set_xlabel("Sentiment")
            ax.set_ylabel("Tweet Count")
            ax.set_title("Sentiment Distribution")
            st.pyplot(fig)

        # Language Chart - Final Clean Version
        st.subheader("🌍 Language Distribution")
        lang_counts = data['Language'].value_counts()
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        colors = plt.cm.tab20.colors  # More distinct colors

        # Pie chart without labels to avoid overlap
        wedges, texts = ax2.pie(
            lang_counts.values,
            colors=colors[:len(lang_counts)],
            startangle=140
        )
        ax2.axis('equal')  # Equal aspect ratio

        # Add legend outside
        ax2.legend(
            wedges,
            [f"{lang}: {count} ({count/sum(lang_counts.values)*100:.1f}%)" for lang, count in lang_counts.items()],
            title="Languages",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
            fontsize=8
        )

        st.pyplot(fig2)

        # Tweet Table
        st.subheader("📄 Tweets with Sentiment & Language")
        st.dataframe(data[['tweet', 'Sentiment', 'Language']], use_container_width=True)

        # WordCloud Section
        st.subheader("☁️ Generate WordCloud")
        option = st.selectbox("Choose tweets to visualize:", ["All", "Positive", "Negative", "Neutral"])

        if option == "All":
            text = ' '.join(data['tweet'].dropna().astype(str))
        else:
            text = ' '.join(data[data['Sentiment'] == option]['tweet'].dropna().astype(str))

        if text.strip():
            wc = WordCloud(width=800, height=400, background_color='white').generate(text)
            fig_wc, ax_wc = plt.subplots()
            ax_wc.imshow(wc, interpolation='bilinear')
            ax_wc.axis('off')
            st.pyplot(fig_wc)
        else:
            st.warning(f"No {option} tweets found for WordCloud.")

        # CSV Download
        st.subheader("⬇️ Download Analyzed Data")
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='analyzed_tweets.csv',
            mime='text/csv'
        )

else:
    st.info("👈 Please upload a CSV file to begin.")

    
# note run file : streamlit run sentiment_dashboard.py
