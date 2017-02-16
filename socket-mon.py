import psutil
from collections import Counter
from operator import itemgetter, attrgetter
pids=psutil.net_connections()
spf = sorted(pids, key=lambda pids: pids[6])
print("pid,","laddr,","raddr,","status")
cl=[]
dr={}
j=0;
for i in spf:
    if( i[3] != () ):
        if( i[4] != () ):
            cli=[]
            cli.append(i[6])
            laddr=str(i[3][0]+'@'+str(i[3][1]))
            cli.append(laddr)
            raddr = str(i[4][0] + '@' + str(i[4][1]))
            cli.append(raddr)
            cli.append(i[5])
            cl.append(cli)
            if(i[6] in dr):
                dr[i[6]]+=1;
            else:
                dr[i[6]]=1;



for b in cl:
    b.append(dr.get(b[0]))

sorted_bi = sorted(dr.items(),key=itemgetter(1),reverse=True)

for c in sorted_bi:
    for d in cl:
        if(c[0]==d[0]):
            print(d[0],",",d[1],",",d[2],",",d[3])