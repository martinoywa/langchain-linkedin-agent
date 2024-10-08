import os
import requests
from dotenv import load_dotenv


load_dotenv()

# Docstrings are for langchain agents
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from LinkedIn profile page.
    Manually scrape information from LinkedIn profile page.
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/martinoywa/8c1043afa2b2d306f0089ac99ec78a4d/raw/ae583589f35a02da88b7470f4d6793ae6fb52158/maritnoywa.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        headers = {'Authorization': f'Bearer {os.getenv("PROXYCURL_API_KEY")}'}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'linkedin_profile_url': linkedin_profile_url,
            'personal_contact_number': 'include',
            'personal_email': 'include',
            'inferred_salary': 'include',
            'skills': 'include',
            'use_cache': 'if-present',
            'fallback_to_cache': 'on-error',
        }
        response = requests.get(api_endpoint,
                                params=params,
                                headers=headers,
                                timeout=10)

    data = response.json()

    # cleanup
    data = {
        k: v for k, v in data.items()
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
    }

    return data


# if __name__ == '__main__':
#     print(
#         # TODO add permanent link to photo in data
#         scrape_linkedin_profile(
#             linkedin_profile_url="https://www.linkedin.com/in/martinoywa/",
#             mock=True
#         )
#     )
