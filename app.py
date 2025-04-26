from flask import Flask, request, jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided!"}), 400

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    result = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
    return jsonify({"sentiment": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
