import hashlib

def findMatch(username, password):
    f = open("users.csv", "r")
    s = f.read().strip().split("\r\n")
    f.close()
    for line in s:
        l = line.split(",")
        if username == l[0]:
            if hashlib.sha224(password).hexdigest() == l[1]:
                return "complete"
            else:
                return "username"
    return "nothing"

def login(username, password):
    s = findMatch(username, password)
    if s == "complete":
        return "successful login"
    else:
        return "login failed"

def register(username, password):
    s = findMatch(username, password)
    if s == "complete" | s == "username":
        return "someone else has this username"
    else:
        f = open("users.csv", "w")
        new_password = hashlib.sha224(password).hexdigest()
        f.write(username + "," + new_password + "\n")
        return "new account registered"
        
register("issac", "kim")