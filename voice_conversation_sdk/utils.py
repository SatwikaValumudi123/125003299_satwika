import pyaudio
import wave

def play_audio(file_path: str):
    """
    Play an audio file using PyAudio.

    Args:
        file_path (str): Path to the audio file in WAV format.
    """
    chunk = 1024  
    
   
    wf = wave.open(file_path, 'rb')
    
  
    p = pyaudio.PyAudio()
    
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    
   
    stream.stop_stream()
    stream.close()
    p.terminate()
