"""
Server module for the Emotion Detection application.

Exposes a Flask API to process text payloads and evaluate emotional metrics.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("My Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the primary dashboard entry point webpage.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    """
    Retrieves textual input parameters, dispatches data to the analytical engine,
    and returns an evaluation log string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Error handling verification sequence
    if response is None or response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return response_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
