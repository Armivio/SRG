### For now, this code does not allow multiple levels of nesting. A different strategy should be 
# used, with queues. Idea: When encountering a new symbol, put the symbol in a queue and the 
# nodes into a list ish corresponding to that specific type. 

from textnode import *

def split_one_node(node, delimiter, text_type):
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
    return old_nodes