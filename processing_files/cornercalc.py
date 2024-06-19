"""
This file calculates the corners of a NxN metre block around a
given centrepoint.
"""

import ast
# Necessary imports
import math
import os
import pandas as pd

# Initialize variables
directory = '/Volumes/PRJ-LandRehyd/DroneData/2023 01 23-25/0017SET/000'
lats = []
lons = []


def calc_corners(center_coord, block_size_metres):
    # decimal degrees > radians
    center_lat_radian = math.radians(center_coord[0])
    center_lon_radian = math.radians(center_coord[1])

    # Set variables
    earth_radius = 6378137.0  # earth radius in metres
    lat_metre_deg = 1 / (earth_radius * math.pi / 180)  # 1 deg latitude in m
    lon_metre_deg = 1 / (earth_radius * math.cos(center_lat_radian) * math.pi / 180)

    # offsets in lat/long
    lat_offset_metres = block_size_metres / lat_metre_deg
    lon_offset_metres = block_size_metres / lon_metre_deg

    # calculate corners
    northeast_lat = center_coord[0] + lat_offset_metres
    northeast_lon = center_coord[1] + lon_offset_metres

    southwest_lat = center_coord[0] - lat_offset_metres
    southwest_lon = center_coord[1] - lon_offset_metres

    southeast_lat = center_coord[0] - lat_offset_metres
    southeast_lon = center_coord[1] + lon_offset_metres

    northwest_lat = center_coord[0] + lat_offset_metres
    northwest_lon = center_coord[1] - lon_offset_metres

    # return coords (southwest, southeast, northwest, northeast)
    return (southwest_lat, southwest_lon), (southeast_lat, southeast_lon), (northwest_lat, northwest_lon), \
        (northeast_lat, northeast_lon)


# read in coordinate data
df = pd.read_csv('convertedcoords.csv')

for coords in df['Coords']:
    coord = ast.literal_eval(coords)

    # find the coordinates of the bounding box
    print(calc_corners(coord, 2))
