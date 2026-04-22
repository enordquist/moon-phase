# Plot circles and ellipses to contstruct a moon phase

import numpy as np
import matplotlib.pyplot as plt
import requests
plt.style.use('dark_background')

def semiellipse(r1, r2, y):
  return r1*np.sqrt(1-(y/r2)**2) 

#-----------------------------------
# Get moon data using web API
date = "2026-04-21"
coords = "39.29,-76.61"   # Baltimore, MD
tz = -5                   # Eastern Time

params = {"date": date, "coords": coords, "tz": tz}
url = "https://aa.usno.navy.mil/api/rstt/oneday"
req = requests.get(url, params=params)

data = req.json()
moon = data["properties"]["data"]
# this is the fraction illuminated:
f = float(moon["fracillum"].replace('%',''))/100
#-----------------------------------

# Set up circle (pi*r**2) and ellipse (pi*r*r2)
r = 1
y = np.linspace(-r, r, 1000, endpoint=True)
# Crescent illuminated fraction:
#     ( pi/2 - pi/2*r2 )    
# f =  ---------------   => r2 = 1 - 2*f
#            pi
# Beautifully, when f>0.5, r2 < 0, so that xe<0 (proper rendered shape)
r2 = 1 - 2*f
xc = semiellipse(r,r,y)
xe = semiellipse(r2,r,y)

# Plot shapes
fig,ax = plt.subplots()
ax.fill_betweenx(y,xc, xe, color='gold') # illuminated shape
ax.fill_betweenx(y,xc,-xc, color='gold', alpha=0.10) # faintly visible
plt.axis('off')
plt.axis('equal')
fig.subplots_adjust(left=0,top=1,right=1,bottom=0)
plt.show()
