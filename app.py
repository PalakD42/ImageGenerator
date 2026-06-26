import os
import requests
import base64
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HF_MODEL = "stabilityai/stable-diffusion-3-medium-diffusers"


def generate_image(prompt):
    api_key = os.environ.get("HF_API_KEY")

    if not api_key:
        return None, "HF_API_KEY is not set."

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.post(
    f"https://router.huggingface.co/hf-inference/models/{HF_MODEL}",
    headers={
        "Authorization": f"Bearer {api_key}"
    },
    json={"inputs": prompt},
    timeout=120
)

        if response.status_code == 200:
            image_b64 = base64.b64encode(response.content).decode("utf-8")
            return f"data:image/png;base64,{image_b64}", None

        elif response.status_code == 503:
            return None, "Model is loading. Please wait and try again."

        else:
            try:
                error = response.json().get("error")
            except:
                error = response.text

            return None, error

    except requests.exceptions.RequestException as e:
        return None, str(e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("components", "").strip()

    if not prompt:
        return "Please enter a prompt.", 400

    image_data, error = generate_image(prompt)

    if error:
        return error, 500

    return image_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)