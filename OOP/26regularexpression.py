import re

pattern = r"[A-Z]+yclone" #just like f string it is r string 
text = (
    'a Cyclone (/ˈsaɪ.kloʊn/) is a large air mass that rotates around a strong center '
    'of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise '
    'in the Southern Hemisphere as viewed from above (opposite to an anticyclone).\n'
    'Dyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.\n'
    'The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale '
    '(the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie '
    'within the synoptic scale.\n'
    'Mesocyclones, tornadoes, and dust devils lie within the smaller mesoscale.'
)

# match = re.search(pattern,text) it stop after first match
match = re.finditer(pattern,text)
for mat in match:
    print(mat)

