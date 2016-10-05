import hashlib

def findMatch(username, password):
    f = open("data/users.csv", "r")
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
    if s == "complete" or s == "username":
        return "someone else has this username"
    else:
        r = open("data/users.csv", "r")
        s = r.read()
        r.close()
        f = open("data/users.csv", "w")
        new_password = hashlib.sha224(password).hexdigest()
        f.write(s + username + "," + new_password + "\n")
        f.close()
        return "new account registered"
        

