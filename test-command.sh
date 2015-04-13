killid[0]=1
killid[1]=2
killid[2]=3
killid[3]=6
killid[4]=9
killid[5]=14
killid[6]=15

killname[0]="HUP"
killname[1]="INT"
killname[2]="QUIT"
killname[3]="ABRT"
killname[4]="KILL"
killname[5]="ALRM"
killname[6]="TERM"

for (( i = 0 ; i < ${#killid[@]} ; i++ ))
do
    python $1&
    pid=$!
    sleep 2
    echo -n "Killing with "
    echo ${killname[$i]}
    kill -${killid[$i]} $pid
    sleep 2
    kill -9 $pid
    echo
done
