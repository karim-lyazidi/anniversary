with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract things array text
start = content.find('const things = [') + len('const things = [')
end = content.find('];\n\nconst THINGS_PER_PAGE')
arr_text = content[start:end]

# Count entries using a simple approach - each entry ends with "," or is the last one
# Count number of ," patterns then add 1 for last entry
import re

# Remove all newlines first
flat = arr_text.replace('\n', ' ').replace('\r', ' ')

# Pattern: "..." followed by comma (or end)
# Use the pattern: "[^"]*"[^"]*" - match quoted strings carefully
# Need to handle strings with escaped quotes though there shouldn't be any

# Simple count: count non-empty strings between quotes
in_quote = False
current = []
entries = []
i = 0
while i < len(flat):
    ch = flat[i]
    if ch == '"' and (i == 0 or flat[i-1] != '\\'):
        if not in_quote:
            in_quote = True
            current = []
        else:
            in_quote = False
            s = ''.join(current).strip()
            if s:
                entries.append(s)
    elif in_quote:
        current.append(ch)
    i += 1

print(f"Total entries in things array: {len(entries)}")
if len(entries) >= 365:
    print("SUCCESS - 365 or more entries")
else:
    print(f"Need {365 - len(entries)} more")
    if len(entries) > 0:
        print("Last few entries:")
        for e in entries[-5:]:
            print(f"  - {e[:60]}")
