import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():
    # Load API keys from environment variables
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    llm = OpenAI()
    text = "What would be a good company name for an AI powered platform that helps user to do market research?"
    print(llm(text))


if __name__ == '__main__':
    main()
