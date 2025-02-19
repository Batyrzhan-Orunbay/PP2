import re
pattern = r'a*b*'
test = ["a", "ab", "abb", "aab", "b", "xyz"]
for s in test:
    if re.fullmatch(pattern,s):
        print(f"Match: {s}")