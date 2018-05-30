#!/bin/bash

cat ./bin/out-* | grep seconds | sed 's/[a-z A-Z =]\+//g' | sort -rn

