import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_value(self):
        # When both tag and value are truthy, expect <tag>value</tag>
        node = LeafNode('p', 'Hello, world!')
        expected = '<p>Hello, world!</p>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_without_tag_returns_value(self):
        # If tag is falsy (e.g. None or empty string), it should just return value
        node1 = LeafNode(None, 'Just text')
        self.assertEqual(node1.to_html(), 'Just text')

        node2 = LeafNode('', 'Bare text')
        self.assertEqual(node2.to_html(), 'Bare text')

    def test_to_html_without_value_raises_value_error(self):
        # If value is falsy (None or empty), to_html must raise ValueError
        with self.assertRaises(ValueError):
            LeafNode('span', None).to_html()

        with self.assertRaises(ValueError):
            LeafNode('span', '').to_html()

    def test_eq_between_two_identical_leafnodes(self):
        # Inherited __eq__ compares tag, value, children, and props
        n1 = LeafNode('span', 'Foo', props={'style': 'color:red'})
        n2 = LeafNode('span', 'Foo', props={'style': 'color:red'})
        self.assertEqual(n1, n2)

    def test_not_eq_when_props_differ(self):
        # Changing props (or tag/value) makes them unequal
        base = LeafNode('span', 'Bar', props={'class': 'a'})
        diff_props = LeafNode('span', 'Bar', props={'class': 'b'})
        diff_tag   = LeafNode('div',  'Bar', props={'class': 'a'})
        diff_value = LeafNode('span', 'Baz', props={'class': 'a'})

        self.assertNotEqual(base, diff_props)
        self.assertNotEqual(base, diff_tag)
        self.assertNotEqual(base, diff_value)

    def test_not_eq_against_non_htmlnode(self):
        # Comparing to something that isn’t an HTMLNode should be False
        leaf = LeafNode('em', 'Italic')
        self.assertNotEqual(leaf, "some string")
        self.assertFalse(leaf == 123)


if __name__ == "__main__":
    unittest.main()