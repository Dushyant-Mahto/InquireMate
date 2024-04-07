<div align="center">

# InquireMate

</div>

**InquireMate** is an AI-powered application that utilizes machine learning and web development technologies to provide real-time or static insights based on the RAG (Retrieval-Augmented Generation) approach. It enables users to interact with a knowledge base through natural language queries, with support for both real-time streaming data and static data sources.

<div align="center">
  <img src="https://github.com/TushnikaC/InquireMate/blob/main/llm.gif" alt="InquireMate">
</div>

## Purpose
InquireMate addresses the common pain point faced by students when dealing with extensive text materials, such as research papers, textbooks, and historical documents. We recognize that students often struggle to sift through large volumes of text to find specific information or answers to their questions efficiently. This inefficiency can hinder their academic progress, leading to frustration and wasted time.

Our project seeks to alleviate this challenge by offering a user-friendly platform where students can upload their text files and ask questions related to the content. Leveraging the Realtime Large Language Models (LLMs) available through the LLM App, InquireMate quickly analyzes the uploaded documents and provides accurate and concise answers to the user's queries in real-time.

## Utilizing Realtime LLMs:
InquireMate leverages the Realtime LLMs (Large Language Models) available through the LLM App to generate answers in real-time. When a student uploads a text file and submits a question, the system combines the uploaded content with the user's query and sends it to the LLM for analysis. The LLM processes the input data and generates a coherent response based on the context and the question asked. This real-time interaction enables students to receive immediate answers and insights from their text files, enhancing their learning experience and academic productivity.


## Installation

### Windows Integration (Original Code):

### Prerequisites
To set up and run InquireMate on your local machine, follow these steps:

Requirements:

1. Python 3.10 or above installed on your machine.
2. Pip installed to manage project packages.
3. Docker (optional if you prefer Dockerized deployment).
4. OpenAI account and API key for utilizing OpenAI services.

### Clone the Repository

```bash
git clone https://github.com/yourusername/InquireMate.git
cd InquireMate
```

### Install Dependencies

```bash
pip install Flask
pip install openai
pip install Werkzeug
```

### Usage


1. **Upload Text File** - Visit the upload page (/) to upload a text file. The uploaded file will be used as the knowledge base for answering questions.
2. **Ask Question** - Once a file is uploaded, you can visit the ask question page (/ask) to input your question. The application will generate an answer based on the provided context and question.


### Running the Server

After installing the dependencies, you can run the InquireMate server locally:

```bash
python app.py
```
Once the server is running, navigate to http://localhost:5000 in your web browser to access the application.
### Mac/Linux Integration (Using Pathway):
```bash
pip install pathway
```
```bash
# app.py

from flask import Flask, request, jsonify
from openai import GPT, util

app = Flask(__name__)

# Initialize OpenAI API
openai_api_key = 'your_openai_api_key'
openai = GPT(api_key=openai_api_key)

# Initialize PathwayIndex for Mac/Linux users
from pathway import PathwayIndex
pathway_index = PathwayIndex()

@app.route('/ask', methods=['POST'])
def ask_question():
    # Retrieve question from user input
    question = request.form['question']
    
    # Query Pathway index to retrieve relevant documents (for Mac/Linux)
    relevant_documents = pathway_index.query(question)
    
    # Combine relevant documents into a single string
    document_text = ' '.join(relevant_documents)
    
    # Use OpenAI API to generate response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=document_text,
        max_tokens=50
    )
    
    # Extract response from OpenAI API result
    response_text = response.choices[0].text.strip()
    
    return jsonify({'response': response_text})

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload logic here
    # Save the uploaded file to a specific location or process it in some way
    return jsonify({'message': 'File uploaded successfully'})

# Additional routes and functionalities can be added here...

if __name__ == '__main__':
    app.run(debug=True)
```

## Usage

### Uploading Text File

1. Navigate to the homepage of the application.
2. Click on the "Upload Text File" button.
3. Select a text file (.txt) containing the data you want to query.
4. Click the "Upload" button to submit the file.

### Asking Questions

1.  After uploading the text file, you'll be redirected to the "Ask Question" page.
2. Enter your question in the provided input field.
3. Click the "Submit" button.
4. The application will generate a response based on the question and the content of the uploaded text file.

## About

InquireMate utilizes the OpenAI API to generate responses to user queries. It employs advanced natural language processing techniques to understand and interpret questions, providing accurate and informative answers.

##
InquireMate is developed as part of the LLM Bootcamp 2024 project, aiming to explore the intersection of artificial intelligence, machine learning, and web development. For any inquiries or feedback, please contact the project maintainers, @Dushyant-Mahto and @TushnikaC.

<div align="center">

## Made with ❤️ by Tushnika and Dushyant.

</div>
