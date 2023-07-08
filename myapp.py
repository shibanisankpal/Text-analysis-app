import streamlit as st

def sentiment_analysis(text):
    positive_keywords = ['good', 'great', 'excellent', 'awesome', 'amazing', 'happy', 'joyful',
                         'pleased', 'satisfied', 'fantastic', 'wonderful', 'love', 'like', 'best',
                         'beautiful', 'fun', 'nice', 'exciting']

    negative_keywords = ['bad', 'terrible', 'poor', 'awful', 'horrible', 'sad', 'disappointed',
                         'frustrated', 'unhappy', 'displeased', 'miserable', 'angry', 'hate',
                         'worst', 'ugly', 'annoying', 'disgusting', 'unpleasant', 'horrid']

    words = text.lower().split()

    positive_count = sum(keyword in words for keyword in positive_keywords)
    negative_count = sum(keyword in words for keyword in negative_keywords)

    if positive_count > negative_count:
        return "Positive"
    elif positive_count < negative_count:
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
