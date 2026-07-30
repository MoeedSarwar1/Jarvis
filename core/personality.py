from pathlib import Path

personality = Path('./assets/prompts')
personality_files = sorted(personality.glob("**.md"))

contents = []

for item in personality_files:
    contents.append(item.read_text())

SYSTEM_PROMPTS = "\n\n".join(contents)
