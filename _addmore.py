extra = [
    "the way your fingers drum on the table when you're thinking", "how you argue gently with your mom on video calls", "when you try to speak arabic phrases you just learned and laugh",
    "the way you look in my hoodie with the sleeves rolled way past your wrists", "how you save songs and tag me in them days later", "when you look at a menu for 10 minutes then order the same thing",
    "how you leave me the window cracked because you know I love the cold air", "the way you text me the moment something bad happens before anyone else", "how you get shy about small injustices and care deeply",
    "when you cry at the end of every Pixar films", "the way you organise books by their covers sometimes", "how you make the whole room lighter just being in",
    "the way you take photos of the sky every time you the rainbow", "the way you hold my arm tighter when we past a stranger", "how you flowers when we window shopping plan imaginary together",
    "when you're feeling down tell me anyway even though you don't want to burden me", "the way you pronounce my name differently when you're being sweet", "the way you smile at your phone when you're texting me",
    "how you save pressed flowers in books and forget them months later", "the way you use my name more than necessary in sentences", "the way you curl up smaller when you watch horror movies",
    "how you about the little achievements as if they're huge, celebrate mine", "how you me water me when I'm working long hours", "the way you look when you first wake up - all soft and sleepy",
    "how you about my laugh at all, the corny puns even they're not", "the way you hold grudges against anyone never ever", "how you make me believe I'm a good person even on days I don't feel like one"
]

# Remove entries that don't make sense. Let me just write proper ones:

better_extra = [
    "the way you drum your fingers on the table when you're thinking",
    "how you laugh gently with your mom on video calls",
    "when you try out Arabic phrases you just learned and then laugh at yourself",
    "the way you look in my hoodie with the sleeves rolled way past your wrists",
    "how you save songs and tag me in them days later when they come on",
    "when you look at a menu for 10 minutes then order the exact same thing",
    "how you leave the car window cracked because you know I love cold air",
    "the way you text me the moment something bad happens before anyone else",
    "how you care about small injustices and feel them deeply",
    "when you cry at the end of every Pixar film no matter how many times you've seen it",
    "the way you sometimes judge books by their covers and admit it shyly",
    "how you make a whole room lighter just by being in it",
    "the way you take photos of the sky every time there's a rainbow",
    "the way you hold my arm tighter when we walk past a stranger",
    "how you plan imaginary homes together when we're window shopping",
    "when you're feeling down you tell me anyway even though you don't want to burden me",
    "the way you pronounce my name differently when you're being extra sweet",
    "the way you smile at your phone when you're texting me",
    "how you save pressed flowers in books and forget about them for months",
    "the way you use my name more than necessary in sentences",
    "the way you curl up smaller when you watch horror movies",
    "the way you celebrate my tiny little achievements as if they're huge",
    "how you bring me water when I'm working long hours without being asked",
    "the way you look when you first wake up — all soft and sleepy",
    "how you laugh at all my corny puns even when they're not funny",
    "the way you hold grudges against literally no one ever",
    "how you make me believe I'm a good person even on days I don't feel like one"
]

print(f"Extra count: {len(better_extra)}")

# Now insert into HTML
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find things array
import re

# Parse current things array
start = content.find('const things = [') + len('const things = [')
end = content.find('];\n\nconst THINGS_PER_PAGE')
arr_text = content[start:end]

# Count current entries
current_entries = [l.strip().rstrip(',') for l in arr_text.split('\n') if l.strip().startswith('"')]
print(f"Current: {len(current_entries)}")

# Need 365 total
need = 365 - len(current_entries)
print(f"Need: {need}")

# Replace the closing section - insert extra before the end
if need > 0:
    to_add = better_extra[:need]
    # Build new lines
    new_lines = []
    for i in range(0, len(to_add), 3):
        group = to_add[i:i+3]
        esc = [f'"{x}"' for x in group]
        new_lines.append("    " + ", ".join(esc) + ",")
    insert_text = "\n".join(new_lines) + "\n"
    # Insert before ]
    arr_end = content.rfind('\n', start, end)
    new_content = content[:arr_end] + "\n" + insert_text + content[arr_end:end] + content[end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Added: {len(to_add)} entries")
else:
    print("No additions needed")

# Re-verify
with open('index.html', 'r', encoding='utf-8') as f:
    content2 = f.read()
start2 = content2.find('const things = [') + len('const things = [')
end2 = content2.find('];\n\nconst THINGS_PER_PAGE')
arr_text2 = content2[start2:end2]
entries = [l.strip().rstrip(',') for l in arr_text2.split('\n') if l.strip().startswith('"')]
print(f"Final: {len(entries)} entries")
if len(entries) >= 365:
    print("✓ SUCCESS: 365+ entries")
