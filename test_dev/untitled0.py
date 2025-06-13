import pandas as p
import matplotlib.pyplot as m 
print("MATPLOT")
print("*******")
data = {'Patient':["John","Alice","Bob","Eve","Charlie","David","Fionna","Grace","Hannah","Ivan"],
        'Hemoglobin':[13.5,11.2,14.8,10.5,15.0,12.7,11.8,14.2,13.0,12.5],
        'Sugar':[95,180,100,190,90,110,160,105,150,170],
        'HeartRate':[72,88,75,95,70,80,85,74,78,90],
        'Pressure':[130,145,128,150,120,135,140,125,138,142],
        'Vitamin B':[450,210,480,190,500,60,220,470,330,250]}
df = p.DataFrame(data)
#print(df)

conditions = [
    df["Hemoglobin"]<12,
    df["Sugar"]>60,
    df["HeartRate"]>90,
    df["Pressure"]>140,
    df["Vitamin B"]<250
    ]

df["risk_count"]=sum(conditions)
df["risk_level"] = df["risk_count"].apply(lambda x: "High Risk" if x>=2 else "Normal")
print(df[df["risk_count"]>= 2])#high risk patients

#bar graph: hemoglobin level

colors = df["risk_level"].map({'High Risk':'red', "Normal":'green'})
m.bar(df["Patient"],df["Hemoglobin"],color=colors)
m.title("Hemoglobin Levels")
m.ylabel("g/dl→")
m.xlabel("patients→")
m.yticks(rotation=90)
m.show()

#line graph : sugar level trend
m.plot(df["Patient"],df["Sugar"],label='Sugar Level',marker='o')
for i, risk in enumerate(df["risk_level"]):
    if risk == "High Risk":
        m.plot(df["Patient"].iloc[i], df["Sugar"].iloc[i],marker = 'x',color='red',label='highrisk' if i == 0 else "")
m.title("Sugar Level Trends")
m.legend()
m.show()