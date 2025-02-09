import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_invalid_initialization(self):
        # Test that initializing with both value and children as None raises an exception
        with self.assertRaises(Exception):
            HTMLNode(tag="p", value=None, children=None)
            
    def test_valid_initialization_with_value(self):
        # Test initialization with a value
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def test_valid_initialization_with_children(self):
        # Test initialization with children
        child1 = HTMLNode(tag="span", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        parent = HTMLNode(tag="div", children=[child1, child2])
        
        self.assertEqual(parent.tag, "div")
        self.assertIsNone(parent.value)
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].value, "Child 1")
        self.assertEqual(parent.children[1].value, "Child 2")
        
    
   
   

if __name__ == "__main__":
    unittest.main()