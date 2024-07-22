import folium as f
import streamlit as st
from streamlit_folium import folium_static

st.set_page_config(
    page_title="Mapify",
    page_icon="icon.png",
    menu_items={
        "About":"Mapify transforms your coordinates into a vibrant map view in seconds! Simply enter your latitude and longitude to visualize any location around the globe. Fast, intuitive, and perfect for explorers, researchers, and travel enthusiasts. Discover your world with Mapify now!"
    }
)

st.write("<h2 style='color:#00BFFF;'>Instant Map from Coordinates!</h2>",unsafe_allow_html=True)

st.page_link(page="https://gps-coordinates-finder.netlify.app/",label="Retrieve Current Coordinates From Here.",icon='🗺️')

latitude=st.text_input("Enter Latitude",placeholder="34.0522")
longitude=st.text_input("Enter Longitude",placeholder="-118.2437")
btn=st.button("View Location")

if btn:
    if(latitude=="" or longitude==""):
        st.warning("Invalid Coordinates")
    else:
        map = f.Map(location=[latitude,longitude], zoom_start=14)

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
            addTileLayer(tile_layer,attribution)

        defineLayer("https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png","Map 1")

        defineLayer("https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png","Map 2")

        defineLayer("https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}","Map 3")

        defineLayer("https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png","Map 4")

        defineLayer("https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png","Map 5")

        defineLayer("http://sgx.geodatenzentrum.de/wmts_topplus_open/tile/1.0.0/web/default/WEBMERCATOR/{z}/{y}/{x}.png","Map 6")

        defineLayer("https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png","Map 7")

        defineLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}","Map 8")

        f.LayerControl().add_to(map)

        folium_static(map)
