from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], "joy")

        result1 = emotion_detector("I am reagladlly mad about this")
        self.assertEqual(result1['dominant_emotion'], "anger")

        result1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result1['dominant_emotion'], "disgust")

        result1 = emotion_detector("I am so sad about this")
        self.assertEqual(result1['dominant_emotion'], "sadness")

        result1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result1['dominant_emotion'], "fear")

unittest.main()
