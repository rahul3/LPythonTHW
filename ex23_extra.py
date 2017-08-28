import sys

script, input_encoding, error=sys.argv

#initializing function named main passing three parameters
def main(language_file,encoding,errors):
    #storing the first line in line variable
    line = language_file.readline()
    #if the line is TRUE then print raw to cooked string. Ends when file ends
    if line:
        print_line(line, encoding,errors)
        return main(language_file,encoding,errors)

#intializing function print line with three parameters
def print_line(line,encoding,errors):
    #removes all spaces preceding and after the line
    next_lang = line.strip()
    #encodes the line with the type of "encoding" specified in function parameters and stores the errors
    raw_bytes = next_lang.encode(encoding,errors=errors)
    #decodes the line and stores it in cooked_string
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

#opneing a file with encoding specified , here it is utf-8
languages = open("languages.txt",encoding="utf-8")

#passing the languages object and input_encoding and error from command line
main(languages,input_encoding,error)
