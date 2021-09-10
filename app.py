from types import MethodDescriptorType

from nltk.corpus.reader.wordnet import res_similarity

# from werkzeug.wrappers import request
import chatbot_model
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return "This is home"

@app.route("/botrespon", methods = ['POST'])
def botrespon():
    value = request.form.get('key')
    response = chatbot_model.chatbot_response(value)
    return response


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)


