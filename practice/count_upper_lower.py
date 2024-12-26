text = "This Sentence Has Mixed CASE Letters!"

upper = 0
lower = 0

for letter in text:
    if letter.isupper():
        upper += 1
    elif letter.islower():
        lower += 1

print(f"The number of uppercase letters is: {upper}")

print(f"The number of lowercase letters is: {lower}")