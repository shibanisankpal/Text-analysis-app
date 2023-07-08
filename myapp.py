import streamlit as st
import spacy 
from textblob import TextBlob

# Load English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Perform sentiment analysis using TextBlob
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Perform entity recognition using spaCy
def perform_entity_recognition(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Perform keyword extraction using spaCy
def perform_keyword_extraction(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return keywords

# Streamlit app
def main():
    st.title("Text Analytics App")
    
    # User input
    text = st.text_area("Enter your text here")

    if st.button("Analyze"):
        # Sentiment analysis
        polarity, subjectivity = perform_sentiment_analysis(text)
        st.write("Sentiment Analysis:")
        st.write(f"Polarity: {polarity}")
        st.write(f"Subjectivity: {subjectivity}")

        # Entity recognition
        entities = perform_entity_recognition(text)
        st.write("Entity Recognition:")
        for entity, label in entities:
            st.write(f"{entity} ({label})")

        # Keyword extraction
        keywords = perform_keyword_extraction(text)
        st.write("Keywords:")
        for keyword in keywords:
            st.write(keyword)

# Run the app
if __name__ == "__main__":
    main()
