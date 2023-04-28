# Programmer name Mohammad Shirvani
# Date 1402/02/08
# This code Smoothes a curve to show its trend

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("project_data.csv")

df_close=df[["<CLOSE>"]]
df_days=df[["<DTYYYYMMDD>"]]

l=len(df_close)
x=range(l)

close=np.array(df_close)
day=np.array(df_days)

close_smooth=close.copy()
smooth_size=21

for i in range(l-smooth_size+1):
  close_smooth[i]=sum(close[i:i+smooth_size])/smooth_size

plt.plot(x,close,label="old")
plt.plot(x,close_smooth,label="smooth")
plt.xlabel("DAYS")
plt.ylabel("CLOSE")
plt.title("smoothing")
plt.legend()
plt.show()