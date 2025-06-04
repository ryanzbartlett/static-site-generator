import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('h1', 'hello world')
        node2 = HTMLNode('h1', 'hello world')
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode('h1', 'hello world')
        node2 = HTMLNode('h2', 'hello world')
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        # Case A: no props → empty string
        node = HTMLNode('div')
        self.assertEqual(node.props_to_html(), '')

        # Case B: single prop
        node = HTMLNode('img', props={'src': 'logo.png'})
        self.assertEqual(node.props_to_html(), ' src="logo.png"')

        # Case C: multiple props (order doesn’t strictly matter, but we can check substrings)
        props = {'class': 'btn', 'id': 'submit-button'}
        node = HTMLNode('button', props=props)
        output = node.props_to_html()
        # It should contain both attributes (with a leading space before each)
        self.assertIn(' class="btn"', output)
        self.assertIn(' id="submit-button"', output)

    def test_eq_with_children(self):
        # Build a small tree: <ul><li>One</li><li>Two</li></ul>
        child1 = HTMLNode('li', 'One')
        child2 = HTMLNode('li', 'Two')
        parent1 = HTMLNode('ul', None, [child1, child2])

        # Build another tree in exactly the same shape
        c1_copy = HTMLNode('li', 'One')
        c2_copy = HTMLNode('li', 'Two')
        parent2 = HTMLNode('ul', None, [c1_copy, c2_copy])

        self.assertEqual(parent1, parent2)

        # Now mutate one child’s value → they should not be equal
        c2_copy.value = 'Three'
        self.assertNotEqual(parent1, parent2)

    def test_str_node_contains_nested_info(self):
        # Create a node with value, props, and one child
        child = HTMLNode('span', 'InnerText', None, {'style': 'color:red'})
        parent = HTMLNode('div', 'Hello', [child], {'class': 'container'})

        out = parent.str_node(depth=0)

        # 1) Top‐level should start with "HTMLNode: div"
        self.assertTrue(out.startswith('HTMLNode: div'))

        # 2) Since depth=0, the "value" line has no leading spaces
        self.assertIn('\nvalue: Hello', out)

        # 3) Similarly, the "props" line at depth=0 has no leading spaces
        self.assertIn('\nprops: class="container"', out)

        # 4) The child’s "HTMLNode: span" is inserted on its own line (no extra spaces before it)
        self.assertIn('\nHTMLNode: span', out)

        # 5) Inside the child’s own str_node(depth=1), its "value" is indented by two spaces
        self.assertIn('\n  value: InnerText', out)

        # 6) And the child’s "props" line is also indented by two spaces
        self.assertIn('\n  props: style="color:red"', out)


if __name__ == "__main__":
    unittest.main()
