import os
import requests


def scrape_linkedin_profile(linkedin_profile_url="", use_gist=False):
    """Scrape information from linkedin profiles. Manually scrape information from the LinkedIn profile"""



    

    

    # Get Response
    if linkedin_profile_url and not use_gist:
        proxycurl_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            proxycurl_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
        )
    else:
        gist_endpoint = os.environ.get("PRIVATE_GIST")
        response = requests.get(gist_endpoint)

    # Parse Data
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data
