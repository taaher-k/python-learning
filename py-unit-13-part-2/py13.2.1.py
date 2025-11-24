#Create a class Gmail with login method. Create 2 different methods
#named as login(). One method should be taking username and password
#as input. Another method with password only as input.



class Gmail:
    def login(self, username=None, password=None):
        if username and password:
            print(f"Login with Username: {username}, Password: {password}")
        elif password:
            print(f"Login with Password only: {password}")
        else:
            print("Invalid login attempt")


# --- Program Execution ---
g = Gmail()

# Login with username and password
g.login("taaher", "mypassword123")

# Login with password only
g.login(password="mypassword123")
