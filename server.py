''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package :
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using the function
        Input
           string
        
        Output
           json containing emotions list with dominant emotion
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    json_data = emotion_detector(text_to_analyze)

    # Estrazione delle emozioni e dei loro valori
    emotions = {k: v for k, v in json_data.items() if k != 'dominant_emotion'}
    dominant_emotion = json_data['dominant_emotion']

    # Creazione della stringa di output
    response = "For the given statement, the system response is "
    response += ", ".join([f"'{emotion}': {value}" for emotion, value in emotions.items()])
    response += f". The dominant emotion is **{dominant_emotion}**."
    
    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
