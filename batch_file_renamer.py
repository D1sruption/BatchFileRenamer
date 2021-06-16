import os
import sys

#dir_path = os.path.dirname(os.path.realpath(__file__))
#user_input = input("Enter Directory: ")
user_input = os.getcwd()
counter = 0
print("Current Working Directory: " + user_input)
path = os.listdir(user_input)
#exists = os.path.exists(user_input)
#print("exists?: ",exists)

files = os.listdir(user_input)

def printFiles():
	for filename in path:
		print(filename)

option_printfiles = raw_input("Do you want to list files in current directory(y/n): ")
if option_printfiles == "y":
	printFiles()

print(" ")
find_what = raw_input("Enter text to replace in file names: ")
replace_with = raw_input("Enter text you want to replace with: ")
print(" ")
print("========================================")
print(" ")

for filename in path:
	if filename.find(str(find_what)) == -1:
		continue
	else:
		print(filename + " ==> " + filename.replace(str(find_what), str(replace_with)))
		print(" ")
		os.rename(os.path.join(user_input, filename), os.path.join(user_input, filename.replace(str(find_what), str(replace_with))))
		counter +=1


print(" ")
print("========================================")

print(" ")
print(str(counter) + " Files Renamed!")