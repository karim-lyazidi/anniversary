import re

with open('happy_birthday_aya_final.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Put newlines before each page div and major sections
content = content.replace('<div class="page', '\n<div class="page')
content = content.replace('<!--', '\n<!--')
content = content.replace('</div>', '</div>\n')

with open('happy_birthday_aya_final.html', 'w', encoding='utf-8') as f:
    f.write(content)
