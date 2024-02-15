import re

n = input().lower()

print(f'The No. of VOWELS are {len(re.findall("[aeiou]", n))}')

print()

print(f'The No. of Consonants are {len(re.findall("[^aeiou]", n))}')
