#rm raiz-t.dat
for i in $(LANG=en_US seq 0 0.01 1); do echo "$i 1e-12" | ./bissecao | tail --lines=1 | awk '{print $2}' | echo "$i $(cat -)" >> raiz-t.dat; done
