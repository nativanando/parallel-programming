#!/bin/bash
cat ./bin/out-* | grep seconds | sed 's/[a-z A-Z =]\+//g' | sort -rn  > csv/execution-time.txt && sed -i "1s/^/execution-time\n/" csv/execution-time.txt  && \
cat ./bin/out-* | grep Total | grep process | sed 's/[a-z A-Z =]\+//g' | sort -n > csv/amount-np.txt && sed -i "1s/^/processors\n/" csv/amount-np.txt && \
cat ./bin/out-* | grep Mop/s | grep total | sed 's/[a-z A-Z = /]\+//g' | sort -n > csv/total-mops.txt && sed -i "1s/^/total-mops\n/" csv/total-mops.txt && \
cat ./bin/out-* | grep Mop/s | grep thread | sed 's/[a-z A-Z = /]\+//g' | sort -nr > csv/amount-thread-mops.txt && sed -i "1s/^/thread-mops\n/" csv/amount-thread-mops.txt
