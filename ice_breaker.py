import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

# PromptTemplate = Wrapper Class around Prompts so we can iterate on Prompts
# Chat Models = Wrapper around LLM. It is way to interact with LLM. Can organize message history
# Chains = Allow us to combine things together.

# Load .env file
load_dotenv()

if __name__ == "__main__":

    print("Hello Langchain")
    linkedin_profile_url = linkedin_lookup_agent(name="Adam Cole")
    summary_template = """
    given the linkedin {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # Can use open source LLMs locally. All supported by Langchain
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url, use_gist=True)

    print(chain.invoke(input = {"information":linkedin_data}))
