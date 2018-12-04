from bs4 import BeautifulSoup as bs
import summarizer
import requests
import json
def parse(url, location = '', category = ''):
    req = requests.get(url)
    xml = req.content
    soup = bs(xml, 'xml')
    result_array = []
    for item in soup.channel.find_all('item'):
        result_array.append(summarizer.summarize(item.link.string))
    result = (category, location, result_array)
    return result
