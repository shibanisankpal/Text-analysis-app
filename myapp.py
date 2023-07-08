import streamlit as st
from transformers import pipeline

def sentiment_analysis(text):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    return result["label"]

def main():
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
