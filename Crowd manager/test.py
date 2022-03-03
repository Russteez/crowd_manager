from itertools import combinations

letters = "GeEKS"

# size of combination is set to 3
a = combinations(letters, 3)
y = [' '.join(i) for i in a]

print(y)