from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key here (safely)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_email():
    data = request.get_json()
    leave_type = data.get("type")
    prompt = data.get("prompt")

    full_prompt = f"Write a formal {leave_type} email based on this reason: {prompt}"

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=full_prompt,
            max_tokens=150,
            temperature=0.7
        )

        return jsonify({"generated_email": response.choices[0].text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
