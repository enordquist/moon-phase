# plot circles and ellipses to contstruct a moon phase in python

import numpy as np
import matplotlib.pyplot as plt
import requests
plt.style.use('dark_background')

def semiellipse(r1, r2, y):
  return r1*np.sqrt(1-(y/r2)**2) 

# get moon data
date = "2026-04-22"
coords = "39.29,-76.61"   # Baltimore, MD
tz = -5                   # Eastern Time

url = "https://aa.usno.navy.mil/api/rstt/oneday"

params = {
  "date": date,
  "coords": coords,
  "tz": tz
}

r = requests.get(url, params=params)
data = r.json()
moon = data["properties"]["data"]
f = f = float(moon["fracillum"].replace('%',''))/100

r = 1
y = np.linspace(-r, r, 1000, endpoint=True)
# Beautifully, when f>0.5, r2 < 0, so that xe<0 (proper rendered shape)
r2 = 1 - 2*f
xc = semiellipse(r,r,y)
xe = semiellipse(r2,r,y)

fig,ax = plt.subplots()
ax.fill_betweenx(y,xc, xe, color='gold')
ax.fill_betweenx(y,xc,-xc, color='gold', alpha=0.12)
plt.axis('off')
plt.axis('equal')
fig.subplots_adjust(left=0,top=1,right=1,bottom=0)
plt.show()



