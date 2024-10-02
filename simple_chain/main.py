from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

summary_template = """
    Given the information {information} about a particular person. I want you to create:
    1. A short summary of the person.
    2. Two interesting facts about the person.
"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
llm = Ollama(model="llama3.1", temperature=0)


def main(information: str) -> str:
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    return response


if __name__ == '__main__':
    information = """
    Andrej Karpathy (born 23 October 1986[2]) is a Slovak-Canadian computer scientist who served as the director of artificial intelligence and Autopilot Vision at Tesla. He co-founded and formerly worked at OpenAI,[3][4][5] where he specialized in deep learning and computer vision.[6][7][1][8]

    Education and early life
    Karpathy was born in Bratislava, Czechoslovakia (now Slovakia)[9][10][11][12] and moved with his family to Toronto when he was 15.[13] He completed his Computer Science and Physics bachelor's degrees at University of Toronto in 2009[14] and his master's degree at University of British Columbia in 2011,[14] where he worked on physically-simulated figures (for example, a simulated runner or a simulated person in a crowd) with his adviser Michiel van de Panne.

    Karpathy received a PhD from Stanford University in 2015 under the supervision of Fei-Fei Li, focusing on the intersection of natural language processing and computer vision, and deep learning models suited for this task.[15][16]

    Career and research
    He authored and was the primary instructor of the first deep learning course at Stanford, CS 231n: Convolutional Neural Networks for Visual Recognition.[17] It became one of the largest classes at Stanford, growing from 150 students in 2015 to 750 in 2017.[18]

    Karpathy is a founding member of the artificial intelligence research group OpenAI,[19][20] where he was a research scientist from 2015 to 2017.[18] In June 2017 he became Tesla's director of artificial intelligence and reported to Elon Musk.[21][7][22] He was named one of MIT Technology Review's Innovators Under 35 for 2020.[23] After taking a several months-long sabbatical from Tesla, he announced he was leaving the company in July 2022.[24] As of February 2023, he makes YouTube videos on how to create artificial neural networks.[25]

    It was reported on February 9 2023 that Karpathy had announced he was returning to OpenAI.[26]

    A year later on February 13 2024, an OpenAI spokesperson confirmed that Karpathy had left OpenAI. [27]
    """

    print(main(information))
