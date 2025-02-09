from htmlnode import *

def text_node_to_html_node(text_node): # maybe we need self here instead of text_node
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag=TextType.BOLD, value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag=TextType.ITALIC, value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag=TextType.CODE, value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag=TextType.LINK, value=text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag=TextType.IMAGE, value="", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Unexpected tag!")
    