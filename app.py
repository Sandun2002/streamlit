import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Summarization Tool")


@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")


summarizer_modal = load_model()

st.title("Text Summarization Tool")
coll, col2 = st.columns([2, 1])

with coll:
    user_input = st.text_area("Enter text to summarize", height=200)
    summarizer_button = st.button("Summarizer Text", type="primary")

with col2:
    st.markdown("Powered by Sandun Gunathilake")

if summarizer_button and user_input:
    with st.spinner("Summarizing ..."):
        result = summarizer_modal(user_input)
        summary_text = result[0]['summary_text']
        st.markdown(summary_text)

elif summarizer_button:
    st.warning("Please enter text to summarize.")
