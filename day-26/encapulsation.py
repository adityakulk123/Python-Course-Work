class Instagram:
    def __init__(self,username,password):
        self.__password = password
        self._post=[]
        self.username = username 

    def get_password(self):
        return self.__password

    def set_password(self,newpassword):
        self.__password = newpassword

    @property
    def access_post(self):
        return self.access_post

    @access_post.setter
    def access_post(self,newpost):
        self._post.append(newpost)

swathi = Instagram("swati123",'s@123')

print("Before update:",swathi.username)
swathi.username="dhanasree"
print("after update:",swathi.username)

print("Before update:",swathi.get_password())
swathi.set_password("dhana@123")
print("after update:",swathi.get_password())

print("Before update:",swathi.access_post)
swathi.access_post = "sunrise.png"
swathi.access_post = "sunset.png"
swathi.access_post = "beach.png"
print("After update:",swathi.access_post)