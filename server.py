"""
Server for the Emotion Detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Gets the emotion value from the server.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the scores from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotion labels and scores
    return f'''For the given statement, the system response is 'anger': {anger},
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.
        The dominant emotion is {dominant_emotion}.'''

@app.route("/")
def render_index_page():
    """
    Render the emotion detection UI.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
