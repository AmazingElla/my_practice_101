def create_username(username):
    if not isinstance(username, str):
        return "Username must be a string"
    if username == "":
        return "Username cannot be empty"
    if " " in username:
        return "Username cannot contain spaces"
    return f"Username: {username}"

print(create_username("Ella123***"))
'''
Write a function called create_username(username) with these rules:
1. If username is not a string, return "Username must be a string".
2. If it's empty, return "Username cannot be empty".
3. If it contains a space, return "Username cannot contain spaces".
4. If it passes all checks, return "Username: " followed by the username.
'''