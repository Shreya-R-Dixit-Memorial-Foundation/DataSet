import pandas as pd
import folium

# Load the cleaned accident data
df = pd.read_csv('C:\\Users\\Theya\\OneDrive - MNSCU\\Desktop\\EyeDaV2\\DVSCrashData\\mn-2016-2021-acc-cleaned-sample.csv')

# Create a map centered around Minnesota
m = folium.Map(location=[46.4419, -93.3650], zoom_start=6)

# Add a marker for each accident
for index, row in df.iterrows():
    folium.Marker([row['XCOORD'], row['YCOORD']]).add_to(m)

# Save it to a file
m.save('C:\\Users\\Theya\\OneDrive - MNSCU\\Desktop\\EyeDaV2\\DVSCrashData\\marked_accidents_map_sample.html')
