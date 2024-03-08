#1
import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

#2
import os
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))

#3
import os
def check_path(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path {path} does not exist.")
path = "C:/Users/John/Documents/example.txt"
check_path(path)


#4
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("file handling.py"))


#5
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())

#6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#7
from shutil import copyfile
copyfile('Built-in functions.py', 'file handling.py')


#8
import os
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File at {path} successfully deleted")
        else:
            print(f"Permission denied to delete file at {path}")
    else:
        print(f"File at {path} does not exist")
file_path = "gh.py"
delete_file(file_path)
