all_lines = []
current_position = 0

while True:

    if current_position + 12 >= len(all_lines):
        content = random.choice(code_list)
        new_lines = format_for_display(content)
        all_lines.extend(new_lines)
    

    display_lines = all_lines[current_position:current_position + 12]
    # ... update LCDs with display_lines ...
    
    current_position += 1
    time.sleep(1)
