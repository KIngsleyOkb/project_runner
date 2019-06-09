import os
os.chdir('/home/kingsley/Desktop')

#print(os.getcwd())

dirName = input("enter your directory name: ")
os.makedirs(dirName)
os.chdir('/home/kingsley/Desktop/{}'.format(dirName))
os.system("git init")
os.system("git commit")
os.system("git add .")
os.system("code .")