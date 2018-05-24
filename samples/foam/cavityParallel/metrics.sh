#!/bin/bash

echo "Filtering log files of openFOAM simulation..."

ls results/ | grep out > /tmp/files
cd results/
while read line; do
    progs=($line)
    cut -d: -f 10,10 ${progs[0]} | grep ExecutionTime | sed 's/[a-z A-Z]\+//g' | cut -d= -f 1,2 | sed 's/[a-z A-Z =,]\+//g' > log-${progs[0]}
    sed -i '1 i\time' log-${progs[0]}
done < /tmp/files
rm /tmp/files

echo "Finishing filter"
