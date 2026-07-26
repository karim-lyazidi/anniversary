import re
import os

file_path = 'happy_birthday_aya_final.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace base64 images with local files
pics = [
    'pic (1).jpg', 'pic (2).jpg', 'pic (3).jpg', 
    'pic (4).jpeg', 'pic (5).jpeg', 'pic (6).jpeg', 
    'pic (7).jpeg', 'pic (8).jpeg',
    'pic (1).jpeg', 'pic (2).jpeg', 'pic (3).jpeg'
]
# Repeat pics to have enough
pics = pics * 5

def replace_base64(match):
    if not pics:
        return 'src="placeholder.jpg"'
    return f'src="{pics.pop(0)}"'

# More robust regex for base64 src
content = re.sub(r'src="data:image/[^;]+;base64,[^"]+"', replace_base64, content)

# Remove portraits on Page 6
# Page 6 structure:
# <div class="page page-6" id="p6">
# ...
# <!-- portraits -->
# <div class="pol-row" style="margin-top:4px">
# ...
# </div>

portraits_pattern = r'<!-- portraits -->.*?<div class="pol-row" style="margin-top:4px">.*?</div>'
content = re.sub(portraits_pattern, '<!-- portraits removed -->', content, flags=re.DOTALL)

# Replace Arabic text
content = content.replace("Na3ch9ek 3omri", "نعشقك عمري")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done stripping base64, removing portraits, and replacing text.")
