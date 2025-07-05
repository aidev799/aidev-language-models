from anthropic import Anthropic 
import os 
from dotenv import load_dotenv 

load_dotenv('Keys/Claude_api_key.env')

client = Anthropic(
    api_key = os.environ.get("CLAUDE_API_KEY")
)

response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": "Tell me a joke"}
            ]
)

print(response.content[0].text)