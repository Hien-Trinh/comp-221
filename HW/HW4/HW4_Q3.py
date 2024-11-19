import re

# Define the regular expressions
regex1 = re.compile(r"(aab|bba)*")
regex2 = re.compile(r"((aab)|(bba))*")

# Test strings to compare results
test_strings = [
    "",        # Empty string
    "aab",     # Single match
    "bba",     # Single match
    "aabaab",  # Multiple matches
    "bbaaab",  # Partial matches
    "aabbbbaab",  # Mix of matches
    "xyz",     # No match
    "aaabbb",  # Partial mismatch
]

# Apply both regexes to each string
results = {s: (bool(regex1.fullmatch(s)), bool(regex2.fullmatch(s)))
           for s in test_strings}

print(results)
