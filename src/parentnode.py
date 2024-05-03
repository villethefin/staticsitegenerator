from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):

        if self.tag == None:
            raise ValueError("Tag not given")
        if self.children == None:
            raise ValueError("Leaf node must have a non-empty value")
        

        outputString = f'<{self.tag}>'
        for node in self.children:
            outputString += node.to_html()
        return outputString + f'</{self.tag}>'