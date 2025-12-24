# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 05:59:26 2022

@author: Sarah
"""
from bs4 import BeautifulSoup, Tag
import os
import re
import json
from itertools import chain

def find_the_code_section(x):
    return x.split('.', 1)[1].split('-', 1)[0]

def find_code_for_usc_26(x):
    return x.rsplit('/', 1)[1][1:].replace('\u2013', '-')

def find_the_number(x):
    try:
        return int(x)
    except:
        pattern = r"\d+\("
        match_no_letter = re.search(pattern, x)
        match = re.match(r'^\d+', x)
        if match_no_letter:
            return int(match.group()) + .1
        else:
            return int(match.group()) + .2

def create_list_from_string(stringtocheck):
    if 'all' in stringtocheck:
        return ['all']
    else:
        initial_list = stringtocheck.split(",")
        return sorted(list(set(initial_list)))

def merge_lists(listoflists):
    merged_lists = sorted(list(set(list(chain(*listoflists)))))
    if 'all' in merged_lists:
        return ['all']
    else:
        return merged_lists

def replace_with_dict(text, replace_dict):
    for key, value in replace_dict.items():
        text = re.sub(key, value, text)
    return text

def replace_in_value(text, old, new):
    return text.replace(old, new)

def createStatuteNoNotes(titlenumber):

    # URL: https://uscode.house.gov/download/download.shtml
    # when you update the code, make sure to change code_updated in functionmodules

    with open(f'usc{titlenumber}.xml', encoding='utf8') as fp:
        soup = BeautifulSoup(fp, 'xml')

    soup_str = str(soup)

# Convert the string back to a BeautifulSoup object
    soup = BeautifulSoup(soup_str, 'xml')

    to_remove = ["note", "notes", "sourceCredit"]
    for r in to_remove:
        for p in soup.find_all(r):
            p.decompose()

    div_elements = soup.find_all('section')
    div_library = {}
    for div in div_elements:

        section_number = div.num
        section_title = div.heading
        section_number_and_title = f"<section>{section_number}{section_title}</section>"
        section_number_and_title = section_number_and_title.replace(
            '\u2013', '-')

        subsection_elements = div.find_all('subsection')
        new_dict = {}
        new_dict['num_title_string'] = section_number_and_title

        if subsection_elements:
            for item in subsection_elements:
                subsection_number = item.get("identifier").rsplit('/', 1)[1]
                new_dict[subsection_number] = str(item)

        else:
            num_tag = div.find('num')
            if num_tag is not None:
                num_tag.decompose()

            heading_tag = div.find('heading')
            if heading_tag is not None:
                heading_tag.decompose()

            new_dict['all'] = str(div)

        div_library[find_code_for_usc_26(div.get("identifier"))] = new_dict


    with open(f'Code{titlenumber}Dictionary.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(json.dumps(div_library))


