
import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    # Get the compound score, which represents the overall sentiment
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    nltk.download('vader_lexicon')
    st.title("NLP Tool: Sentiment Analysis")

    user_text = st.text_area("Enter text:", "")

    if st.button("Analyze"):
        if user_text.strip() != "":
            result = sentiment_analysis(user_text)
            st.write("Sentiment:", result)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
