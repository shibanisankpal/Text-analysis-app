import streamlit as st
from textblob import TextBlob

def sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

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
