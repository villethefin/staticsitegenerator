from leafnode import LeafNode

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, target):
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url
    
    def __repr__(self):
        teksti =  f"TextNode({self.text}, {self.text_type}, {self.url})"
        return teksti
    
    def text_node_to_html_node(self):
        if self.text_type == "text":
            self = LeafNode(None,self.text)

        if self.text_type == "bold":
            self = LeafNode("b", self.text)
        
        if self.text_type == "italic":
            self = LeafNode("i", self.text)
        
        if self.text_type == "code":
            self = LeafNode("code", self.text)
        
        if self.text_type == "link":
            self = LeafNode("a", self.text, {"href":self.url})
        
        if self.text_type == "image":
            self = LeafNode("img", "", {"src":self.url, "alt":self.text})

        raise Exception("texttype not found")
            