import os 
import sys
from dotenv import load_dotenv 

from anthropic import Anthropic 

load_dotenv('Keys/Claude_api_key.env')
# Set API Key 
client = Anthropic(
    api_key = os.environ.get("CLAUDE_API_KEY")
)
def ask_claude(question, model="claude-3-haiku-20240307", max_tokens=1000):

    try:
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error: {e}")
        return None 
def interactive_questions():
    print("Welcome to the Claude API interactive questions!")
    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == "exit":
            print("Thank you for using the Claude API interactive questions!")
            break     
        if not question:
            print("Please enter a valid question.")
            continue 
        answer = ask_claude(question)
        print(f"\nClaude: {answer}\n")

def main():
    print("CLaude API Connection Script")
    print("="*30)
    print()

    interactive_questions()

if __name__ == "__main__":
    main()
