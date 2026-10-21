
"""Flask web server for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Analyze submitted text and return emotion results."""
    text_to_analyze = request.values.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Please enter some text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Unable to analyze the text. Please try again later.", 503

    return (
        f"For the given statement, the dominant emotion is "
        f"{result['dominant_emotion']}. "
        f"Anger: {result['anger']}, "
        f"Disgust: {result['disgust']}, "
        f"Fear: {result['fear']}, "
        f"Joy: {result['joy']}, "
        f"Sadness: {result['sadness']}"
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
