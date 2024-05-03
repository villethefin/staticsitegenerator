from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        Initializes the LeafNode which does not allow children.
        :param tag: str - the tag name of the HTML element
        :param value: str - the content of the HTML element; must not be empty
        :param props: dict or None - HTML attributes as key-value pairs
        """
        if not value:
            raise ValueError("Leaf node must have a non-empty value")
        
        # Call the parent class constructor with no children allowed
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        
        if self.tag and self.value:
               
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        if self.value:
            return f"{self.value}"
        raise ValueError()