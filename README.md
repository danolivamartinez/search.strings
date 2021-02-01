# Challenge

The program must return a list of the 100 most common three word sequences.

## Running the program

The program is based in Python. Running possibilities: 

- With arguments: ```python search.py <file01> <file02> ... <file_N>```
- With stdin: ```cat file01.txt | python search.py```

*Output example with one argument:
==== INFO: Detected 1 arguments to process
==== INFO: File scan01.txt found!
==== INFO: Running search engine
[('<pattern>', <number of iterations>]
==== INFO: All task completed

*Output example with stdin:
==== INFO: stdin input detected
==== INFO: Running search engine
[('<pattern>', <number of iterations>]
==== INFO: All task completed


## Test cases

In this repo you can find some example files:

*Short test file: file01.txt 
*Short test file: file02.txt 
*Long test file: "Origin Of Species"

## Handling Exceptionss

Running with arguments referred to missing entries: ```python search.py <missing_file>```

*Output example with stdin:
==== INFO: Detected 1 arguments to process
==== ERROR: File <missing_file> not found
==== INFO: All task completed

Running with emtpy STDIN: ```echo "" | python search.py```

*Output example with stdin:
==== ERROR: Empty stdin input

Running without STDIN or arguments: ```python search.py```

*Output example with stdin:
==== HELP: You must pass stdin or arguments. Please check this info: https://github.com/danolivamartinez/search.strings/edit/main/README.md 
