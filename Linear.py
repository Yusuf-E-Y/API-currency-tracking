import pandas as pd
import xml.etree.ElementTree as ET
import requests
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

url = "https://www.tcmb.gov.tr/kurlar/today.xml" 
response = requests.get(url) 
tree = ET.fromstring(response.text)

for currency in tree.findall("Currency"): 
    code = currency.get("CurrencyCode") 
    if code in ["USD"]: 
        name = currency.find("Isim").text 
        forex_selling = currency.find("ForexSelling").text

data = pd.read_csv("data.csv")

Int = data["Faiz"]
Enf = data["Enflasyon"]
Cur = data["Dolar"]
Date = data["Tarih"]

def Predict(num):
    dolar_array = [forex_selling]
    array_Int = np.array(Int)
    array_Enf = np.array(Enf)
    array_Cur = np.array(Cur)
    for i in range(num):
        # ENF
        X = np.arange(1, len(array_Enf)+1).reshape(-1,1) 
        y = array_Enf

        scaler = StandardScaler()
        X_ENF = scaler.fit_transform(X)

        model_Enf = LinearRegression()
        model_Enf.fit(X_ENF,y)
            
        next_date_ENF = np.array([[X[-1, 0] + 1]])  # 2D array, bir sonraki "tarih" için
        next_val = model_Enf.predict(scaler.transform(next_date_ENF))        

        array_Enf = np.append(array_Enf,next_val[0])

        #INT
        X1 = np.arange(1,len(array_Int)+1).reshape(-1,1)
        y1 = array_Int

        scaler1 = StandardScaler()
        X_INT = scaler1.fit_transform(X1)

        model_INT = LinearRegression()
        model_INT.fit(X_INT,y1)

        next_date_INT = np.array([[X[-1, 0] + 1]])  # 2D array, bir sonraki "tarih" için
        next_val1 = model_INT.predict(scaler1.transform(next_date_INT))

        array_Int = np.append(array_Int,next_val1[0])        
        
        #Dolar
        X2 = np.column_stack((array_Enf[:-1], array_Int[:-1]))  # shape = (num_samples, 2)
        y2 = array_Cur

        scaler2 = StandardScaler()
        X_Cur = scaler2.fit_transform(X2)

        model_Cur = LinearRegression()
        model_Cur.fit(X_Cur,y2)

        user_input = [[array_Enf[-1], array_Int[-1]]]
        user_scaled = scaler2.transform(user_input)
        prediction = model_Cur.predict(user_scaled)

        array_Cur = np.append(array_Cur,prediction[0])

        percentage = float(dolar_array[-1])
        dolar = percentage * (1 + prediction[0]/100)
        
        dolar_array.append(dolar)
        
    return dolar_array