import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = LeafNode("h1", "bold", {"href": "https://www.google.com", "target": "_blank"})
        
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_to_html(self):
        node = LeafNode("h1", "bold", {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode("p", "This is a paragraph of text.")
        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        
        self.assertEqual(node2.to_html(), '<p>This is a paragraph of text.</p>')
    def test_to_html2(self):

        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        
        self.assertEqual(node3.to_html(), '<a href="https://www.google.com">Click me!</a>')



if __name__ == "__main__":
    unittest.main()
