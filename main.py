import streamlit as st 
from scrape import scrape_website,extract_body_content,clean_body_content,split_dom_content
from parse import parse_with_ollama
import time
# phân chia trang
st.set_page_config(
    page_title="WebScraping AI",
    page_icon="🔍",
)
st.sidebar.success("Select page extend")

# header 
st.title("🔍 Web Scraping")
url = st.text_input("Enter a Website URL : ")


if st.button("Scrape Site"):
    
    # khi ấn sẽ tự động tạo thanh tải 
    progess_bar = st.progress(0, text="Scraping the webstie...")
    for i in range(1,11):
        time.sleep(0.5)
        progess_bar.progress(i/10,text=f"Scraping the webstie...{i*10}%")
    
    # thu thập html từ website
    result = scrape_website(url)
    
    # chỉ lấy body trong html
    body_content = extract_body_content(result)
    for i in range(1,11):
        time.sleep(0.5)
        progess_bar.progress(i/10,text=f"Extracting content... {10 * i}%")

    # dọn sạch body loại bỏ script, style
    progess_bar.progress(1.0, text="Extraction complete!")
    cleaned_content = clean_body_content(body_content)
        
    st.session_state.dom_content = cleaned_content
    with st.expander("View DOM Content"):
        st.text_area("DOM content",cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_descript = st.text_area("Description what you want to parse?")
    if st.button("Parse Content"):
        if parse_descript:
            st.write("Parsing the content")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_descript)
            st.write(result)