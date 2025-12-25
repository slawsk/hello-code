# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 05:59:26 2022
@author: Sarah
"""
from bs4 import BeautifulSoup, Tag
import os
import re
import json

def createStatuteNoNotes(titlenumber):
    with open(f'usc{titlenumber}.xml', encoding='utf8') as fp:
        soup = BeautifulSoup(fp, 'xml')
    
    # Remove notes and source credits
    to_remove = ["note", "notes", "sourceCredit"]
    for r in to_remove:
        for p in soup.find_all(r):
            p.decompose()
    
    section_elements = soup.find_all('section')
    div_library = {}
    
    for section in section_elements:
        num_tag = section.find('num')
        if num_tag is not None:
            section_number = num_tag.get('value')
            
            if section_number is not None:
                print(f"Section number: {repr(section_number)}")  # Debug
                section_number = str(section_number).strip()
            num_tag.decompose()
            section_text = section.get_text(separator=' ', strip=True)
            section_text = ' '.join(section_text.split())
            
            if section_number is not None and not section_text.lower().startswith('repealed'):
                div_library[section_number] = section_text
    
    output_file = f'Code{titlenumber}Dictionary.json'
    with open(output_file, 'w', encoding='utf8') as fp:
        json.dump(div_library, fp, ensure_ascii=False, indent=2)
    
    return div_library

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <title_number>")
        sys.exit(1)
    
    title_number = sys.argv[1]
    createStatuteNoNotes(title_number)
    print(f"Successfully created Code{title_number}Dictionary.json")
