import re

def text_to_blocks(text):
    blocks = re.split(r'\n\s*\n', text)
    blocks = [block for block in blocks if block]
    return blocks

def block_to_block_type(block):
    # check if paragraph
    count = 0
    while (block[count] == '#'):
        count += 1
    if block[count] == ' ':
        return f"h{count}"
    
    # check if code
    if block[0] == block[1] == block[2] == block[-1] == block[-2] == block[-3] == '`':
        return "code"
    
     # check if quote
    if (block[0] == '>'):
        splitted = block.split('\n')
        is_quote = True
        for row in splitted:
            if not row[0] == '>':
                is_quote = False
        if is_quote:
            return "blockquote"
    
    # check if unordered list
    if (block[0] == '*' or block[0] == '-') and block[1] == ' ':
        splitted = block.split('\n')
        is_unordered_list = True
        for row in splitted:
            if not ( (row[0] == '*' or row[0] == '-') and row[1] == ' '):
                is_unordered_list = False
        if is_unordered_list:
            return "ul"
    

    # check if ordered list
    if (block[0] == '1') and block[1] == '.' and block[2] == ' ':
        splitted = block.split('\n')
        is_ordered_list = True
        for row in range(0,len(splitted)):
            if not (splitted[row][0] == f'{row + 1}' and splitted[row][1] == '.' and splitted[row][2] == ' '):
                is_ordered_list = False
        if is_ordered_list:
            return "ol"
        
    # normal paragraph
    return "p"
    

