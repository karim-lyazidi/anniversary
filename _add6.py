extra6 = [
    "how you make me feel seen even on the most invisible days",
    "the way your hand fits in mine like it was made for it",
    "how every song sounds softer when you're next to me",
    "the way you look at our future like it's already ours",
    "how your voice is the first thing I want to hear in the morning",
    "the quiet, unshakable certainty that you are it for me"
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert right before "];\n\nconst THINGS_PER_PAGE"
needle = "];\n\nconst THINGS_PER_PAGE"
end_idx = content.find(needle)

# Build new lines
esc = [f'"{x}"' for x in extra6]
insert_str = ",\n    " + ", ".join(esc) + "\n"

new_content = content[:end_idx] + insert_str + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Inserted {len(extra6)} new entries")
print("Done")
