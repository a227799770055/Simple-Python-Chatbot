from types import MethodDescriptorType

from werkzeug.wrappers import request
import chatgui
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
  
  return 'Hi'

app.run(host='0.0.0.0', port=3000)
