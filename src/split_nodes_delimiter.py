from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    valid_delimiters = ['**', '_', '`']

    if delimiter not in valid_delimiters:
        raise ValueError(f"Invalid delimiter: {delimiter}. Valid delimiters are: {valid_delimiters}")

    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError(f"Expected TextNode, got {type(node)}")
        
        elif node.text_type != TextType.TEXT:
            new_nodes.append(node)
            
        else:
            parts = node.text.split(delimiter)
            for part in parts:
                if part:
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes