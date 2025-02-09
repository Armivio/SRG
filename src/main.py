from textnode import *

def main():
    test_node = TextNode("This is a test node", TextType.BOLD, "https://boot.dev")
    print(test_node.__repr__())


if __name__ == "__main__":
    main()