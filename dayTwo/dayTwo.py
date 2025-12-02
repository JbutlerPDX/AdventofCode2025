import re


with open('invalidRanges.txt', 'r') as f:
    invalid_ranges = []
    pattern = r"^(\d+)\1+$"
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        match = re.match(r'(\d+)-(\d+)', line.strip())
        if match:
            start, end = int(match.group(1)), int(match.group(2))
        for i in range(start, end + 1):
            if re.fullmatch(pattern, str(i)):
                invalid_ranges.append(i)
print(f"Invalid numbers with consecutive digits: {invalid_ranges}")
print(f"Total sum of invalid numbers: {sum(invalid_ranges)}")


