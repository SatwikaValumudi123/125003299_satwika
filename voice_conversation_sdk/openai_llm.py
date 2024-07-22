import aiohttp

class OpenAI_LLM:
    def __init__(self, api_key, system_prompt):
        self.api_key = api_key
        self.system_prompt = system_prompt
        self.endpoint = "https://api.openai.com/v1/completions"  

    async def query(self, text):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            "model": "text-davinci-003", 
            "prompt": f"{self.system_prompt}\n{text}",
            "max_tokens": 150
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.endpoint, headers=headers, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['choices'][0]['text'].strip()
                else:
                    raise Exception(f"Error {response.status}: {await response.text()}")
