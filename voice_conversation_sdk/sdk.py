import json
import asyncio
import time
from .deepgram_stt import DeepgramSTT
from .deepgram_tts import DeepgramTTS
from .openai_llm import OpenAI_LLM
from .pyaudio_stream import PyAudioInputStream, PyAudioOutputStream
from .utils import play_audio

class VoiceBotSDK:
    def __init__(self, stt_config, tts_config, llm_config):
        self.stt_engine = DeepgramSTT(stt_config['api_key'])
        self.tts_engine = DeepgramTTS(tts_config['api_key'])
        self.llm_engine = OpenAI_LLM(llm_config['api_key'], llm_config['system_prompt'])
    
    async def stream_conversation(self, input_stream, output_stream):
        start_time = time.time()
        
       
        audio_buffer = b''
        stt_start_time = time.time()

        while True:
            try:
                
                audio_data = input_stream.read(1024)
                if not audio_data:
                    break

                
                audio_buffer += audio_data

                response_text = await self.stt_engine.convert(audio_buffer)
                transcript = self.handle_stt_result(response_text)
                
                
                if self.is_speech_stopped(response_text):
                    break

            except Exception as e:
                print(f"Error during STT conversion: {e}")
                break

        stt_time = time.time() - stt_start_time
        
       
        llm_start_time = time.time()
        try:
            llm_response = await self.llm_engine.query(transcript)
        except Exception as e:
            print(f"Error during LLM query: {e}")
            llm_response = "Sorry, there was an error processing your request."
        llm_time = time.time() - llm_start_time
        
        
        tts_output_file = "output.wav"
        try:
            await self.tts_engine.convert(llm_response, tts_output_file)
        except Exception as e:
            print(f"Error during TTS conversion: {e}")
            tts_output_file = None
        
       
        if tts_output_file:
            play_audio(tts_output_file)
        
     
        total_time_taken = time.time() - start_time
        
        return {
            "stt_time": stt_time,
            "llm_time": llm_time,
            "total_time": total_time_taken
        }
    
    def handle_stt(self, response_text):
        response = json.loads(response_text)
        return response['results']['channels'][0]['alternatives'][0]['transcript']
    
    def is_speech_stopped(self, response_text):
        response = json.loads(response_text)
        return response.get('is_final', False)  
