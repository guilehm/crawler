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
    for d_node in description_nodes:
        if d_node.name == 'p' and d_node.text.strip():
            description_items.append({
                'type': 'text',
                'content': d_node.get_text(strip=True),
            })
        if d_node.name == 'div':
            if d_node.find('img'):
                content = d_node.img['src']
                if content:
                    description_items.append({
                        'type': 'image',
                        'content': content,
                    })
            if d_node.find('ul'):
                content = [li.a['href'] for li in d_node.find('ul') if hasattr(li, 'a') if li.a]
                if content:
                    description_items.append({
                        'type': 'links',
                        'content': content,
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
