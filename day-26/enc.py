class ProfileStatus:
    def __init__(self):
        self._foryou =''
        self._forconnection = ''
        self.foreveryone =''

    def get_url(self):
        return self.__foryou

    def set_url(self,url):
        self.__foryou = url

    @property
    def giveaccess(self):
        return self._forconnection

    @giveaccess.setter
    def giveaacess(self,url):
        self._forconnection = url 


user = ProfileStatus()

print("Before update: ",user.foreveryone)
user.foreveryone = "pyton.png"
print("After update: ",user.foreveryone)

print("Before update:",user.get_url())
user.set_url("Functions.py")
print("after.update",user.get_url())

print("Before update:",user.giveaccess)
user.foreveryone = "java.png"
print("after.update",user.giveaccess)
