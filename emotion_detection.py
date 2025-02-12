import requests
import json

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    formatted_text = json.loads(response.text)['emotionPredictions'][0]['emotion']

    last_value = 0
    dominant_emotion = ''

    for key, value in formatted_text.items():
        if value > last_value:
            dominant_emotion = key
        
        last_value = value

    formatted_text['dominant_emotion'] = dominant_emotion

    return formatted_text
