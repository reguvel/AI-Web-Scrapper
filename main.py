import streamlit as st

st.title("AI Web Scrapper")
url=st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    st.write("Scrapping the website")

