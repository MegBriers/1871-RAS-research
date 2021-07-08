# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:08:40 2021

@author: Meg
"""

import folium
from folium.plugins import BeautifyIcon

icon_star = BeautifyIcon(
    icon='star',
    inner_icon_style='color:blue;font-size:30px;',
    background_color='transparent',
    border_color='transparent',
)

icon= BeautifyIcon(icon="star",text_color='#b3334f', background_color='transparent',border_color='transparent', inner_icon_style='font-size:20px')


m = folium.Map(location=[41,15], tiles="OpenStreetMap", zoom_start=6)

# Import the pandas library
import pandas as pd

# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':[13.033800, 12.464430, 15.080009969314204, 15.016040, 15.284260, 15.092450],
   'lat':[41.982570, 45.590300, 37.5045164837884, 37.273682, 37.066170, 37.250870],
   'name':['Agnosta', 'Terra Nuora', 'Sanctuary', 'Carlentini', 'Syracuse', 'Villasmunda'],
   'value':[10, 12, 40, 70, 23, 1],
   'members':[['Cacciatore', 'Sechi', 'Donati', 'Blaserna', 'Agnello', 'De Lisa', 'Tagiliarini', 'Adams', 'Burton', 'Clifford'],['P Tacchini', 'Lorenzoni', 'Legnazzi', 'Nobile', 'A Tacchini', 'Diamilla Muller', 'Serra'],['Schott', 'Lane', 'Fitz', 'Chapman', 'Burgess', 'N Lockeyer', 'Mrs Lockeyer', 'Seabroke', 'Cumming', 'Thorpe', 'Pedlar'],['Watson'],['Party of the US Naval Observatory', 'Harkness', 'Hall', 'Eastman', 'Mrs Eastman', 'Brothes', 'Fryer', 'Griffiths'],['Raynard', 'Samuelson', 'Brett']],
   'summary':['Very near central line, mainly Italian observers','Only Italian observers, must be near central line','Photographers + Headquarters for time and latitude observations','Only one observer??','Party of the US Naval Observatory + others','Only British observers, not quite in the centre of Villasmunda either']

}, dtype=str)

def example(elements):
    return '<ul>\n' + '\n'.join(['<li>'.rjust(8) + name + '</li>' for name in elements]) + '\n</ul>'

# add marker one by one on the map
for i in range(0,len(data)):
    html=f"""
        <h1> {data.iloc[i]['name']}</h1>
        <p>Members of the party:</p>""" + example(data.iloc[i]['members'])+ """</p> <p>""" + data.iloc[i]['summary'] + """</p>"""
    iframe = folium.IFrame(html=html, width=200, height=200)
    popupa = folium.Popup(iframe, max_width=2650)
    folium.Marker(
        location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
        icon=BeautifyIcon(icon="star",text_color='#b3334f', background_color='transparent',border_color='transparent', inner_icon_style='font-size:20px'),
        popup = popupa
    ).add_to(m)

# Show the map again
m.save('1871_eclipse.html')

# monte rossi di nicolosi (western top)

# slope of mount etna (8000ft)
# casa terentina del bosco


# casai di st guiliano (500 ft)


# monte rossi (3120 feet high)
