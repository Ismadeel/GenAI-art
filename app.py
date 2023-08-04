import os 
import replicate
from flask import Flask, render_template,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500", "http://127.0.0.1:5500/index.html"])


# Define a simple Python function
def get_greeting(prompt):
    return "Your Prompt: "+prompt

def get_logo(prompt):
    os.environ["REPLICATE_API_TOKEN"]='r8_T36OWfUdsxhg7rOzQorvX8igWqwcl7m13NJ50'

    output = replicate.run(
    "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
    input={"prompt": prompt},
    )

    lora_url = "https://replicate.delivery/pbxt/fdtiMuQFF1yQAS22N4JWR3epRbW7ea5shRBsSmFqJBceBTZFB/tmpmzwgpo3puc.safetensors"

    output_url = replicate.run(
    "replicate/lora:97ec1b97e5e6a6476e45ba7211d368509bbf39c30a927e39637f3cb98b36ac91",
    input={
        "prompt": "IT company logo",
        "lora_urls": lora_url,
    },
    )
    return output_url
    
@app.route('/')
def index():
    prompt = request.args.get('prompt')  # 'Guest' is the default value if 'name' is not provided
    # Call the Python function in the HTML template
    greeting = get_logo(prompt)
    #print(get_logo())
    return jsonify(greeting)

if __name__ == '__main__':
    app.run()
