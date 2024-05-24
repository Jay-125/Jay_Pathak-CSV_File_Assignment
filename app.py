import streamlit as st 
from pandasai.llm.local_llm import LocalLLM
from pandasai import SmartDataframe
import pandas as pd
# from pandasai import PandasAI

model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)

st.set_page_config(layout='wide')

st.title("ChatCSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:

        col1, col2 = st.columns([1,1])

        with col1:
            st.info("CSV Uploaded Successfully")
            data = pd.read_csv(input_csv)
            st.dataframe(data, use_container_width=True)

        with col2:

            st.info("Chat Below")
            
            input_text = st.text_area("Enter your query")

            df = SmartDataframe(data, config={"llm": model})

            if input_text is not None:
                if st.button("Chat with CSV"):
                    with st.spinner("Generating response..."):
                        st.info("Your Query: "+input_text)
                        result = df.chat(input_text)
                        st.success(result)
