import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

from youtube_genie import summarise_transcript_with_open_ai


def main():
    # Load API keys from environment variables
    load_dotenv()

    summarise_transcript_with_open_ai(
        youtube_url="https://www.youtube.com/watch?v=qaPMdcCqtWk&list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5&index=20&t=5s&ab_channel=DataIndependent"
    )

    # llm = OpenAI()
    # text = "What would be a good company name for an AI powered platform that helps user to do market research?"
    # print(llm(text))


if __name__ == '__main__':
    main()
