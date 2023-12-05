
import sys 
file = open(sys.argv[1]).read().strip()
ans = 0
for line in file.split('\n'):
    digits = []
    for index, word in enumerate(line):
        if word.isdigit():
            digits.append(word)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[index:].startswith(val):
                digits.append(str(d + 1))
    score = int(digits[0] + digits[-1])
    ans += score
print(ans)
