from zipfile import ZipFile

print("What would you like to do?")
print("1.Print the content of zip file")
print("2.Print the contents of the zip file, and extract all the files")
print("3.Print the contents of the zip file, and extract only one file")
print("4.Print the contents of the zip file, and read the data from one file")
choice = int(input("Which of the 4 choices are you gonna chose: "))
#Sentenal value
while choice != 1 or choice != 2 or choice != 3 or choice != 4:
    print("That wasnt an option, chose again")
    choice = int(input())

file_name = input("Enter the file name, with the .zip at the end of the name: ")

#Create instance of zipfile
with ZipFile (file_name, 'r') as zip:
