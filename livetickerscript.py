#create empty list for each stock
import pandas as pd
airbus_results=[]
db_results=[]
bnp_results=[]
volk_results=[]
lor_results=[]

# how to populate the list for a day





airbus1221=pd.read_csv("/users/jorge/documents/airbus1221.csv")
airbus1221=airbus1221[airbus1221["bid"]!=0]
airbus1221=airbus1221.iloc[1::50]
airbus1221["time"]=airbus1221["time"].str.replace('20161221T', '')
airbus1221["time"]=airbus1221["time"].astype(int)
airbus1221["change"]=(airbus1221["bid"] - airbus1221["offer"].iloc[1])/ airbus1221["offer"].iloc[1] 



airbus_late=airbus1221[(airbus1221["time"]>170000) & (airbus1221["time"]<173000)]




max_late1221=airbus_late["change"].mean()


airbus_wrong=airbus1221[(airbus1221["time"]>100000) & (airbus1221["change"]<(-0.01))]
try:
    stoploss=airbus_wrong["time"].iloc[0]
except Exception:
    stoploss=0

airbus_day=airbus1221[(airbus1221["time"]>100000)]
airbusmin=airbus_day["change"].min()
airbusmax=airbus_day["change"].max()

airbus_timemin=airbus_day[airbus_day["change"]==airbusmin]
airbustimemin=airbus_timemin["time"].iloc[0]
airbus_timemax=airbus_day[airbus_day["change"]==airbusmax]
airbustimemax=airbus_timemax["time"].iloc[0]

airbus_surge=airbus1221[(airbus1221["time"]<100000) & (airbus1221["time"]>91000) & (airbus1221["change"]>0.005)]
try:
    trigger=airbus_surge["time"].iloc[0]
except Exception:
    trigger=0

try:
    trigger_change=airbus_surge["change"].iloc[0]
except Exception:
    trigger_change=0
    

    
final_results1221=[1221, trigger, trigger_change, max_late1221, stoploss, airbusmin, airbustimemin, airbusmax, airbustimemax]

airbus_results.append(final_results1221)


db1221=pd.read_csv("/users/jorge/documents/db1221.csv")
db1221=db1221[db1221["bid"]!=0]
db1221=db1221.iloc[1::50]
db1221["time"]=db1221["time"].str.replace('20161221T', '')
db1221["time"]=db1221["time"].astype(int)
db1221["change"]=(db1221["bid"] - db1221["offer"].iloc[1])/ db1221["offer"].iloc[1] 



db_late=db1221[(db1221["time"]>170000) & (db1221["time"]<173000)]




max_late1221=db_late["change"].mean()


db_wrong=db1221[(db1221["time"]>100000) & (db1221["change"]<(-0.01))]
try:
    stoploss=db_wrong["time"].iloc[0]
except Exception:
    stoploss=0

db_day=db1221[(db1221["time"]>100000)]
dbmin=db_day["change"].min()
dbmax=db_day["change"].max()

db_timemin=db_day[db_day["change"]==dbmin]
dbtimemin=db_timemin["time"].iloc[0]
db_timemax=db_day[db_day["change"]==dbmax]
dbtimemax=db_timemax["time"].iloc[0]

db_surge=db1221[(db1221["time"]<100000) & (db1221["time"]>91000) & (db1221["change"]>0.005)]
try:
    trigger=db_surge["time"].iloc[0]
except Exception:
    trigger=0

try:
    trigger_change=db_surge["change"].iloc[0]
except Exception:
    trigger_change=0
    

    
final_results1221=[1221, trigger, trigger_change, max_late1221, stoploss, dbmin, dbtimemin, dbmax, dbtimemax]

db_results.append(final_results1221)

lor1221=pd.read_csv("/users/jorge/documents/lor1221.csv")
lor1221=lor1221[lor1221["bid"]!=0]
lor1221=lor1221.iloc[1::50]
lor1221["time"]=lor1221["time"].str.replace('20161221T', '')
lor1221["time"]=lor1221["time"].astype(int)
lor1221["change"]=(lor1221["bid"] - lor1221["offer"].iloc[1])/ lor1221["offer"].iloc[1] 



lor_late=lor1221[(lor1221["time"]>170000) & (lor1221["time"]<173000)]




max_late1221=lor_late["change"].mean()


lor_wrong=lor1221[(lor1221["time"]>100000) & (lor1221["change"]<(-0.01))]
try:
    stoploss=lor_wrong["time"].iloc[0]
except Exception:
    stoploss=0

lor_day=lor1221[(lor1221["time"]>100000)]
lormin=lor_day["change"].min()
lormax=lor_day["change"].max()

lor_timemin=lor_day[lor_day["change"]==lormin]
lortimemin=lor_timemin["time"].iloc[0]
lor_timemax=lor_day[lor_day["change"]==lormax]
lortimemax=lor_timemax["time"].iloc[0]

lor_surge=lor1221[(lor1221["time"]<100000) & (lor1221["time"]>91000) & (lor1221["change"]>0.005)]
try:
    trigger=lor_surge["time"].iloc[0]
except Exception:
    trigger=0

try:
    trigger_change=lor_surge["change"].iloc[0]
except Exception:
    trigger_change=0
    

    
final_results1221=[1221, trigger, trigger_change, max_late1221, stoploss, lormin, lortimemin, lormax, lortimemax]

lor_results.append(final_results1221)



volk1221=pd.read_csv("/users/jorge/documents/volk1221.csv")
volk1221=volk1221[volk1221["bid"]!=0]
volk1221=volk1221.iloc[1::50]
volk1221["time"]=volk1221["time"].str.replace('20161221T', '')
volk1221["time"]=volk1221["time"].astype(int)
volk1221["change"]=(volk1221["bid"] - volk1221["offer"].iloc[1])/ volk1221["offer"].iloc[1] 



volk_late=volk1221[(volk1221["time"]>170000) & (volk1221["time"]<173000)]




max_late1221=volk_late["change"].mean()


volk_wrong=volk1221[(volk1221["time"]>100000) & (volk1221["change"]<(-0.01))]
try:
    stoploss=volk_wrong["time"].iloc[0]
except Exception:
    stoploss=0

volk_day=volk1221[(volk1221["time"]>100000)]
volkmin=volk_day["change"].min()
volkmax=volk_day["change"].max()

volk_timemin=volk_day[volk_day["change"]==volkmin]
volktimemin=volk_timemin["time"].iloc[0]
volk_timemax=volk_day[volk_day["change"]==volkmax]
volktimemax=volk_timemax["time"].iloc[0]

volk_surge=volk1221[(volk1221["time"]<100000) & (volk1221["time"]>91000) & (volk1221["change"]>0.005)]
try:
    trigger=volk_surge["time"].iloc[0]
except Exception:
    trigger=0

try:
    trigger_change=volk_surge["change"].iloc[0]
except Exception:
    trigger_change=0
    

    
final_results1221=[1221, trigger, trigger_change, max_late1221, stoploss, volkmin, volktimemin, volkmax, volktimemax]

volk_results.append(final_results1221)


bnp1221=pd.read_csv("/users/jorge/documents/bnp1221.csv")
bnp1221=bnp1221[bnp1221["bid"]!=0]
bnp1221=bnp1221.iloc[1::50]
bnp1221["time"]=bnp1221["time"].str.replace('20161221T', '')
bnp1221["time"]=bnp1221["time"].astype(int)
bnp1221["change"]=(bnp1221["bid"] - bnp1221["offer"].iloc[1])/ bnp1221["offer"].iloc[1] 



bnp_late=bnp1221[(bnp1221["time"]>170000) & (bnp1221["time"]<173000)]




max_late1221=bnp_late["change"].mean()


bnp_wrong=bnp1221[(bnp1221["time"]>100000) & (bnp1221["change"]<(-0.01))]
try:
    stoploss=bnp_wrong["time"].iloc[0]
except Exception:
    stoploss=0

bnp_day=bnp1221[(bnp1221["time"]>100000)]
bnpmin=bnp_day["change"].min()
bnpmax=bnp_day["change"].max()

bnp_timemin=bnp_day[bnp_day["change"]==bnpmin]
bnptimemin=bnp_timemin["time"].iloc[0]
bnp_timemax=bnp_day[bnp_day["change"]==bnpmax]
bnptimemax=bnp_timemax["time"].iloc[0]

bnp_surge=bnp1221[(bnp1221["time"]<100000) & (bnp1221["time"]>91000) & (bnp1221["change"]>0.005)]
try:
    trigger=bnp_surge["time"].iloc[0]
except Exception:
    trigger=0

try:
    trigger_change=bnp_surge["change"].iloc[0]
except Exception:
    trigger_change=0
    

    
final_results1221=[1221, trigger, trigger_change, max_late1221, stoploss, bnpmin, bnptimemin, bnpmax, bnptimemax]

bnp_results.append(final_results1221)

#create aggregated tables for company and add variables like buy, stop, gain, buylim (0.5% /1%)  and gain2 (with buylim)

airbus=pd.DataFrame(airbus_results)
airbus.columns=["date","time_ex", "change_ex", "final_mean","stop_loss", "min", "time_min", "max", "time_max"]
airbus["ganancia"]=airbus["final_mean"]-airbus["change_ex"]
n=airbus.shape[0]

buy=[]
for i in range(0,n):
    if airbus["time_ex"].iloc[i]==0:
        buy.append(0)
    else:
        buy.append(1)
airbus["BUY"]=buy
stop=[]
for i in range(0,n):
    if airbus["stop_loss"].iloc[i]==0:
        stop.append(0)
    else:
        stop.append(1)
airbus["STOP"]=stop
gain=[]
for i in range(0,n):
    if (airbus["STOP"].iloc[i]==0) & (airbus["BUY"].iloc[i]==1) :
        gain.append(airbus["ganancia"].iloc[i])
    elif (airbus["STOP"].iloc[i]==1) & (airbus["BUY"].iloc[i]==1) :
        gain.append((-1)*(airbus["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
airbus["GAIN"]=gain


cia=[]
for i in range(0,n):
    cia.append("AIRBUS")
airbus["COMPANY"]=cia    

deutsche=pd.DataFrame(db_results)
deutsche.columns=["date","time_ex", "change_ex", "final_mean","stop_loss", "min", "time_min", "max", "time_max"]

deutsche["ganancia"]=deutsche["final_mean"]-deutsche["change_ex"]
n=deutsche.shape[0]

buy=[]
for i in range(0,n):
    if deutsche["time_ex"].iloc[i]==0:
        buy.append(0)
    else:
        buy.append(1)
deutsche["BUY"]=buy
stop=[]
for i in range(0,n):
    if deutsche["stop_loss"].iloc[i]==0:
        stop.append(0)
    else:
        stop.append(1)
deutsche["STOP"]=stop
n=deutsche.shape[0]
gain=[]
for i in range(0,n):
    if (deutsche["STOP"].iloc[i]==0) & (deutsche["BUY"].iloc[i]==1):
        gain.append(deutsche["ganancia"].iloc[i])
    elif (deutsche["STOP"].iloc[i]==1) & (deutsche["BUY"].iloc[i]==1):
        gain.append((-1)*(deutsche["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
deutsche["GAIN"]=gain

cia=[]
for i in range(0,n):
    cia.append("DEUTSCHE")
deutsche["COMPANY"]=cia    

bnp=pd.DataFrame(bnp_results)
bnp.columns=["date","time_ex", "change_ex", "final_mean","stop_loss", "min", "time_min", "max", "time_max"]


bnp["ganancia"]=bnp["final_mean"]-bnp["change_ex"]
n=bnp.shape[0]

buy=[]
for i in range(0,n):
    if bnp["time_ex"].iloc[i]==0:
        buy.append(0)
    else:
        buy.append(1)
bnp["BUY"]=buy
stop=[]
for i in range(0,n):
    if bnp["stop_loss"].iloc[i]==0:
        stop.append(0)
    else:
        stop.append(1)
bnp["STOP"]=stop
n=bnp.shape[0]
gain=[]
for i in range(0,n):
    if (bnp["STOP"].iloc[i]==0) & (bnp["BUY"].iloc[i]==1):
        gain.append(bnp["ganancia"].iloc[i])
    elif (bnp["STOP"].iloc[i]==1) & (bnp["BUY"].iloc[i]==1):
        gain.append((-1)*(bnp["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
bnp["GAIN"]=gain

cia=[]
for i in range(0,n):
    cia.append("BNP")
bnp["COMPANY"]=cia    

lor=pd.DataFrame(lor_results)
lor.columns=["date","time_ex", "change_ex", "final_mean","stop_loss", "min", "time_min", "max", "time_max"]
lor["ganancia"]=lor["final_mean"]-lor["change_ex"]
n=lor.shape[0]

buy=[]
for i in range(0,n):
    if lor["time_ex"].iloc[i]==0:
        buy.append(0)
    else:
        buy.append(1)
lor["BUY"]=buy
stop=[]
for i in range(0,n):
    if lor["stop_loss"].iloc[i]==0:
        stop.append(0)
    else:
        stop.append(1)
lor["STOP"]=stop
n=lor.shape[0]
gain=[]
for i in range(0,n):
    if (lor["STOP"].iloc[i]==0) & (lor["BUY"].iloc[i]==1):
        gain.append(lor["ganancia"].iloc[i])
    elif (lor["STOP"].iloc[i]==1) & (lor["BUY"].iloc[i]==1):
        gain.append((-1)*(lor["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
lor["GAIN"]=gain
cia=[]
for i in range(0,n):
    cia.append("LOREAL")
lor["COMPANY"]=cia    


volk=pd.DataFrame(volk_results)
volk.columns=["date","time_ex", "change_ex", "final_mean","stop_loss", "min", "time_min", "max", "time_max"]
volk["ganancia"]=volk["final_mean"]-volk["change_ex"]
n=volk.shape[0]

buy=[]
for i in range(0,n):
    if volk["time_ex"].iloc[i]==0:
        buy.append(0)
    else:
        buy.append(1)
volk["BUY"]=buy
stop=[]
for i in range(0,n):
    if volk["stop_loss"].iloc[i]==0:
        stop.append(0)
    else:
        stop.append(1)
volk["STOP"]=stop
n=volk.shape[0]
gain=[]
for i in range(0,n):
    if (volk["STOP"].iloc[i]==0) & (volk["BUY"].iloc[i]==1):
        gain.append(volk["ganancia"].iloc[i])
    elif (volk["STOP"].iloc[i]==1) & (volk["BUY"].iloc[i]==1):
        gain.append((-1)*(volk["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
volk["GAIN"]=gain

cia=[]
for i in range(0,n):
    cia.append("VOLKSWAGEN")
volk["COMPANY"]=cia    



n=airbusf.shape[0]
buy=[]
for i in range(0,n):
    if (airbusf["change_ex"].iloc[i]>=0.005) & (airbusf["change_ex"].iloc[i]<0.01):
        buy.append(1)
    else:
        buy.append(0)
airbus["BUYlim"]=buy
n=airbus.shape[0]
gain=[]
for i in range(0,n):
    if (airbus["STOP"].iloc[i]==0) & (airbus["BUYlim"].iloc[i]==1):
        gain.append(airbus["ganancia"].iloc[i])
    elif (airbus["STOP"].iloc[i]==1) & (airbus["BUYlim"].iloc[i]==1):
        gain.append((-1)*(airbusf["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
airbus["GAIN2"]=gain

n=deutsche.shape[0]

buy=[]
for i in range(0,n):
    if (deutsche["change_ex"].iloc[i]>=0.005) & (deutsche["change_ex"].iloc[i]<0.01):
        buy.append(1)
    else:
        buy.append(0)
deutsche["BUYlim"]=buy

n=deutsche.shape[0]
gain=[]
for i in range(0,n):
    if (deutsche["STOP"].iloc[i]==0) & (deutsche["BUYlim"].iloc[i]==1):
        gain.append(deutsche["ganancia"].iloc[i])
    elif (deutsche["STOP"].iloc[i]==1) & (deutsche["BUYlim"].iloc[i]==1):
        gain.append((-1)*(deutsche["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
deutsche["GAIN2"]=gain

n=bnp.shape[0]

buy=[]
for i in range(0,n):
    if (bnp["change_ex"].iloc[i]>=0.005) & (bnp["change_ex"].iloc[i]<0.01):
        buy.append(1)
    else:
        buy.append(0)
bnp["BUYlim"]=buy

gain=[]
for i in range(0,n):
    if (bnp["STOP"].iloc[i]==0) & (bnp["BUYlim"].iloc[i]==1):
        gain.append(bnp["ganancia"].iloc[i])
    elif (bnp["STOP"].iloc[i]==1) & (bnp["BUYlim"].iloc[i]==1):
        gain.append((-1)*(bnp["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
bnp["GAIN2"]=gain
n=lor.shape[0]
buy=[]
for i in range(0,n):
    if (lor["change_ex"].iloc[i]>=0.005) & (bnp["change_ex"].iloc[i]<0.01):
        buy.append(1)
    else:
        buy.append(0)

lor["BUYlim"]=buy
n=lor.shape[0]
gain=[]
for i in range(0,n):
    if (lor["STOP"].iloc[i]==0) & (lor["BUYlim"].iloc[i]==1):
        gain.append(lor["ganancia"].iloc[i])
    elif (lor["STOP"].iloc[i]==1) & (lor["BUYlim"].iloc[i]==1):
        gain.append((-1)*(lor["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
lor["GAIN2"]=gain

n=volk.shape[0]

buy=[]
for i in range(0,n):
    if (volk["change_ex"].iloc[i]>=0.005) & (volk["change_ex"].iloc[i]<0.01):
        buy.append(1)
    else:
        buy.append(0)


volk["BUYlim"]=buy
gain=[]
for i in range(0,n):
    if (volk["STOP"].iloc[i]==0) & (volk["BUYlim"].iloc[i]==1):
        gain.append(volk["ganancia"].iloc[i])
    elif (volk["STOP"].iloc[i]==1) & (volk["BUYlim"].iloc[i]==1):
        gain.append((-1)*(volk["change_ex"].iloc[i]+0.01))
    else:
        gain.append(0)
  
volk["GAIN2"]=gain


 
# add stop win
airbus

n=airbus.shape[0]
win=[]
for i in range(0,n):
    if airbus["time_max"].iloc[i]<170000:
        win.append(airbus["GAIN"].iloc[i]) 
    elif ((airbus["max"].iloc[i])-(airbus["change_ex"].iloc[i]))>=0.02:
        win.append(0.02)
    else:
        win.append(airbus["GAIN"].iloc[i])
airbus["stop_win"]=win
n=deutsche.shape[0]
win=[]
for i in range(0,n):
    if deutsche["time_max"].iloc[i]<170000:
        win.append(deutsche["GAIN"].iloc[i]) 
    elif ((deutsche["max"].iloc[i])-(deutsche["change_ex"].iloc[i]))>=0.02:
        win.append(0.02)
    else:
        win.append(deutsche["GAIN"].iloc[i])
deutsche["stop_win"]=win
n=lor.shape[0]
win=[]
for i in range(0,n):
    if lor["time_max"].iloc[i]<170000:
        win.append(lor["GAIN"].iloc[i]) 
    elif ((lor["max"].iloc[i])-(lor["change_ex"].iloc[i]))>=0.02:
        win.append(0.02)
    else:
        win.append(lor["GAIN"].iloc[i])
lor["stop_win"]=win
n=bnp.shape[0]
win=[]
for i in range(0,n):
    if bnp["time_max"].iloc[i]<170000:
        win.append(bnp["GAIN"].iloc[i]) 
    elif ((bnp["max"].iloc[i])-(bnp["change_ex"].iloc[i]))>=0.02:
        win.append(0.02)
    else:
        win.append(bnp["GAIN"].iloc[i])
bnp["stop_win"]=win
n=volk.shape[0]
win=[]
for i in range(0,n):
    if volk["time_max"].iloc[i]<170000:
        win.append(volk["GAIN"].iloc[i]) 
    elif ((volk["max"].iloc[i])-(volk["change_ex"].iloc[i]))>=0.02:
        win.append(0.02)
    else:
        win.append(volk["GAIN"].iloc[i])
volk["stop_win"]=win
        
#print results 
print(airbus["stop_win"].sum())
print(deutsche["stop_win"].sum())
print(bnp["stop_win"].sum())
print(lor["stop_win"].sum())
print(volk["stop_win"].sum())

print(airbus["GAIN"].sum())
print(deutsche["GAIN"].sum())
print(bnp["GAIN"].sum())
print(lor["GAIN"].sum())
print(volk["GAIN"].sum())

print(airbus["GAIN2"].sum())
print(deutsche["GAIN2"].sum())
print(bnp["GAIN2"].sum())
print(lor["GAIN2"].sum())
print(volk["GAIN2"].sum())

#save files
airbus.to_csv("airbusB11051221.csv")
deutsche.to_csv("deutscheB11141221.csv")
bnp.to_csv("bnpB11141221.csv")
lor.to_csv("lorB11141221.csv")
volk.to_csv("volkB11141221.csv")

#compare to regular shareholder
#load loreal data from yahoo finance
lormc=pd.read_csv("/users/jorge/downloads/lormc.csv")

#adjust for date
lormc["Date"] = pd.to_datetime(lormc["Date"],format='%Y-%m-%d')
n=lormc.shape[0]
difflor=lormc["Close"].iloc[0]-lormc["Open"].iloc[n]

#compare with our models
print(lor["GAIN"].sum(), difflor)

