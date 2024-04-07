from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import openai

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Set your OpenAI API key here
openai.api_key = 'Enter your own open AI key here'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def read_text_from_txt(txt_path):
    # Function to read text from a .txt file
    with open(txt_path, 'r') as file:
        return file.read()

def generate_answer(question, context):
    # Function to generate an answer using OpenAI's GPT-3 model
    # Construct a prompt combining the context and question
   
    prompt = f"{context}\nQuestion: {question}\nAnswer:"
    # Limit prompt to 4000 tokens (GPT-3's maximum input token limit)
    
    prompt = prompt[:4000]  
    # Generate response using OpenAI's Completion API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", 
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # Route to handle file upload
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save uploaded file to specified UPLOAD_FOLDER
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            try:
                file.save(filename)
            except Exception as e:
                return f"Error saving file: {e}"
            # Render template for asking question after file upload
            return render_template('ask_question.html', filename=filename)
             # Render template for file upload if request method is GET
    return render_template('upload.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    # Route to handle asking a question
    filename = request.form['filename']
    question = request.form['question']

    # Read text from uploaded file
    file_text = read_text_from_txt(filename)
    
    # Generate answer to the question using GPT-3 model
    answer = generate_answer(question, file_text)
    
   # Render template with answer
    return render_template('ask_question.html', filename=filename, answer=answer)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
