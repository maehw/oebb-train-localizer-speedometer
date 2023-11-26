import glob
import folium
import csv
import branca.colormap

# define map center and zoom level
center_latitude = 48.362762
center_longitude = 13.565262
map_zoom_start = 7
vmin = 0  # minimum train velocity
vmax = 230  # maximum train velocity

# define a color map for mapping the speed; this can either be a single color (string!) or a color map
# track_color = 'red'
track_color = branca.colormap.LinearColormap(["red", "yellow", "green"], vmin=vmin, vmax=vmax)
# track_color = branca.colormap.linear.RdYlGn_04.scale(vmin, vmax)

list_of_files = glob.glob("journey_started_*.csv")
travel_map = folium.Map(location=[center_latitude, center_longitude], tiles=None, zoom_start=map_zoom_start)

# add Openstreetmap layer
folium.TileLayer('openstreetmap', name='OpenStreet Map').add_to(travel_map)

# load coordinate points from different files
for file in list_of_files:
    print(f"Processing file '{file}'...")
    # collect points for every file
    points = []
    speeds = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            # filter invalid coordinates
            if float(row[2]) != 0.0 and float(row[3]) != 0.0:
                points.append(tuple([float(row[2]), float(row[3])]))
                speeds.append(row[1])
                num_points = len(points)
                if num_points > 0:
                    line_points = [points[num_points-2], points[num_points-1]]
                    # print(f"Line points: {line_points}; speed: {speeds[-1]}")

                    if not isinstance(track_color, str):
                        folium.ColorLine(line_points, colormap=track_color, weight=5,
                                         colors=[int(speeds[-1])]).add_to(travel_map)
    if isinstance(track_color, str):
        folium.PolyLine(points, color=track_color, weight=5, opacity=0.85).add_to(travel_map)
    print(f"  {len(points)} points added.")

# save and open map
travel_map.save('travel_map.html')
print("Done.")
