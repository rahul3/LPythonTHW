# #imports argv from sys module
# from sys import argv
#
# #script and filename are variables assigned to the first two arguments after "python3.6"
# script, filename = argv
#
# #opens the file assigned to filename and stores the path etc. in the object text
# txt = open(filename)
#
# #prints the name of the file we just entered
# print(f"Here is your file {filename}")
# #reads the file as the path is in txt
# print(txt.read())
#
# #then type the filename again printed on the screen
# print("Type the filename again")
# #file_again is just to ask us to type the name of the file again or a different file and use the > to look like a prompt
# file_again = input("> ")
#
# #txt_again is the variable of the new file or same file again
# txt_again = open(file_again)
# #read the filename
# print(txt_again.read())


filename = input("Enter your filename")
txt = open(filename)
txt.open(filename)
print(f"Here is your file {filename} \n",txt.read())

file_again = input("Type the file name again:\n> ")
txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()
