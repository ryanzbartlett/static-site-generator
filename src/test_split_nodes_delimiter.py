import unittest
from src.split_nodes_delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        old_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)
    
    def test_split_nodes_delimiter_italic(self):
        old_nodes = [TextNode("This is _italic_ text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.ITALIC)
    
    def test_split_nodes_delimiter_code(self):
        old_nodes = [TextNode("This is `code` text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.CODE)
    
    def test_split_nodes_delimiter_multiple_occurrences(self):
        old_nodes = [TextNode("**first** and **second** bold", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "first")
        self.assertEqual(new_nodes[1].text, " and ")
        self.assertEqual(new_nodes[2].text, "second")
        self.assertEqual(new_nodes[3].text, " bold")
    
    def test_split_nodes_delimiter_no_delimiter(self):
        old_nodes = [TextNode("No delimiter here", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "No delimiter here")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
    
    def test_split_nodes_delimiter_empty_text(self):
        old_nodes = [TextNode("", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 0)
    
    def test_split_nodes_delimiter_non_text_node(self):
        old_nodes = [
            TextNode("Regular text", TextType.TEXT),
            TextNode("Already bold", TextType.BOLD)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "Regular text")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "Already bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
    
    def test_split_nodes_delimiter_invalid_delimiter(self):
        old_nodes = [TextNode("Test text", TextType.TEXT)]
        
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "@@", TextType.BOLD)
    
    def test_split_nodes_delimiter_invalid_node_type(self):
        old_nodes = ["not a TextNode"]
        
        with self.assertRaises(TypeError):
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
    
    def test_split_nodes_delimiter_consecutive_delimiters(self):
        old_nodes = [TextNode("Text **bold****more bold** text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "Text ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text, "more bold")
        self.assertEqual(new_nodes[3].text, " text")

if __name__ == '__main__':
    unittest.main()