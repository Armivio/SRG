import os
from textnode import *
from recursive_public_generator import recursive_public_generator
from generate_page import generate_page

def main():
    # test_node = TextNode("This is a test node", TextType.BOLD, "https://boot.dev")
    # print(test_node.__repr__())
    main_dir = os.getcwd()
    recursive_public_generator(main_dir)
    generate_page(os.path.join(main_dir, "content/index.md"), os.path.join(main_dir, "template.html"), os.path.join(main_dir, "public/index.html"))


if __name__ == "__main__":
    main()