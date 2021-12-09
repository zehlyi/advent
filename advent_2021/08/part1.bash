c=0; for w in `cat input.txt |awk -F '|' '{print $2}'`; do if [ ${#w} -eq 2 -o ${#w} -eq 4 -o ${#w} -eq 3 -o ${#w} -eq 7 ]; then c=$((c+1)); fi; done; echo $c
