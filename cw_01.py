#!/bin/bash

#make new directory
mkdir testfiles
#new testfiles directory
cd testfiles
#files 1-100
touch file{001..100}.tmp
cd/
exit 0

###
# INSTRUCTOR COMMENTS:
# The file name should end in .sh not .py for a Bash SHell file.
# The second to last line should be "cd -", which changes back to the last
# working directory.  Alternatively, you could define a variable at the
# beginning "CWD=$(pwd)" that contains the current working directory, then
# at the end change back to it: "cd $CWD"
###
