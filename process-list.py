import json
import re

with open('irc_text_list.json', 'r', encoding='utf8') as fp:
    code_list = json.load(fp)
    
def extract_section_number(text):
    # Match: number, space, number, period, capital letters, period
    match = re.match(r'(§\s*\d+[A-Z]*\.[A-Z\s\-\d]*?)(?=\n|[^A-Z\s\-\d])', text)
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


