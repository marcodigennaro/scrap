import requests
import csv
from bs4 import BeautifulSoup


def fetch_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_html(html_content):
    return BeautifulSoup(html_content, 'html.parser')


def write_to_csv(filename, headers, rows):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)


def extract_data(soup, structure):
    data = []
    sections = soup.find_all(structure['section_tag'], class_=structure['section_class'])
    for section in sections:
        row = []
        for item in structure['items']:
            element = section.find(item['tag'], class_=item['class'])
            row.append(element.text.strip() if element else '')
        data.append(row)
    return data
