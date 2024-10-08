from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub


def lookup(name: str) -> str:
    llm = Ollama(model="llama3.1", temperature=0)
    lookup_template = """Given the fill name {name_of_person}. Get the link to their LinkedIn profile page.
    Your answer should contain only a URL.
    """
    lookup_prompt_template = PromptTemplate(input_variables=["name_of_person"], template=lookup_template)

    # list of tools
    tools_list = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func="?", # from tools
            description="Useful for when you need to get the LinkedIn Page URL"
        )
    ]

    # get the ReAct prompt template
    prompt = hub.pull("hwchase17/react")

    # agent
    agent = create_react_agent(llm=llm, tools=tools_list, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_list, verbose=True)

    result = agent_executor.invoke(
        input={"input": lookup_prompt_template.format_prompt(name_of_person=name)}
    )

    return result["output"]


if __name__ == '__main__':
    linkedin_url = lookup("Martin Oywa")
    print(linkedin_url)
