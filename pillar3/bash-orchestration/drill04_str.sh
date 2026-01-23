#! usr/bin/env bash


#  Bash string manipulation

# Goals  
# Transform strings without external tools.

# Tasks 
# - Given `current="2002-01"`
# - Convert it to `200201` using Bash only
# - Print both values

# Outcome
# - You understand parameter expansion
# - You don’t need `sed` for simple cases


# Set the environmental variable
echo "Script name: $0"
echo "DATE-TO-STRING: $1"

# Remove characters ${var//old/new}
current="$1"
current_nodash=${current//-/}

# Print solution
echo "Original: $current"
echo "No dash: $current_nodash"