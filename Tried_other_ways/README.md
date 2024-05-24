# Introduction

Here, I have tried other ways to approach the problem. 

## How application works ?

The application reads the CSV file and processes the data. It utilizes ollama LLMs alongside with Langchain Agents in order to answer your questions. The CSV agent then uses tools to find solutions to your questions and generates an appropriate response with the help of a LLM.

In this case, I have tried both streamlit and chainlit for the APP UI.

## Installation

To install the repository, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

  ### Installing ollama

  1. Click on link https://ollama.com/download/linux to navigate to ollama official website.
  2. Choose your OS and download ollama. For example, I am using Linux, so I will be firing command

  '''
  curl -fsSL https://ollama.com/install.sh | sh
  '''

  3. Now, open terminal in linux and fire below command to pull llama3 model, so that we can run the model localy.

  '''
  ollama pull llama3
  '''

## Usage

To use the application, execute the any .py file using the Streamlit/Chainlit CLI.  Run the following command in your terminal based on the file:

```
streamlit run <filename>
```

OR

```
chainlit run <filename>
```

Here are some screenshots that demonstrates the chat.

[query_1](./pictures/pic_1.png)

[query_2](./pictures/pic_2-1.png)

[query_2_result](./pictures/pic_2-2.png)


## Observation

Using ollama llama3, I am able to answer basic questions about csv. But, when it comes to more complex questions, the agent took some time and the results are not consistent. Sometimes, the agent will return correct output, sometimes not.