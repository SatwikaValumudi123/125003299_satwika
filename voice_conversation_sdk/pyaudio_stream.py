import pyaudio

class PyAudioInputStream:
    def __init__(self):
        self.chunk = 1024  
        self.p = pyaudio.PyAudio()
        try:
            self.stream = self.p.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=16000,
                                      input=True,
                                      frames_per_buffer=self.chunk)
        except Exception as e:
            self.p.terminate()
            raise RuntimeError(f"Failed to open input stream: {e}")

    def read(self, chunksize):
        try:
            return self.stream.read(chunksize)
        except Exception as e:
            raise RuntimeError(f"Failed to read from input stream: {e}")

    def close(self):
        try:
            self.stream.stop_stream()
            self.stream.close()
        except Exception as e:
            print(f"Failed to close input stream: {e}")
        finally:
            self.p.terminate()

class PyAudioOutputStream:
    def __init__(self):
        self.chunk = 1024  
        self.p = pyaudio.PyAudio()
        try:
            self.stream = self.p.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=16000,
                                      output=True)
        except Exception as e:
            self.p.terminate()
            raise RuntimeError(f"Failed to open output stream: {e}")

    def write(self, data):
        try:
            self.stream.write(data)
        except Exception as e:
            raise RuntimeError(f"Failed to write to output stream: {e}")

    def close(self):
        try:
            self.stream.stop_stream()
            self.stream.close()
        except Exception as e:
            print(f"Failed to close output stream: {e}")
        finally:
            self.p.terminate()
