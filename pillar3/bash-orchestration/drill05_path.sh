#! usr/bin/env bash


# Deterministic path building
#
# Goal
# Build predictable filesystem paths.
#
# Task
# - Given `BASE_DIR=data/raw/comext_products`
# - Given `month=2002-01`
# - Print the full output path for `full_200201.7z`
#
# Outcome
# - Understand deterministic data layouts

# Define variables
BASE_DIR="data/raw/comext_products"
month="2002-01"

clean_month=${month//-/} # Remove dash
filename="full_${clean_month}.7z"  # Build the filename
full_path="${BASE_DIR}/${month}/${filename}"  # Join into a full path

echo "Full path: $full_path"



