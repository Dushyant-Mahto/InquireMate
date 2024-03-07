from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import openai

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set your OpenAI API key
openai.api_key = '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'

# Create the uploads directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to read text from a .txt file
def read_text_from_txt(txt_path):
    with open(txt_path, 'r') as file:
        return file.read()

# Function to make API request to OpenAI's GPT-3 model
def generate_answer(question, context):
    prompt = f"{context}\nQuestion: {question}\nAnswer:"
    prompt = prompt[:4000]  # Limit the prompt to 4000 tokens
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Use the davinci-codex engine
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            try:
                file.save(filename)
            except Exception as e:
                return f"Error saving file: {e}"
            
            return render_template('ask_question.html', filename=filename)
    return render_template('upload.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    filename = request.form['filename']
    question = request.form['question']

    # Read text from the uploaded .txt file
    file_text = read_text_from_txt(filename)

    # Generate answer using OpenAI GPT-3 model
    answer = generate_answer(question, file_text)
    
    return render_template('ask_question.html', filename=filename, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
