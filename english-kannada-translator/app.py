from flask import Flask, render_template, request
from translator.translator import translate_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_route():
    try:
        english_text = request.form.get('english_text', '')
        if not english_text.strip():
            return render_template('result.html', translation='Please enter some text to translate')
        kannada_translation = translate_text(english_text)
        return render_template('result.html', english_text=english_text, translation=kannada_translation)
    except Exception as e:
        return render_template('result.html', translation=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)