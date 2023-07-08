import streamlit as st
import requests

def download_afinn():
    url = "https://raw.githubusercontent.com/fnielsen/afinn/master/afinn/data/AFINN-111.txt"
    response = requests.get(url)
    afinn_data = response.text
    afinn = dict()
    for line in afinn_data.split("\n"):
        word, score = line.split("\t")
        afinn[word] = int(score)
    return afinn

def sentiment_analysis(text, afinn):
    words = text.lower().split()
    sentiment_score = sum(afinn.get(word, 0) for word in words)

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("NLP Tool: Sentiment Analysis")
    afinn = download_afinn()

    user_text = st.text_area("Enter text:", "")

    if st.button("Analyze"):
        if user_text.strip() != "":
            result = sentiment_analysis(user_text, afinn)
            st.write("Sentiment:", result)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()

