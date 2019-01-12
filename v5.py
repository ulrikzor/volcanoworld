
import os
import json
import folium
import pandas
import requests
from folium import plugins
from bs4 import BeautifulSoup
from tabulate import tabulate
from folium.features import DivIcon
from geopy.geocoders import Nominatim
from folium.plugins import MeasureControl, FloatImage

df = pandas.read_csv('GVP.csv')
df2 = pandas.read_csv('GVP2.csv')

def ld(column_name):
    return list(df[str(column_name)])

lat = ld("Latitude")
lon = ld("Longitude")
elev = ld("Elevation (m)")
nam = ld("Volcano Name")
typ = ld("Primary Volcano Type")
loc = ld("Country")
lst = ld("Last Known Eruption")
drt = ld("Dominant Rock Type")
reg = ld("Region")
sub = ld("Subregion")
tec = ld("Tectonic Setting")
act = ld("Activity Evidence")
vnr = ld("Volcano Number")

def ld2(column_name):
    return list(df2[str(column_name)])

lat2 = ld2("Latitude")
lon2 = ld2("Longitude")
elev2 = ld("Elevation (m)")
nam2 = ld2("Volcano Name")
typ2 = ld2("Primary Volcano Type")
loc2 = ld2("Country")
lst2 = ld2("Last Known Eruption")
drt2 = ld2("Dominant Rock Type")
reg2 = ld2("Region")
sub2 = ld2("Subregion")
tec2 = ld2("Tectonic Setting")
act2 = ld2("Activity Evidence")
vnr2 = ld2("Volcano Number")

def color_producer(elevation):
    if elevation < 0:
        return '#B8FDFF'
    elif 0 <= elevation <= 1000:
        return 'green'
    elif 1000 <= elevation <= 2000:
        return 'yellow'
    elif 2000 <= elevation <= 3000:
        return 'orange'
    elif 3000 <= elevation <= 4000:
        return 'red'
    elif 4000 <= elevation <= 5000:
        return 'purple'
    else:
        return 'black'

#map details
map = folium.Map(location=[31, 20], zoom_start=2, 
                 tiles="Stamen Terrain")

#add extra tiles to map
def t_layer(name):
    return folium.TileLayer(str(name)).add_to(map)
t_layer('Mapbox ControlRoom')
t_layer('Mapbox Bright')
t_layer('stamentoner')
t_layer('stamenwatercolor')
t_layer('cartodbpositron')
t_layer('cartodbdark_matter')

#text on coordinates: <div style="font-size: 24pt">APPLY HERE</div>
folium.map.Marker([34.0302, -118.2352],icon=DivIcon(icon_size=(150,36),
                  icon_anchor=(0,0),
                  html='<div style="font-size: 24pt"></div>')).add_to(map)

fgv = folium.FeatureGroup(name="Holocene volcanoes")
fgl = folium.FeatureGroup(name="Pleistocene volcanoes",overlay=True,
                          control=True, show=False)

#add population layer
"""fgp = folium.FeatureGroup(name="Population", show=False)
  data_json = open("world.json", 'r', encoding='utf-8-sig').read()
  
  fgp.add_child(folium.GeoJson(data=data_json,
style_function=lambda x: {'fillColor':'green' if x['properties'] ['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))"""

#holocene volcanoes
for lt, ln, el, nm, ty, lc, ls, dr, re, su, te, ac, vn in zip(
lat, lon, elev, nam, typ, loc, lst, drt, reg, sub, tec, act, vnr):
    fgv.add_child(folium.RegularPolygonMarker(
        location=[lt, ln], number_of_sides = 3, 
        radius = 9, popup="Name: " + nm + " " + "(" + str(vn) + ")"
                          +"<br>"
                          +"Location:" + " " + lc
                          +"<br>"
                          +"Region:" + " " + str(re)
                          +"<br>"
                          +"Subregion:" + " " + str(su)
                          +"<br>"
                          + "Altitude: " + str(el) + " m"
                          + "<br>"
                          + "Type: " + ty
                          + "<br>"
                          + "Dominant rock type: " + str(dr)
                          + "<br>"
                          + "Tectonic Setting:" + " " + str(te)
                          + "<br>"
                          + "Last known eruption: " + str(ls)
                          + "<br>"
                          + "Activity evidence:" + " " + str(ac)
                          + "<br>"
                          + "Coordinates: " + str(lt) + " " + " " + str(ln),
            fill_color = color_producer(el), color = 'grey', 
            fill_opacity = 0.7))

#pleistocene volcanoes
for lt2, ln2, el2, nm2, ty2, lc2, ls2, dr2, re2, su2, te2, ac2, vn2 in zip(
lat2, lon2, elev2, nam2, typ2, loc2, lst2, drt2, reg2, sub2, tec2, act2, vnr2):
    fgl.add_child(folium.RegularPolygonMarker(
        location=[lt2, ln2], number_of_sides = 3,
        radius = 9, popup="Name: " + nm2 + " " + "(" + str(vn2) + ")"
                          +"<br>"
                          +"Location:" + " " + lc2
                          +"<br>"
                          +"Region:" + " " + str(re2)
                          +"<br>"
                          +"Subregion:" + " " + str(su2)
                          +"<br>"
                          + "Altitude: " + str(el2) + " m"
                          + "<br>"
                          + "Type: " + ty2
                          + "<br>"
                          + "Dominant rock type: " + str(dr2)
                          + "<br>"
                          + "Tectonic Setting:" + " " + str(te2)
                          + "<br>"
                          + "Last known eruption: " + str(ls2)
                          + "<br>" 
                          + "Activity evidence:" + " " + str(ac2)
                          + "<br>"
                          + "Coordinates: " + str(lt2) + " " + " " + str(ln2), 
        fill_color = color_producer(el2), color = 'grey', 
        fill_opacity = 0.7))

#display image on map (logo)
url = ('https://volcano.si.edu/includes/images/GVP_logo.png')
FloatImage(url, bottom=1,
           left=1).add_to(map)  

#elevation image
url = ('elev.jpg')
FloatImage(url, bottom=25,
           left=91).add_to(map)   

#corner minimap
minimap = plugins.MiniMap()
map.add_child(minimap)

map.add_child(fgv)
"""map.add_child(fgp)""" #add the population-feature to the map
map.add_child(fgl)
map.add_child(folium.LayerControl()) 
map.add_child(MeasureControl())
map.save("world_volcanoes.html")
