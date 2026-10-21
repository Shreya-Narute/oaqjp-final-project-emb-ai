
"""Unit tests for the emotion detection application."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test emotion detector behavior."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_joy(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.02,
                        "joy": 0.90,
                        "sadness": 0.06,
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_blank_input(self):
        result = emotion_detector(" ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
