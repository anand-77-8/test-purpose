from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Sentiment Analysis App!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    # Simple sentiment analysis based on keywords
    if "good" in text.lower():
        result = "Positive"
    else:
        result = "Negative"
    return jsonify({'sentiment': result})

if __name__ == '__main__':
    app.run(debug=True)
