from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError('missing tag')
        if not self.children:
            raise ValueError('missing children')
        child_tags = ''
        for child in self.children:
            child_tags += child.to_html()
        return f'<{self.tag}>{child_tags}</{self.tag}>'