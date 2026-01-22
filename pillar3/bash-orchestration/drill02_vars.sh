
#!usr/bin/env bash

#Variables & quoting

# Goal 
# Understand variable assignment and safe expansion.

# Tasks
# - Define three variables: `A=hello`, `B="hello world"`, `C=""`
# - Print them with and without quotes
# - Observe the differences

# Outcome
# - You know when and why to quote variables
# - You avoid word-splitting bugs

A=hello
B="hello world"
C=""

echo A=$A 
echo B=$B 
echo C=$C 

echo "A=$A"
echo "B=$B" 
echo "C=$C" 

# Rule: allways quote VARIABLES unless you explicitly want splitting