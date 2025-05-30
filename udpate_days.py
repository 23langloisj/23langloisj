from datetime import datetime

# Set your Ender Dragon kill date here:
last_kill = datetime(2025, 5, 9)

today = datetime.utcnow()
days_since = (today - last_kill).days

# Read README
with open("README.md", "r") as file:
    lines = file.readlines()

# Update the marker line
with open("README.md", "w") as file:
    for line in lines:
        if "<!--DRAGON-->" in line:
            file.write("<!--DRAGON-->\n")
            file.write(f"> 🐉 It's been **{days_since} days** since I last killed the Ender Dragon.\n")
        else:
            file.write(line)
