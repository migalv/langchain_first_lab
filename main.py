from langchain.llms import OpenAI
import os


def main():
    os.environ['OPENAI_API_KEY'] = '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'
    llm = OpenAI()
    text = "What would be a good company name for an AI powered platform that helps user to do market research?"
    print(llm(text))


if __name__ == '__main__':
    main()
