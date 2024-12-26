username = input("Enter a username: ")

valid_username = {"length": False,
                  "alphanumeric": False,
                  "first_is_alpha": False
                  }

def check_username_validity(username):
    if len(username) >= 5 and len(username) <= 15:
        valid_username.update({"length": True})
    else:
        print("Invalid username: Length not between 5 and 15 characters.")
    if username.isalnum() == True:
        valid_username.update({"alphanumeric": True})
    else:
        print("Invalid username: Not alphanumeric.")
    if username[0].isalpha() == True:
        valid_username.update({"first_is_alpha": True})
    else:
        print("Invalid username: First character is not a letter.")


check_username_validity(username)

if all(value == True for value in valid_username.values()):
    print("Valid username")