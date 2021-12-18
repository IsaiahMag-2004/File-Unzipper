from zipfile import ZipFile

print("What would you like to do?")
print("1.Print the content of zip file")
print("2.Print the contents of the zip file, and extract all the files")
print("3.Print the contents of the zip file, and extract only one file")
print("4.Print the contents of the zip file, and read the data from one file")
choice = int(input("Which of the 4 choices are you gonna chose: "))
file_name = input("Enter the file name, with the .zip at the end of the name: ")

#Create instance of zipfile
with ZipFile (file_name, 'r') as zip:
    if choice == 1:
        zip.printdir()
    elif choice == 2:
        #Print A table of contents for the file
        zip.printdir()

        #Extracting all the files
        print("Extracting all the files now...")
        zip.extractall()
        print("DONE!")
        print("The files have been extracted to the current working directory")