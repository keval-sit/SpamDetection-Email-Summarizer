import pandas as pd
import streamlit as st
import google.generativeai as genai

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

GEMINI_API_KEY = "YOUR_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config(
    page_title="Spam Detection & Email Summarizer",
    page_icon="📧",
    layout="centered"
)

data = pd.read_csv("spam.csv", encoding="latin-1")

data = data[['v1', 'v2']]
data.columns = ['label', 'message']
data['label'] = data['label'].map({
    'ham': 0,
    'spam': 1
})

X = data['message']
y = data['label']

vectorizer = TfidfVectorizer(
    stop_words='english'
)

X_tfidf = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
st.title("📧 Spam Detection & Email Summarizer")

st.markdown("---")

st.success(
    f"Model Accuracy: {accuracy*100:.2f}%"
)

email_text = st.text_area(
    "Enter Email / Message",
    height=200
)

if st.button("Analyze Message"):

    if email_text.strip() == "":
        st.warning("Please enter a message.")
        st.stop()

    transformed = vectorizer.transform(
        [email_text]
    )

    prediction = model.predict(
        transformed
    )[0]

    probability = model.predict_proba(
        transformed
    )[0]

    spam_probability = probability[1] * 100

    st.markdown("---")

    if prediction == 1:

        st.error(
            f"⚠️ SPAM DETECTED\n\nSpam Probability: {spam_probability:.2f}%"
        )

    else:

        st.success(
            f"✅ Legitimate Message\n\nSpam Probability: {spam_probability:.2f}%"
        )

        st.subheader("📄 AI Generated Summary")

        prompt = f"""
        Summarize the following email/message
        in 3 concise bullet points.

        Message:
        {email_text}
        """

        model_gemini = genai.GenerativeModel(
            "gemini-2.0-flash"
        )

        response = model_gemini.generate_content(
            prompt
        )

        st.write(response.text)

        st.markdown("---")

        st.info(
            "Summary generated using Gemini AI."
        )