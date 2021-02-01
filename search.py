import re
import sys
import os

filetext = ""

def search_function(filetext):
    print("==== INFO: Running search engine")
    match = re.findall(r'((\b.+?\b)(?:\s\2)+)',filetext,re.DOTALL)
    return [(m[1], int((len(m[0]) + 1) / (len(m[1]) + 1))) for m in match]
    textfile.close()

def argument_function(argument,stdin):
    if stdin == 1:    
        print("==== INFO: stdin input detected")
        print(search_function(argument))
    else:
        try:
            with open(argument) as textfile:
                print("==== INFO: File " + argument + " found!")
                print(search_function(textfile.read()))
        except:
            print("==== ERROR: File " + argument + " not found")
            return


# Main 
if __name__ == "__main__":  
    if sys.stdin.isatty():
        if len(sys.argv) > 1: 
            stdin = 0
            argument = sys.argv
            del argument[0]
            print("==== INFO: Detected " + str(len(argument)) + " arguments to process")
            # Call functions
            for x in range(len(argument)):
                argument_function(argument[x],stdin)
            print("==== INFO: All task completed")
        else:
            print("==== HELP: You must pass stdin or arguments. Please check this info: https://github.com/danolivamartinez/search.strings/edit/main/README.md ")
    else:
        argument = sys.stdin.read()
        # Check empty stdin
        if len(argument) > 1:
            stdin = 1
            # Call functions
            argument_function(argument,stdin)
            print("==== INFO: All task completed")
        else:
            stdin = 0
            print("==== ERROR: Empty stdin input")

    # if len(sys.argv) > 1: 
    #     stdin = 0
    #     argument = sys.argv
    #     del argument[0]
    #     print("==== INFO: Detected " + str(len(argument)) + " arguments to process")
    #     # Call functions
    #     for x in range(len(argument)):
    #         argument_function(argument[x],stdin)
    #     print("==== INFO: All task completed")
    # else:
    #     if len(sys.argv) <= 1 and not sys.stdin.isatty():
    #         print("==== INFO: help asystant")
    #         exit
    #     else:
    #         argument = sys.stdin.read()
    #         stdin = 1
    #         argument_function(argument,stdin)
    #         print("==== INFO: All task completed")

