from RPLCD.i2c import CharLCD
import json
import random
import time

# Load preprocessed IRC sections
with open('Code26Dictionary.json', 'r', encoding='utf8') as fp:
    code_dict = json.load(fp)
    
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

lcd_bottom = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)
lcd_top = CharLCD(i2c_expander='PCF8574', address=0x26, port=1, cols=20, rows=4, dotsize=8)

def make_greeting():
    lcd_top.clear()
    lcd_bottom.clear()
    lines = ["HELLO CODE", "a random walk", "through U.S. tax law"]
    for row, text in enumerate(lines):
        lcd_top.cursor_pos = (row, (20 - len(text)) // 2)
        lcd_top.write_string(text)
    time.sleep(5)

make_greeting()
time.sleep(5)
    
# Fixed: use code_dict instead of code_list and div_library
current_section_number = random.choice(list(code_dict.keys()))
current_section_lines = format_for_display(code_dict[current_section_number])
section_position = 0

lcd_top.clear()
display_text = f"26 U.S.C. {current_section_number}"
lcd_top.cursor_pos = (1, (20 - len(display_text)) // 2)
lcd_top.write_string(display_text)
start_time = time.time()    

while True:
    # Bottom screen: scrolling section text
    lcd_bottom.clear()
    for row in range(4):
        if section_position + row < len(current_section_lines):
            lcd_bottom.cursor_pos = (row, 0)
            lcd_bottom.write_string(current_section_lines[section_position + row])
    
    section_position += 1
    time.sleep(1.5)
    
    # Check if section finished
    if section_position >= len(current_section_lines):
        end_time = time.time()
        total_time = int(end_time - start_time)
        display_time_text = f"{total_time} seconds"
        lcd_top.cursor_pos = (2, (20 - len(display_time_text)) // 2)
        lcd_top.write_string(display_time_text)
        time.sleep(5)
        
        # sometimes throw up the greeting again, but for shorter
        if random.randint(1, 20) == 20:
            make_greeting()
        
        # start new code section - Fixed variable names
        current_section_number = random.choice(list(code_dict.keys()))
        current_section_lines = format_for_display(code_dict[current_section_number])
        section_position = 0
        
        # Top screen: static display - only update on new section
        lcd_top.clear()
        display_text = f"26 U.S.C. {current_section_number}"
        lcd_top.cursor_pos = (1, (20 - len(display_text)) // 2)
        lcd_top.write_string(display_text)
        start_time = time.time()
