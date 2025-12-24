import re
import json

with open('irc_text_list.json', 'r', encoding='utf8') as fp:
    all_sections = json.load(fp)

# Remove repealed sections
code_list = [section for section in all_sections if not section.startswith('[')]

def extract_section_number(text):
    # Match: number, space, number, period, capital letters, period
    
    match = re.match(r'(§\s*\d+[A-Z]*\.)', text)
    if match:
        return match.group(1).strip()
    return "Unknown Section"

# Preprocess sections
processed_sections = []
for section in code_list:
    title = extract_section_number(section)
    processed_sections.append({
        'title': title,
        'text': section
    })

with open('irc_text_list_with_titles.json', 'w', encoding='utf8') as fp:
        json.dump(processed_sections, fp, ensure_ascii=False)
        print("Write successful")

