from faker import Faker

from textnode import TextNode, TextType
from htmlnode import HTMLNode

def maybe_none(val):
    fake = Faker()
    return fake.random_element([val, None])

def make_html_text_node(depth=1):
    fake = Faker()

    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'span', 'div']
    tag = fake.random_element(tags)

    value = maybe_none(' '.join(fake.words(3)))

    children = None
    if fake.boolean() and depth < 3:
        children = []
        for i in range(fake.random_int(min=0, max=3)):
            children.append(make_html_text_node(depth+1))

    prop_options = [
        ('title', ' '.join(fake.words(3))),
        ('aria-label', ' '.join(fake.words(3))),
        ('target', ' '.join(fake.words(3))),
        ('class', ' '.join(fake.words(3))),
        ('style', ' '.join(fake.words(3))),
        ('disabled', fake.random_element(['true', 'false'])),
    ]
    props = dict(fake.random_elements(prop_options))

    return HTMLNode(tag, value, children, props)


def main():
    html_nodes = []

    for _ in range(10):
        html_nodes.append(make_html_text_node())

    print('\n\n'.join(list(map(lambda n: str(n), html_nodes))))

main()
