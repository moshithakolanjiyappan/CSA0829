s1 = "what"
s2 = "watch"
matches = sum(c1 == c2 for c1, c2 in zip(s1, s2))
print(matches)
