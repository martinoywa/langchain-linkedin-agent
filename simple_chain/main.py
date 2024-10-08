from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from scrapers import linkedin

summary_template = """
    Given the information {information} about a particular person. I want you to create:
    1. A short summary of the person.
    2. Two interesting facts about the person.
"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
llm = Ollama(model="llama3.1", temperature=0)
chain = summary_prompt_template | llm

def main(information: str) -> str:
    response = chain.invoke(input={"information": information})

    return response


if __name__ == '__main__':
    linkedin_data = linkedin.scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/martinoywa/",
                                                     mock=True)
    print(main(linkedin_data))
