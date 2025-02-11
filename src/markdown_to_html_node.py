from text_to_blocks import *
from text_to_html import text_node_to_html_node
from htmlnode import *
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from textnode import *

def line_to_children(line):
    list_of_text_nodes = text_to_textnodes(line)            
    html_list_of_line_nodes = list(map(text_node_to_html_node, list_of_text_nodes))
    return html_list_of_line_nodes

def lines_to_children(block, how_many_delete=0, is_list=False):
    lines = block.split("\n")
    children_of_parent = []
    if not is_list:
        for line in lines:
            children_of_parent.extend(line_to_children(line[how_many_delete:]))
    else:
        for line in lines:
            children_of_parent.append(ParentNode(tag="li", children=line_to_children(line[how_many_delete:])))
    return children_of_parent

def markdown_to_html_node(markdown):
    blocks = text_to_blocks(markdown)
    big_parent_children = []
    big_parent_tag = "content"
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case _ if block_type.startswith("h") and block_type[1].isdigit(): # hx case
                children_of_parent = line_to_children(block[1 + int(block_type[1]):])
            case "pre":
                children_of_parent = [LeafNode(tag=TextType.CODE, value=block[3:-3])]
            case "blockquote":
                children_of_parent = lines_to_children(block, how_many_delete=2)
            case "ul":
                children_of_parent = lines_to_children(block, how_many_delete=2, is_list=True)
            case "ol":
                children_of_parent = lines_to_children(block, how_many_delete=3, is_list=True)
            case "p":
                children_of_parent = lines_to_children(block)
            case _: 
                raise Exception("Unknown parent tag!")

        parent_tag = block_type
        parent = ParentNode(tag=parent_tag, children=children_of_parent)
        big_parent_children.append(parent)
    return ParentNode(tag=big_parent_tag, children=big_parent_children)

### !!!! also change how the to_html works for the parent nodes