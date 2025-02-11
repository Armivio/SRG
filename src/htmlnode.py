from textnode import TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # A string representing the HTML tag name (e.g. “p”, “a”, “h1”, etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside
        # a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the
        # HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        if (value == None and children == None):
            raise Exception("value and children cannot be both None at the same time!")
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        all_props = ""
        for key in self.props:  
            all_props += f' {key}="{self.props[key]}"'
        return all_props
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node has no value!")
        if self.tag == None:
            return self.value
        
        match self.tag:
            case TextType.TEXT:
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
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not isinstance(self.children, list):
            print(f"The faulty node is: {self.__repr__()}")
            raise Exception("Somehow the children list is not a list!\nMaybe somewhere was only a node returned and not a list of nodes?")
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
            case TextType.TEXT:
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
            case "content":
                return final_value
            case _:
                return f"<{self.tag}>{final_value}</{self.tag}>"
                #raise Exception("Unexpected tag!")
            # case _ if self.tag.startswith("h") and self.tag[1:].isdigit():
                # return f"<{self.tag}>{final_value}</{self.tag}>"