from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest):

    def test_emotion_joy(self):
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'] , 'joy')

    def test_emotion_anger(self):
        # Test case for anger
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'] , 'anger')

    def test_emotion_disgust(self):
        # Test case for disgust
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'] , 'disgust')

    def test_emotion_sadness(self):
        # Test case for sadness
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'] , 'sadness')

    def test_emotion_fear(self):
        # Test case for fear
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'] , 'fear')