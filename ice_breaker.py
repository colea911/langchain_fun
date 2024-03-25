
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# PromptTemplate = Wrapper Class around Prompts so we can iterate on Prompts
# Chat Models = Wrapper around LLM. It is way to interact with LLM. Can organize message history
# Chains = Allow us to combine things together.


print(os.environ['OPENAI_API_KEY'])

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")
    information = "Elon Musk is amaaaaaaaazing"


    summary_template = """
    given the {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template = summary_template)
    
    # Can use open source LLMs locally. All supported by Langchain
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information":information})

    print(res)
