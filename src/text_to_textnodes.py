from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import *

def text_to_textnodes(text):
    initial = TextNode(text, TextType.TEXT)
    final = split_nodes_image([initial])
    final = split_nodes_link(final)
    final = split_nodes_delimiter(final, '**', TextType.BOLD)
    final = split_nodes_delimiter(final, '*', TextType.ITALIC)
    final = split_nodes_delimiter(final, '`', TextType.CODE) 
    return final