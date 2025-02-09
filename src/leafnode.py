from htmlnode import HTMLNode
from textnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node has no value!")
        if self.tag == None:
            return self.value
        
        match self.tag:
            case TextType.NORMAL:
                return f"<p>{self.value}</p>"
            case TextType.BOLD:
                return f"<b>{self.value}</b>"
            case TextType.ITALIC:
                return f"<i>{self.value}</i>"
            case TextType.CODE:
                return f"<code>{self.value}</code>"
            case TextType.LINK:
                return f"<a{self.props_to_html()}>{self.value}</a>"
            case TextType.IMAGE:
                return f"<{self.props_to_html()[1:]}>"
            case _:
                raise Exception("Unexpected tag!")
        