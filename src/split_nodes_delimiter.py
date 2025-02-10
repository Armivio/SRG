### For now, this code does not allow multiple levels of nesting. A different strategy should be 
# used, with queues. Idea: When encountering a new symbol, put the symbol in a queue and the 
# nodes into a list ish corresponding to that specific type. 

from textnode import *
from extractors import extract_markdown_images, extract_markdown_links

def split_one_node(node, delimiter, text_type):
    if len(node.text) == 0:
        return []
    if node.text_type == TextType.IMAGE or node.text_type == TextType.LINK:
        return [node]
    if node.text.count(delimiter) % 2: # if the number of delimiters is odd, e.g. we only have *this
        raise Exception(f"Invalid Markdown Syntax with delimiter {delimiter}")
    # we distinguish 4 cases: *text*, *tex*t, t*ext*, t*ex*t
    # imp. cases: ** ? *
    if node.text.count(delimiter) == 0: # if there are no delimiters, job is finished
        return [node]
    first_split = node.text.split(delimiter, maxsplit=1)
    if (len(first_split) == 1): # delimiter at beginning
        second_split = first_split[0].split(delimiter, maxsplit=1)
        if (len(second_split) == 1): # case 1
            return [TextNode(second_split[0], text_type)]
        else: # case 2
            return [TextNode(second_split[0], text_type), TextNode(second_split[1], node.text_type)]
    else: # len is 2, 
        second_split = first_split[1].split(delimiter, maxsplit=1)
        if (len(second_split) == 1): # case 3
            return [TextNode(first_split[0], node.text_type), TextNode(second_split[0], text_type)]
        else: # case 4
            return [TextNode(first_split[0], node.text_type), TextNode(second_split[0], text_type), TextNode(second_split[1], node.text_type)]

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_one_node(node, delimiter, text_type))
    if len(old_nodes) != len(new_nodes):
        return split_nodes_delimiter(new_nodes, delimiter, text_type)
    return new_nodes

def split_one_node_image(node):
    if len(node.text) == 0:
        return []
    image_tuples = extract_markdown_images(node.text)
    if len(image_tuples) == 0: 
        return [node]
    current_text = node.text
    item = image_tuples[0] # (alt, url)
    alt = item[0]
    url = item[1]
    pattern = f"![{alt}]({url})"
    splitted = current_text.split(pattern, maxsplit=1)
    start_point = current_text.find(pattern)
    # cases: p, pt, tp, tpt
    match len(splitted):
        case 0: # case p
            return [TextNode(alt, TextType.IMAGE, url)]
        case 1:
            if start_point == 0: # case pt
                return split_nodes_image([TextNode(alt, TextType.IMAGE, url), TextNode(splitted[0], TextType.TEXT)])
            else: # case tp
                return split_nodes_image([TextNode(splitted[0], TextType.TEXT), TextNode(alt, TextType.IMAGE, url)])
        case 2: # case tpt
            return split_nodes_image([TextNode(splitted[0], TextType.TEXT), TextNode(alt, TextType.IMAGE, url), TextNode(splitted[1], TextType.TEXT)])
        case _:
            raise Exception("Something went wrong in the image splitting")
        

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_one_node_image(node))
    if len(old_nodes) != len(new_nodes):
        return split_nodes_image(new_nodes)
    return new_nodes


def split_one_node_link(node):
    if len(node.text) == 0:
        return []
    link_tuples = extract_markdown_links(node.text)
    if len(link_tuples) == 0: 
        return [node]
    current_text = node.text
    item = link_tuples[0] # (alt, url)
    alt = item[0]
    url = item[1]
    pattern = f"[{alt}]({url})"
    splitted = current_text.split(pattern, maxsplit=1)
    start_point = current_text.find(pattern)
    # cases: p, pt, tp, tpt
    match len(splitted):
        case 0: # case p
            return [TextNode(alt, TextType.LINK, url)]
        case 1:
            if start_point == 0: # case pt
                return split_nodes_link([TextNode(alt, TextType.LINK, url), TextNode(splitted[0], TextType.TEXT)])
            else: # case tp
                return split_nodes_link([TextNode(splitted[0], TextType.TEXT), TextNode(alt, TextType.LINK, url)])
        case 2: # case tpt
            return split_nodes_link([TextNode(splitted[0], TextType.TEXT), TextNode(alt, TextType.LINK, url), TextNode(splitted[1], TextType.TEXT)])
        case _:
            raise Exception("Something went wrong in the link splitting")
        

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_one_node_link(node))
    if len(old_nodes) != len(new_nodes):
        return split_nodes_link(new_nodes)
    return new_nodes
