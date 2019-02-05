import requests
from bs4 import BeautifulSoup

URL = 'https://revistaautoesporte.globo.com/rss/ultimas/feed.xml'


def get_items_nodes(url=URL):
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'xml')
    items = soup.find_all('item')
    return items


def parse_description(description_data):
    soup_description = BeautifulSoup(description_data.get_text(strip=True), 'html.parser')
    description_nodes = soup_description.find_all()
    description_items = list()
    for d_item in description_nodes:
        if d_item.name == 'p' and d_item.text.strip():
            description_items.append({
                'type': 'text',
                'content': d_item.get_text(strip=True)
            })
        if d_item.name == 'div':
            if d_item.find('img'):
                description_items.append({
                    'type': 'image',
                    'content': d_item.img['src']
                })
            if d_item.find('ul'):
                description_items.append({
                    'type': 'links',
                    'content': [li.a['href'] for li in d_item.find('ul') if hasattr(li, 'a') if li.a]
                })
    return description_items


def parse_item(node_item):
    title = node_item.find('title').get_text(strip=True)
    link = node_item.find('link').get_text(strip=True)
    description = parse_description(node_item.find('description'))
    item_data = dict(
        title=title,
        link=link,
        description=description,
    )
    return item_data


def create_feed():
    nodes = get_items_nodes()
    feed_dict = dict(feed=[
        dict(item=parse_item(node)) for node in nodes
    ])
    return feed_dict
