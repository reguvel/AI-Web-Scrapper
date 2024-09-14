import streamlit as st# This is used for frontend
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content# importing the needed funcs from scrape
#from parse import parse_with_ollama

st.title("AI Web Scraper")# The Title of the Project
url = st.text_input("Enter a website URL: ")#This will take the input of Website and save the string in url

if st.button("Scrape Site"): #A button with "Text: Scrape Site", when clicked the below will execute
    st.write("Scraping...")
    
    result = scrape_website(url)#The Website Content will be saved in result(string)
    body_content = extract_body_content(result)# The Content is given to extract the Body Content using Soap
    cleaned_content = clean_body_content(body_content)# the Body get cleaned

    st.session_state.dom_content = cleaned_content# store the cleaned content in session for stramlit


    with st.expander("View DOM Content: "):# to view more content
        st.text_area("DOM Content", cleaned_content, height = 300)

    
# if "dom_content" in st.session_state: 
#     parse_desc = st.text_area("Describe what you want to parse: ")

#     if st.button("Parse Content"):
#         if parse_desc:
#             st.write("Parsing the Content")

#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             result = parse_with_ollama(dom_chunks, parse_desc)
#             st.write(result)