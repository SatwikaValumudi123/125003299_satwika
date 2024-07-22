import aiohttp

class DeepgramTTS:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.deepgram.com/v1/speak"

    async def convert(self, text, output_file):
        headers = {
            'Authorization': f'Token {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            "text": text,
            "voice": "en_us_male" 
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.endpoint, headers=headers, json=payload) as response:
                if response.status == 200:
                    with open(output_file, 'wb') as f:
                        f.write(await response.read())
                else:
                    raise Exception(f"Error {response.status}: {await response.text()}")
