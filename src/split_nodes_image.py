import re
from src.textnode import TextNode, TextType
from src.extract_markdown_images import extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError(f"Expected TextNode, got {type(node)}")
            
        else:
            parts = re.split(r"(!\[.+?\))", node.text)
            
            for part in parts:
                if re.match(r"^!\[.+?\]\(.+?\)$", part):
                    alt, url = extract_markdown_images(part)[0]
                    new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))

    return new_nodes