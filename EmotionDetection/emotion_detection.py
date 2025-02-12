import requests
import json

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        largest_value = 0
        dominant_emotion = ''
        formatted_text = json.loads(response.text)['emotionPredictions'][0]['emotion']

        for key, value in formatted_text.items():
            if value > largest_value:
                dominant_emotion = key
                largest_value = value

        formatted_text['dominant_emotion'] = dominant_emotion
    # If the response status code is either 400, set values to None
    elif response.status_code == 400:
        formatted_text = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return formatted_text
