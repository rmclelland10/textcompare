from flask import Flask, request
from flask_cors import CORS
from textcompare import TextCompare

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    out_string = "Text Compare Exercise"
    return out_string
      
@app.route('/compare', methods = ['POST'])
def compare():
    data = request.get_json()
    text1, text2 = data['text1'], data['text2']
    text_compare = TextCompare(text1=text1, text2=text2)
    return text_compare.compare()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")