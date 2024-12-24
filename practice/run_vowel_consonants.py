text = "How many vowels and consonants are in this sentence?"
text = text.lower()

def vowel_count(text_local):

    count = 0

    vowel = "aeiou"

    for i in text_local:
        if i in vowel:
            count = count + 1

    message = print(f"No. of vowels: {count}")
    return message

def consonant_count(text_local):

    nonvowel_count = 0

    consonant = "bcdfghjklmnpqrstvwxyz"
 
    for i in text_local:
        if i in consonant:
            nonvowel_count = nonvowel_count + 1

    message = print(f"No. of consonants: {nonvowel_count}")
    return message

vowel_count(text)
consonant_count(text)