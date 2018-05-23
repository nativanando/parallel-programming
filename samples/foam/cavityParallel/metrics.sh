#!/bin/bash

file="$1"

cut -d: -f 10,10 $file | grep ExecutionTime | sed 's/[a-z A-Z]\+//g' | cut -d= -f 1,2 | sed 's/[a-z A-Z =,]\+//g' > $file.log
