import asyncio
from voice_conversation_sdk.sdk import VoiceBotSDK
from voice_conversation_sdk.utils import play_audio  
from voice_conversation_sdk.pyaudio_stream import PyAudioInputStream, PyAudioOutputStream
from voice_conversation_sdk.handle_stt import handle_stt_result
 


async def main():
    
    sdk = VoiceBotSDK(
        stt_config={
            'engine': 'Deepgram',
            'api_key': '2ea290c37a9c4e1bf290393dad7dfe5c47b8f796'
        },
        tts_config={
            'engine': 'Deepgram',
            'api_key': '2ea290c37a9c4e1bf290393dad7dfe5c47b8f796'
            
        },
        llm_config={
            'engine': 'OpenAI',
            'api_key': 'sk-proj-Hg6x5uk6dEtjiSQCnezFT3BlbkFJ6zwYyYvIxJeM5tu6n80O',
            'system_prompt': 'Your system prompt here.'
        }
    )
    
    
    input_stream = PyAudioInputStream()
    output_stream = PyAudioOutputStream()

    try:
       
        result = await sdk.stream_conversation(input_stream, output_stream)
        print("Processing results:", result)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        
        input_stream.close()
        output_stream.close()

    response_text = '{"results": {"channels": [{"alternatives": [{"transcript": "Sample text"}]}}]}'
    handle_stt_result(response_text)


if __name__ == '__main__':
    asyncio.run(main())
