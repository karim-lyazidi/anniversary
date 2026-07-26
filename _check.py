with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const things = [') + len('const things = [')
end = content.find('];', start)
arr_text = content[start:end]

import re
entries = re.findall(r'"[^"]*"', arr_text)
print(f'Things count: {len(entries)}')

# Better: count lines starting with quotes
lines_with_quotes = re.findall(r'^\s*"', arr_text, re.MULTILINE)
print(f'Lines starting with quote: {len(lines_with_quotes)}')

actual = [l.strip() for l in arr_text.split('\n') if l.strip().startswith('"')]
print(f'Actual entries: {len(actual)}')

if len(actual) >= 365:
    print('PASS: Enough entries')
else:
    print(f'Need: {365 - len(actual)}')
