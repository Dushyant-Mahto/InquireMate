from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import openai

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

openai.api_key = 'Enter your own open AI key here'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def read_text_from_txt(txt_path):
    with open(txt_path, 'r') as file:
        return file.read()

def generate_answer(question, context):
    prompt = f"{context}\nQuestion: {question}\nAnswer:"
    prompt = prompt[:4000]  
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", 
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

    file_text = read_text_from_txt(filename)

    answer = generate_answer(question, file_text)
    
    return render_template('ask_question.html', filename=filename, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
