from htmlnode import HTMLNode
from textnode import TextType
class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag present!")
        if not self.children:
            raise ValueError("It's a parent with no children!")
        if len(self.children) == 0:
            raise ValueError("It's a parent with no children!")
        final_value = ""
        for child in self.children:
            final_value += child.to_html()

        match self.tag:
            case TextType.NORMAL:
                return f"<p>{final_value}</p>"
            case TextType.BOLD:
                return f"<b>{final_value}</b>"
            case TextType.ITALIC:
                return f"<i>{final_value}</i>"
            case TextType.CODE:
                return f"<code>{final_value}</code>"
            case TextType.LINK:
                return f"<a{self.props_to_html()}>{final_value}</a>"
            case TextType.IMAGE:
                # return f"<{self.props_to_html()[1:]}>"
                raise Exception("Can images have children?")
            case _:
                raise Exception("Unexpected tag!")
        