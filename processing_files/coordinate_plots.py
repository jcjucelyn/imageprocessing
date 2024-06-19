"""
This code is intended plot locations of images taken onto a
Folium map.
"""

# Necessary Imports
import piexif
import os
import pandas as pd
import time
import matplotlib.pyplot as plt
import folium


# Initialize variables
directory = '/Volumes/PRJ-LandRehyd/DroneData/2023 01 23-25/0017SET/000'
save_map = 'map.html' # file to save Folium map as
save_csv = 'convertedcoords.csv' # file to save coordinate csv as
stop_at = 20   # num image to stop at
plot = False   # plot points on a plot
marker = True  # plot markers on the Folium map
count = 0      # initial count
imgs = []      # list of images iterated through
coords = []    # list of decimal degree coordinates
latits = []    # list of decimal degree latitudes
longits = []   # list of decimal degree latitudes
start = time.time()

# Centrepoint around which to create the map (coordinates)
centre_coords = (-30.2744, 149.7981)

# Make map
main_map = folium.Map(location=centre_coords, zoom_start=14)


def get_lat_long(imagepath):
    """
    Get the latitude, longitude, and their respective directions
    :param imagepath: path to image
    :return: latitude, longitude, latitude direction, longitude direction
    """
    exif_dict = piexif.load(directory + '/' + imagepath)

    lat = exif_dict['GPS'][piexif.GPSIFD.GPSLatitude]
    lon = exif_dict['GPS'][piexif.GPSIFD.GPSLongitude]

    lat_dir = exif_dict.get('GPS', {}).get(piexif.GPSIFD.GPSLatitudeRef)
    long_dir = exif_dict.get('GPS', {}).get(piexif.GPSIFD.GPSLongitudeRef)

    return lat, lon, lat_dir, long_dir


def add_marker(coords, popup):
    """
    Add markers to the map
    :param coords: coordinates in decimal degrees
    :param popup: value of the popup on the map
    """
    folium.Marker(coords, popup=popup).add_to(main_map)


def _convert_coord(dms, dir):
    """
    Function to convert degree/minute/second coordinates into decimal degrees
    :param dms: coordinate in dms
    :param dir: direction of the coordinate (b'N', b'E', b'S', or b'W')
    :return: coordinate in decimal degrees
    """
    # Convert dms to decimal degrees
    d = float(dms[0][0])
    m = float(dms[1][0])/60
    s = float(dms[2][0])/3600

    # Account for negative coordinate values (South or West)
    if dir == b'S' or dir == b'W':
        coord = - (d + m + s)
    else:
        coord = d + m + s

    return coord


# Iterate through the images in the directory, get coordinates, and map
for img in os.listdir(directory):

    # Get coordinates & directions for image
    latit, longit, lat_dir, long_dir = get_lat_long(img)

    latit = [([i[0] / i[1]]) for i in latit]
    longit = [([i[0] / i[1]]) for i in longit]

    # Convert dms to degrees
    deg_lat = _convert_coord(latit, lat_dir)
    deg_long = _convert_coord(longit, long_dir)

    # Append to lists
    imgs.append(img)
    coords.append((deg_lat, deg_long))

    latits.append(deg_lat)
    longits.append(deg_long)

    # Add markers to the plot and/or map
    if plot:
        plt.scatter(deg_lat, deg_long)

    if marker:
        add_marker((deg_lat, deg_long), popup=img)

    # Uncomment to stop at the previously-defined count of images
    # if count / stop_at == 1:
    #     break

    count += 1

stop = time.time()
print(str(stop - start), 'sec')

# Show plots/save maps if previously determined
if plot:
    plt.show()

if marker:
    main_map.save(save_map)

# Save to a dataframe & download dataframe
df = pd.DataFrame({'Images': imgs, 'Latitude': latits, 'Longitude': longits, 'Coords':coords})
df.to_csv(save_csv, index=False)

# https://support.micasense.com/hc/en-us/articles/4403432185879-How-to-read-and-export-image-metadata-with-Exiftool
# https://www.earthdatascience.org/tutorials/introduction-to-leaflet-animated-maps/
