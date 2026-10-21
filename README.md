# NLP Emotion Detection Application

## Project Overview

This project is a web-based emotion detection application built using Python and Flask. It uses the IBM Watson NLP Emotion Prediction service to analyze text and identify five emotions: anger, disgust, fear, joy, and sadness.

## Features

- Analyze user-provided text for emotions.
- Display emotion scores and the dominant emotion when the service is available.
- Handle blank input with an HTTP 400 response.
- Handle unavailable emotion detection service responses.
- Provide a browser-based interface.

## Technologies Used

- Python
- Flask
- Requests
- HTML, CSS, and JavaScript
- IBM Watson NLP Emotion Prediction service
- Unittest

## Project Structure

- `EmotionDetection/emotion_detection.py` — emotion detection function
- `EmotionDetection/__init__.py` — package initialization
- `test_emotion_detection.py` — unit tests
- `server.py` — Flask web application
- `templates/index.html` — web interface
- `static/mywebscript.js` — browser-side request handling

## Run the Application

1. Activate your Python virtual environment.
2. Install the required packages: `python -m pip install Flask requests pylint pytest`
3. Start the application: `python server.py`
4. Open `http://127.0.0.1:5000` in a browser.

**Note:** Successful emotion analysis requires connectivity to the IBM Watson NLP service.
