"""

xml_printer. 

Write a short, modular Python script that:
	1.	Fetches an XML document from a URL.
	2.	Parses key fields from it (e.g., name, price, description, calories).
	3.	Prints a clean table of values directly to the terminal.

"""

import requests
import xml.etree.ElementTree as ET

def fetch_xml(url) ->  list:
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def parse_food_items (xml_content):
    root = ET.fromstring(xml_content)
    data = []
    for food in root.findall("food"):
        item = {
            "name": food.findtext("name"),
            "price": food.findtext("price"),
            "description": food.findtext("description"),
            "calories": food.findtext("calories")
        }
        data.append(item)
    return data

if __name__ == "__main__":
    url = "https://www.w3schools.com/xml/simple.xml"
    xml = fetch_xml(url)
    items = parse_food_items(xml)
    for item in items:
        print(item)