class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ''
        return ''.join(list(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items())))
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
    
    def str_node(self, depth=1):
        def newline(v, d, s=2, c=' '):
            return '\n' + (c * d * s) + v
        
        result = f'HTMLNode: {self.tag}'
        
        if self.value:
            result += newline(f'value: {self.value}', depth)

        if self.props:
            result += newline(f'props: {self.props_to_html().strip()}', depth)
        
        if self.children:
            for child in self.children:
                result += newline(child.str_node(depth+1), depth)

        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        # return self.str_node()
