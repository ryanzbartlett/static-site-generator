import unittest
from leafnode import LeafNode
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_type_text(self):
        tn = TextNode("plain text", TextType.TEXT)
        result = text_node_to_html_node(tn)

        # TEXT should yield a LeafNode with tag=None, value="plain text", props=None
        expected = LeafNode(None, "plain text")
        self.assertEqual(result, expected)

    def test_text_type_bold(self):
        tn = TextNode("make me bold", TextType.BOLD)
        result = text_node_to_html_node(tn)

        # BOLD → <b>…</b>
        expected = LeafNode("b", "make me bold")
        self.assertEqual(result, expected)

    def test_text_type_italic(self):
        tn = TextNode("slanted", TextType.ITALIC)
        result = text_node_to_html_node(tn)

        # ITALIC → <i>…</i>
        expected = LeafNode("i", "slanted")
        self.assertEqual(result, expected)

    def test_text_type_code(self):
        tn = TextNode("print('hi')", TextType.CODE)
        result = text_node_to_html_node(tn)

        # CODE → <code>…</code>
        expected = LeafNode("code", "print('hi')")
        self.assertEqual(result, expected)

    def test_text_type_link(self):
        url = "https://example.com"
        tn = TextNode("click here", TextType.LINK, url=url)
        result = text_node_to_html_node(tn)

        # LINK → <a href="...">…</a>
        expected = LeafNode("a", "click here", props={"href": url})
        self.assertEqual(result, expected)

    def test_text_type_image(self):
        url = "https://cdn.example.com/pic.jpg"
        alt  = "An example image"
        tn = TextNode(alt, TextType.IMAGE, url=url)
        result = text_node_to_html_node(tn)

        # IMAGE → <img src="..." alt="...">
        # (Note: LeafNode stores value="" for images per the implementation.)
        expected_props = {"src": url, "alt": alt}
        expected = LeafNode("img", "", props=expected_props)
        self.assertEqual(result, expected)

    def test_invalid_text_type_raises_value_error(self):
        # If text_type is not in TextType, it should hit the default and raise
        tn1 = TextNode("oops", None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn1)

        # Even an unknown enum‐like string (not a TextType) should raise
        tn2 = TextNode("oops", "SOMETHING_ELSE")
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn2)


if __name__ == "__main__":
    unittest.main()