from datetime import datetime

# Set your Ender Dragon kill date here:
last_kill = datetime(2025, 5, 1)

today = datetime.utcnow()
days_since = (today - last_kill).days

with open("README.md", "r") as file:
    lines = file.readlines()

with open("README.md", "w") as file:
    i = 0
    while i < len(lines):
        line = lines[i]
        if "<!--DRAGON-->" in line:
            file.write(line)  # write the <!--DRAGON--> line as-is
            i += 1  # skip the line after <!--DRAGON-->
            file.write(f"🐉 It's been **{days_since} days** since I last killed the Ender Dragon.\n")
        else:
            file.write(line)
        i += 1
