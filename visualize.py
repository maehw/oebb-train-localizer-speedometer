import os
import glob
import folium
import csv


center_latitude = 48.362762
center_longitude = 13.565262
map_zoom_start = 7

list_of_files = glob.glob("journey_started_*.csv")
travel_map = folium.Map(location=[center_latitude, center_longitude], tiles=None, zoom_start=map_zoom_start)

# add Openstreetmap layer
folium.TileLayer('openstreetmap', name='OpenStreet Map').add_to(travel_map)

# load coordinate points from different files
for file in list_of_files:
    print(f"Processing file '{file}'...")
    # collect points for every file
    points = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            # filter invalid coordinates
            if float(row[2]) != 0.0 and float(row[3]) != 0.0:
                points.append(tuple([float(row[2]), float(row[3])]))
    folium.PolyLine(points, color='red', weight=5, opacity=0.85).add_to(travel_map)
    print(f"  {len(points)} points added.")

# save and open map
travel_map.save('travel_map.html')
