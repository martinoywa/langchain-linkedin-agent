from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

from parsers.output_parser import summary_parser
from scrapers import linkedin
from agents import linkedin_lookup

summary_template = """
    Given the information {information} about a particular person. I want you to create:
    1. A short summary of the person.
    2. Two interesting facts about the person.
    \n{format_instructions}
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template,
    partial_variables={"format_instructions": summary_parser.get_format_instructions()}
)
llm = Ollama(model="llama3.1", temperature=0)
chain = summary_prompt_template | llm | summary_parser


def main(name: str, role: str) -> str:
    linkedin_url = linkedin_lookup.lookup(name, role)
    linkedin_data = linkedin.scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=True)
    response = chain.invoke(input={"information": linkedin_data})

    return response


if __name__ == '__main__':
    result = main("Martin Oywa", "Machine Learning Engineer Safaricom")
    print(result)
