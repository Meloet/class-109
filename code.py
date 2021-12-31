import plotly.figure_factory as ff
import statistics as st
import random

diceresult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)

mean=st.mean(diceresult)
std=st.stdev(diceresult)
median=st.median(diceresult)
mode=st.mode(diceresult)

fstd_start=mean-std
fstd_end=mean+std
sstd_start=mean-2*std
sstd_end=mean+2*std
tstd_start=mean-3*std
tstd_end=mean+3*std
tlist=[]
slist=[]
flist=[]

for data in diceresult:
    if(data>fstd_start and data<fstd_end):
        flist.append(data)
    if(data>sstd_start and data<sstd_end):
        slist.append(data)
    if(data>tstd_start and data<tstd_end):
        tlist.append(data)

fpercentage=(len(flist)/len(diceresult))*100
print(fpercentage)
spercent=(len(slist)/len(diceresult))*100
print(spercent)
tpercent=(len(tlist)/len(diceresult))*100
print(tpercent)