from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation as mt

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french=mt.translator.english_to_french(textToTranslate)
    return french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english=mt.translator.french_to_english(textToTranslate)
    return english

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)
