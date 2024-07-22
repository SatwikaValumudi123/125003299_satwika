import aiohttp

class DeepgramSTT:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.deepgram.com/v1/listen"

    async def convert(self, audio_data):
        headers = {
            'Authorization': f'Token {self.api_key}',
            'Content-Type': 'audio/wav'
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.endpoint, headers=headers, data=audio_data) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise Exception(f"Error {response.status}: {await response.text()}")
