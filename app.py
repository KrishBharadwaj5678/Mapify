import folium as f
import streamlit as st
from streamlit_folium import folium_static
import requests

st.set_page_config(
    page_title="Track Me Live",
    page_icon="icon.png",
    menu_items={
        "About":"Track your current location on an interactive map with ease. Our Real-Time Location Tracker provides instant updates on your whereabouts, helping you navigate and explore with confidence. Perfect for travel, adventure, or just finding your way!"
    }
)

st.write("<h2 style='color:#00BFFF;'>Real-Time Location Tracker.</h2>",unsafe_allow_html=True)

url2=requests.get(f"https://ipinfo.io/json")
geo_data=url2.json()

latitude,longitude,city,region,timezone = geo_data["loc"].split(",")[0],geo_data["loc"].split(",")[1],geo_data["city"],geo_data["region"],geo_data["timezone"]

map = f.Map(location=[latitude, longitude], zoom_start=16)

def addTileLayer(tile_layer,attribution):
    f.TileLayer(
        tiles=tile_layer,
        attr=attribution,
        name=attribution,
        overlay=True
    ).add_to(map)

def defineLayer(url,attr):
    tile_layer = url
    attribution = attr
    addTileLayer(tile_layer,attribution,)

defineLayer("https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png","Map 1")

defineLayer("https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png","Map 2")

defineLayer("https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}","Map 3")

defineLayer("https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png","Map 4")

defineLayer("https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png","Map 5")

defineLayer("http://sgx.geodatenzentrum.de/wmts_topplus_open/tile/1.0.0/web/default/WEBMERCATOR/{z}/{y}/{x}.png","Map 6")

defineLayer("https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png","Map 7")

defineLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}","Map 8")

f.LayerControl().add_to(map)

f.Marker([latitude, longitude], popup=f.Popup(f"<h3 style=color:crimson;>{city}</h3>", max_width=300)).add_to(map)
folium_static(map)

st.write(f"<h3>City: {city}</h3>", unsafe_allow_html=True)
st.write(f"<h3>State: {region}</h3>", unsafe_allow_html=True)
st.write(f"<h3>Timezone: {timezone}</h3>", unsafe_allow_html=True)