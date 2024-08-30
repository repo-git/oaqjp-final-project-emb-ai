import requests
import json

def emotion_detector(text_to_analyze):
    '''
        Function to use the Emotion Predict of the Watson NLP Library.

        Input
           string

        Output
           string
    '''
    # if text_to_analyze.strip():

    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=header)

    emotions = {}
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        
        # Extract "emotions"
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Evaluate max emotion
        max_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = max_emotion
    elif response.status_code == 400:
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None

    # Returning a dictionary containing the response in text format
    return emotions