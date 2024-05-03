class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError(None)

    def props_to_html(self):
        if self.props != None:
            rivi = ""
            for x,y in self.props.items():
                rivi += f' {x}="{y}"'
            return rivi
        else:
            return ""
        
    
    def __repr__(self):
        teksti =  f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return teksti