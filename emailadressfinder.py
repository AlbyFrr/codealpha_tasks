import re

infile = "input.txt"
outfile = "emails.txt"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

with open(infile, "r") as f:
    text = f.read()

emails = re.findall(pattern, text)

with open(outfile, "w") as f:
    for email in set(emails):
        f.write(email + "\n")
