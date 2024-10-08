from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from tools.tools import get_profile_url_tavily


load_dotenv()


def lookup(name: str, role: str) -> str:
    llm = Ollama(model="llama3.1", temperature=0)
    lookup_template = """Given the full name {name_of_person}, who's a {role}. Get the link to their LinkedIn profile page.
    Your answer should contain only a URL.
    """
    lookup_prompt_template = PromptTemplate(input_variables=["name_of_person", "role"], template=lookup_template)

    # wrapper function to pass both name and role to get_profile_url_tavily
    def search_profile_tool(name: str):
        return get_profile_url_tavily(name, role)

    # list of tools
    tools_list = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=search_profile_tool,  # from tools
            description="Useful for when you need to get the LinkedIn Page URL"
        )
    ]

    # get the ReAct prompt template
    prompt = hub.pull("hwchase17/react")

    # agent
    agent = create_react_agent(llm=llm, tools=tools_list, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_list, verbose=True)

    result = agent_executor.invoke(
        input={"input": lookup_prompt_template.format_prompt(name_of_person=name, role=role)},
    )

    return result["output"]


if __name__ == '__main__':
    linkedin_url = lookup("Martin Oywa", "Machine Learning Engineer")
    print(linkedin_url)
