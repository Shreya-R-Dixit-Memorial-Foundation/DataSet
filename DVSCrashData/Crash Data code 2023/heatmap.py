import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the cleaned accident data
df = pd.read_csv('C:\\Users\\Theya\\OneDrive - MNSCU\\Desktop\\EyeDaV2\\DVSCrashData\\mn-2016-2021-acc-cleaned-sample.csv')

# Create a map centered around Minnesota
m = folium.Map(location=[46.4419, -93.3650], zoom_start=6)

# Add a heatmap layer
heat_data = [[row['XCOORD'], row['YCOORD']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(m)

# Save it to a file
m.save('C:\\Users\\Theya\\OneDrive - MNSCU\\Desktop\\EyeDaV2\\DVSCrashData\\accidents_heat_map_sample.html')
