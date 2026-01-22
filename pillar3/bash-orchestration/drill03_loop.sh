#!/usr/bin/env bash

# while loops & termination
#
# Goal
# Control repetition with conditions.
#
# Tasks
# - Write a `while` loop that prints months from `2002-01` to `2002-03`
# - Stop exactly at the end month
# - Print the current month on each iteration
#
# Outcome
# - You can reason about loop start/stop conditions

year=2002
month=1

while [[ $year -lt 2002 || ( $year -eq 2002 && $month -le 3 ) ]]; do
  printf "%04d-%02d\n" $year $month

  # increment month and handle year change
  if [[ $month -eq 12 ]]; then
    month=1
    ((year++))
  else
    ((month++))
  fi
done