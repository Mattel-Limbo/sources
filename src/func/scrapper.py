from bs4 import BeautifulSoup
import requests

def scrape_attributes_with_values(url):
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    elements = []

    for element in soup.find_all(True):
        element_data = {'tag': element.name, 'attributes': {}}
        for attr, value in element.attrs.items():
            element_data['attributes'][attr] = value
        if element_data['attributes']:
            elements.append(element_data)

    return elements
