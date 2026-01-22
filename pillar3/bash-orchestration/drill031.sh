#!/usr/bin/env bash

# Bash execution & arguments — WITH RANGE PRINTING

echo "Script name: $0"
echo "FROM: $1"
echo "TO: $2"

# Parse input
from="$1"
to="$2"

# Extract year and month
from_year=${from:0:4}
from_month=${from:5:2}
to_year=${to:0:4}
to_month=${to:5:2}

# Convert to integers (strip leading zeros)
from_month=$((10#$from_month))
to_month=$((10#$to_month))

# Initialize loop counters
year=$from_year
month=$from_month

# Loop from FROM to TO
while [[ $year -lt $to_year || ( $year -eq $to_year && $month -le $to_month ) ]]; do
  printf "%04d-%02d\n" $year $month

  if [[ $month -eq 12 ]]; then
    month=1
    ((year++))
  else
    ((month++))
  fi
done