s = "Saveetha School of Engineering Sample"
v = sum(ch in "aeiouAEIOU" for ch in s)
c = sum(ch.isalpha() and ch not in "aeiouAEIOU" for ch in s)
print(f"Vowels={v} Consonants={c}")
print("Vowels max" if v > c else "Consonants max" if c > v else "Equal")



