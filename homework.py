import pandas as pd
import statistics as st
df=pd.read_csv("StudentsPerformance.csv")
d=df["reading score"].tolist()

mean=st.mean(d)
std=st.stdev(d)
median=st.median(d)
mode=st.mode(d)

fstd_start=mean-std
fstd_end=mean+std
sstd_start=mean-2*std
sstd_end=mean+2*std
tstd_start=mean-3*std
tstd_end=mean+3*std
tlist=[]
slist=[]
flist=[]

for data in d:
    if(data>fstd_start and data<fstd_end):
        flist.append(data)
    if(data>sstd_start and data<sstd_end):
        slist.append(data)
    if(data>tstd_start and data<tstd_end):
        tlist.append(data)

fpercentage=(len(flist)/len(d))*100
print(fpercentage)
spercent=(len(slist)/len(d))*100
print(spercent)
tpercent=(len(tlist)/len(d))*100
print(tpercent)