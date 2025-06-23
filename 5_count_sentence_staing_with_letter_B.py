text = "Birds are living things"
sentences = text.split('.')
count = 0
for sentence in sentences:
    sentence = sentence.strip()  # Remove leading/trailing spaces
    if sentence and sentence[0].lower() == 'b':
        count += 1
print("Number of sentences starting with 'B':", count)
