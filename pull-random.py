# -*- coding: utf-8 -*-
"""
Created 18 December 2025
@author SarahLawsky
"""

import json
import random

with open('irc_text_list.json', 'r', encoding='utf8') as fp:
    codestring = fp.read()
    code_list = json.loads(codestring)

def format_for_display(text, width=20):
    lines = []
    words = text.split()
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += word + " "
        else:
            lines.append(current_line.ljust(width))
            current_line = word + " "
    
    if current_line:
        lines.append(current_line.ljust(width))
    
    return lines

def formatted_section():
    content = random.choice(code_list)
    lines = format_for_display(content)
    for line in lines:
        print(f"{line}")

formatted_section()
