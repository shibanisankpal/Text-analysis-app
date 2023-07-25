# app.py
import streamlit as st
import pandas as pd
import nltk
from textblob import TextBlob
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from PyPDF2 import PdfReader

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

def main():
    st.title("Text Analysis Tool")

    # File upload
    uploaded_file = st.file_uploader("Upload a text file", type=["txt", "pdf"])
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode('utf-8')
        elif uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a text file (txt) or a PDF file (pdf).")
            return

        st.text_area("Uploaded Text", text, height=200)
        analyze_text(text)

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# ... rest of the code remains the same ...


def analyze_text(text):
    # Perform text analysis
    word_count = get_word_count(text)
    sentiment_score = get_sentiment_score(text)
    keywords = get_keywords(text)

    # Display results
    st.subheader("Word Count")
    st.write(word_count)

    st.subheader("Sentiment Analysis")
    st.write(sentiment_score)

    st.subheader("Keywords")
    st.write(keywords)

def get_word_count(text):
    words = nltk.word_tokenize(text)
    word_count = Counter(words)
    return dict(word_count)

def get_sentiment_score(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    return f"Sentiment: {sentiment}, Polarity: {sentiment_score:.2f}"

def get_keywords(text):
    # Extract keywords using TF-IDF
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    tfidf_matrix = tfidf_vectorizer.fit_transform([text])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    keywords = [feature_names[col] for col in tfidf_matrix.nonzero()[1]]

    return keywords

if __name__ == "__main__":
    main()
