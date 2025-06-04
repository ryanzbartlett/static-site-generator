import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_missing_tag_raises_value_error(self):
        # tag is None → should raise ValueError('missing tag')
        child = LeafNode("i", "italic")
        with self.assertRaises(ValueError) as cm:
            ParentNode(None, [child]).to_html()
        self.assertEqual(str(cm.exception), "missing tag")

        # tag is empty string → also falsy
        with self.assertRaises(ValueError) as cm2:
            ParentNode("", [child]).to_html()
        self.assertEqual(str(cm2.exception), "missing tag")

    def test_to_html_missing_children_raises_value_error(self):
        # children=None → missing
        with self.assertRaises(ValueError) as cm:
            ParentNode("section", None).to_html()
        self.assertEqual(str(cm.exception), "missing children")

        # children=[] (empty list) → also falsy, so still “missing”
        with self.assertRaises(ValueError) as cm2:
            ParentNode("section", []).to_html()
        self.assertEqual(str(cm2.exception), "missing children")

    def test_to_html_multiple_sibling_children(self):
        # Two leaf nodes side by side
        child1 = LeafNode("span", "first")
        child2 = LeafNode("span", "second")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            "<div><span>first</span><span>second</span></div>"
        )

    def test_eq_and_not_eq_for_parentnode(self):
        # Build two identical trees
        leaf1 = LeafNode("span", "A")
        leaf2 = LeafNode("span", "B")
        p1 = ParentNode("ul", [leaf1, leaf2], props={"role": "list"})
        # separate instances but same structure
        l1_copy = LeafNode("span", "A")
        l2_copy = LeafNode("span", "B")
        p2 = ParentNode("ul", [l1_copy, l2_copy], props={"role": "list"})
        self.assertEqual(p1, p2)

        # Change props → no longer equal
        p3 = ParentNode("ul", [l1_copy, l2_copy], props={"role": "not-list"})
        self.assertNotEqual(p1, p3)

        # Change one child’s value → no longer equal
        l2_copy.value = "C"
        self.assertNotEqual(p1, p2)

    def test_child_not_htmlnode_raises_attribute_error(self):
        # If a “child” isn’t an HTMLNode, calling to_html() on it will raise
        parent = ParentNode("div", ["not a node"])
        with self.assertRaises(AttributeError):
            parent.to_html()


if __name__ == "__main__":
    unittest.main()
