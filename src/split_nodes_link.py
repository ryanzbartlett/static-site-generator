import re
from src.textnode import TextNode, TextType
from src.extract_markdown_links import extract_markdown_links


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError(f"Expected TextNode, got {type(node)}")
            
        else:
            parts = re.split(r"(\[.+?\))", node.text)
            
            for part in parts:
                if re.match(r"^\[.+?\]\(.+?\)$", part):
                    text, url = extract_markdown_links(part)[0]
                    new_nodes.append(TextNode(text, TextType.LINK, url))
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))

    return new_nodes