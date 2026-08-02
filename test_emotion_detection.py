from EmotionDetection import emotion_detector

def test_emotion_detector():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for statement, expected_emotion in test_cases:
        response = emotion_detector(statement)
        assert response["dominant_emotion"] == expected_emotion
        print(
            f"Input: {statement}\n"
            f"Expected: {expected_emotion}, "
            f"Detected: {response['dominant_emotion']}\n"
        )

    print("All tests passed!")

if __name__ == "__main__":
    test_emotion_detector()