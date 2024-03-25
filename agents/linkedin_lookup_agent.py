from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import Tool
from tools.tools import get_profile_url
# from wrappers.wrappers import get_profile_url
 
def lookup(name: str) -> str:

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """Given the full name of {name_of_person} I want you to get me a link to their Linkedin profile page. Your answer should only contain a URL"""

    # Agent looks at description when deciding to use this tool class
    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url,
            description="useful for when you need the LinkedIn page URL",
        )
    ]
    # decides reasoning process. Verbose lets us see each reasoning step.
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    # delete
    # linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    linkedin_profile_url = agent.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    return linkedin_profile_url
