from RPLCD.i2c import CharLCD
import json
import random
import time

# Load preprocessed IRC sections
with open('irc_text_list_with_titles.json', 'r', encoding='utf8') as fp:
    code_list = json.load(fp)
    
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

lcd_top = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)
lcd_bottom = CharLCD(i2c_expander='PCF8574', address=0x26, port=1, cols=20, rows=4, dotsize=8)

lcd_top.clear()
lcd_bottom.clear()
display_text = "HELLO CODE"
lcd_top.cursor_pos = (1, (20 - len(display_text)) // 2)  # Row 1, centered
lcd_top.write_string(display_text)

time.sleep(10)

current_section_lines = []
current_section_number = ""
section_position = 0

while True:
    # Get new section when current one is done
    if section_position >= len(current_section_lines):
        content = random.choice(code_list)
        current_section_number = content['title']  # Just the § number
        current_section_lines = format_for_display(content['text'])
        section_position = 0
        
        # Top screen: static display - only update on new section
        lcd_top.clear()
        display_text = f"26 U.S.C. {current_section_number}"
        lcd_top.cursor_pos = (1, (20 - len(display_text)) // 2)  # Row 1, centered
        lcd_top.write_string(display_text)
    
    # Bottom screen: scrolling section text
    lcd_bottom.clear()
    for row in range(4):
        if section_position + row < len(current_section_lines):
            lcd_bottom.cursor_pos = (row, 0)
            lcd_bottom.write_string(current_section_lines[section_position + row])
    
    section_position += 1
    time.sleep(1)
