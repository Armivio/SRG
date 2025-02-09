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
