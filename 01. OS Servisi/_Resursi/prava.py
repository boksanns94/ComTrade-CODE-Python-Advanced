import os

os.chdir("./APD/cas 1")
# print(os.getcwd())

os.chmod("./test.txt",0o777)
statinfo = os.stat("./test.txt")
print(oct(statinfo.st_mode))