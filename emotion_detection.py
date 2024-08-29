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
    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
        
    # Returning a dictionary containing sentiment analysis results
    return formatted_response