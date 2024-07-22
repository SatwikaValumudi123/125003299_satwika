import json

def handle_stt_result(response_text):
  
    response = json.loads(response_text)
    
    
    transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
    
    print("Transcript:", transcript)


response_text = '''
{
    "metadata": {
        "transaction_key": "deprecated",
        "request_id": "d5623ee2-537a-46bd-811c-b8c3b094c7e2",
        "sha256": "8a90127bbb21b686fedf5f7d7202deb3475d3ebd54c48cd6320d178e76522877",
        "created": "2024-07-22T08:58:54.767Z",
        "duration": 4.98,
        "channels": 1,
        "models": ["1ed36bac-f71c-4f3f-a31f-02fd6525c489"],
        "model_info": {
            "1ed36bac-f71c-4f3f-a31f-02fd6525c489": {
                "name": "general",
                "version": "2024-01-26.8851",
                "arch": "base"
            }
        }
    },
    "results": {
        "channels": [{
            "alternatives": [{
                "transcript": "good evening being ladies and gentlemen we like to welcome you to flu down your radio broadcast of the",
                "confidence": 0.98828125,
                "words": [
                    {"word": "good", "start": 0.118333325, "end": 0.19722222, "confidence": 0.9633789},
                    {"word": "evening", "start": 0.19722222, "end": 0.355, "confidence": 1.0},
                    {"word": "being", "start": 0.355, "end": 0.59166664, "confidence": 0.6147461},
                    {"word": "ladies", "start": 0.59166664, "end": 0.9072222, "confidence": 1.0},
                    {"word": "and", "start": 0.9072222, "end": 1.0649999, "confidence": 0.99316406},
                    {"word": "gentlemen", "start": 1.0649999, "end": 1.3016666, "confidence": 0.9975586},
                    {"word": "we", "start": 1.4594444, "end": 1.6172222, "confidence": 0.59814453},
                    {"word": "like", "start": 1.6172222, "end": 1.775, "confidence": 0.9980469},
                    {"word": "to", "start": 1.775, "end": 1.9327776, "confidence": 0.9902344},
                    {"word": "welcome", "start": 1.9327776, "end": 2.1694443, "confidence": 0.9995117},
                    {"word": "you", "start": 2.1694443, "end": 2.327222, "confidence": 0.99658203},
                    {"word": "to", "start": 2.327222, "end": 2.485, "confidence": 0.984375},
                    {"word": "flu", "start": 2.485, "end": 2.7216666, "confidence": 0.23852539},
                    {"word": "down", "start": 2.7216666, "end": 2.9583333, "confidence": 0.9946289},
                    {"word": "your", "start": 2.9583333, "end": 3.116111, "confidence": 0.8730469},
                    {"word": "radio", "start": 3.116111, "end": 3.616111, "confidence": 0.8491211},
                    {"word": "broadcast", "start": 4.0627775, "end": 4.536111, "confidence": 0.98828125},
                    {"word": "of", "start": 4.536111, "end": 4.6938887, "confidence": 0.99072266},
                    {"word": "the", "start": 4.6938887, "end": 4.98, "confidence": 0.98583984}
                ]
            }]
        }]
    }
}
'''


handle_stt_result(response_text)
