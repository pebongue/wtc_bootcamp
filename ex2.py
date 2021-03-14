#Ask user for their username and password
username = input("Type in your username :")
password = input("Type in your password :")

if password == "LearningPythonIsFun":
    print("Hello {}! Correct password, ACCESS GRANTED!".format(username))
else:
    print("Hello {}! Incorrect password, ACCESS DENIED!".format(username))