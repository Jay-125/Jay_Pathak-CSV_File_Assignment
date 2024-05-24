from langchain_experimental.agents import create_csv_agent
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents import AgentExecutor
# from langchain_community.tools import WikipediaQueryRun
# from langchain.llms import OpenAI
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
import io
import streamlit as st
import pandas as pd


llm = Ollama(temperature=0.0, model="llama3")

def create_agent(data: str, llm):
    """Create a Pandas DataFrame agent."""
    return create_pandas_dataframe_agent(llm, data, verbose=True, 
                                         agent_executor_kwargs={"handle_parsing_errors": True})



def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    # if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
    #     print("OPENAI_API_KEY is not set")
    #     exit(1)
    # else:
    #     print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:

        # agent = create_csv_agent(
        #     llm, csv_file, verbose=True)

        df = pd.read_csv(csv_file)
        agent = create_agent(df, llm)

        user_question = st.text_input("Ask a question about your CSV: ")

        prompt = """You are professional data scientist who is proficient in reading and manipulating 
        csv data. Now, you have recieved a pandas dataframe that contains the information about
        indian population.
        
        This dataset contains the data about population in India from 1950 to 2022. 
        The dataset contain different factors affecting the population like birth rate, death rate, 
        fertility rate, migration rate etc. and the percentage increase or decrease in it. 

        You recently got a job to assist a user by answering questions asked by the user about the
        dataset.
        
        Now, your task is to analyze and read the data in efficient way and answer the below
        question based on the dataset asked by user to assist the user
        
        Question:"""


        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                prompt = prompt + user_question
                response = agent.invoke(prompt)
                st.write(response)




if __name__ == "__main__":
    main()
