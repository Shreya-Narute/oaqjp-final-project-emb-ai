# Final Project: Emotion Detection Application

## Project Overview

This Final Project demonstrates an Emotion Detection application using Natural Language Processing (NLP) and the IBM Watson Emotion Prediction service.

The application analyzes text entered by a user and identifies five emotions: anger, disgust, fear, joy, and sadness. It also determines the dominant emotion in the given text.

The application is developed using Python and Flask, with a web interface that allows users to enter text and view the emotion analysis results.

## Project Objectives

- Build an emotion detection function using the IBM Watson NLP service.
- Identify five emotions from the submitted text.
- Determine the dominant emotion.
- Create a Flask web application for text input and emotion analysis.
- Handle blank input and HTTP error responses.
- Test the application using Python unit tests.
- Perform static code analysis using Pylint.

## Features

- **Emotion Detection:** Identifies anger, disgust, fear, joy, and sadness.
- **Dominant Emotion:** Determines the emotion with the highest score.
- **Flask Web Interface:** Allows users to submit text for analysis.
- **Input Validation:** Handles blank text input.
- **Error Handling:** Handles HTTP 400 responses and unavailable service responses.
- **Unit Testing:** Tests the emotion detection function.
- **Static Code Analysis:** Uses Pylint to check code quality.

## Technologies Used

- Python
- Flask
- IBM Watson NLP Emotion Prediction service
- Requests
- HTML
- JavaScript
- Unittest
- Pylint
- Git and GitHub

## Project Structure

```text
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── test_emotion_detection.py
├── server.py
└── README.md
```

## Emotion Detection Function

The `emotion_detector()` function sends the input text to the IBM Watson NLP Emotion Prediction service and processes the returned emotion scores.

The function returns a dictionary containing:

- `anger`
- `disgust`
- `fear`
- `joy`
- `sadness`
- `dominant_emotion`

The dominant emotion is the emotion with the highest score.

If the input is blank, the service returns an HTTP 400 response, or an error prevents analysis, the function returns `None` values for the emotion scores and dominant emotion.

## Flask Web Application

The Flask application is implemented in `server.py`.

It provides two routes:

- `/` — Displays the emotion detection web page.
- `/emotionDetector` — Receives submitted text and returns the emotion analysis results.

The application validates blank input and displays an appropriate error message when the input is empty or the emotion analysis service is unavailable.

## Unit Testing

Unit tests are implemented in `test_emotion_detection.py` using Python's `unittest` framework.

The tests verify the dominant emotion result and the handling of blank input. The IBM Watson request is mocked in the dominant emotion test so the test can run without contacting the external service.

Run the unit tests using:

```bash
python -m unittest -v test_emotion_detection.py
```

## Static Code Analysis

Pylint is used to analyze the Flask server code for coding standards and potential issues.

Run the analysis using:

```bash
python -m pylint server.py
```

The recorded Pylint score for this project was **10.00/10**.

## How to Run the Application

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install the required packages

```bash
python -m pip install Flask requests pylint
```

### 3. Start the Flask server

```bash
python server.py
```

### 4. Open the application

Open the following address in your web browser:

http://127.0.0.1:5000

Enter text into the input field and run the emotion analysis.

**Note:** Successful live emotion predictions require the IBM Watson NLP service endpoint to be accessible. If the service is unavailable, the application displays an error message instead of a prediction.

## Conclusion

This Final Project demonstrates the development of an NLP-based emotion detection application using Python, Flask, and the IBM Watson Emotion Prediction service. It includes input validation, error handling, unit testing, and static code analysis.

The project illustrates how NLP can be integrated into a web application to identify emotions expressed in text.