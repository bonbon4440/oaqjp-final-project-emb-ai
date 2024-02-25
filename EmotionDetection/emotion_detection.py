import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sends an HTTP request to the URL
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    # Error handling
    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
    
    # If no error - gets the values of the formatted response
    else:
        anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    # Create the dictionary based on the response
    dictionary = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    # Find the dominant emotion & add it to the dictionary
    if response.status_code == 400:
        dictionary["dominant_emotion"] = None
    else:
        dictionary["dominant_emotion"] = max(dictionary, key=dictionary.get)

    return dictionary