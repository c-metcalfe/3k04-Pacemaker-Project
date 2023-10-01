import os

class UserClass:
    def __init__(self, user_file): # This is not the function that creates a new user, see RegisterPage.py
        # open file from Users folder named "username"
        # assign parameter values from file
        # maybe encrypt file?
        try:
            file_name = os.path.join("DCM","Users","{}.txt".format(user_file))
            f = open(file_name)
            self.file_found = True
            self.username = f.readline().rstrip()  # remove newlines from username and pw with rstrip
            self.password = f.readline().rstrip() 

            # TODO read pacemaker parameters to user attributes


        except:
            self.file_found = False
            return
    def getUsername(self):
        return self.username

