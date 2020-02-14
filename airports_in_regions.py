import csv
from fastkml import kml
from shapely.geometry import shape, Point

with open('filtered_airports.csv') as csvfile:
    reader = csv.reader(csvfile)
    airports = list(reader)

with open('Pokemon Go Regional Map.kml') as kmlfile:
    kmldoc = kmlfile.read()

k = kml.KML()
k.from_string(bytes(kmldoc, encoding='utf-8'))
document = list(k.features())[0]
folders = list(document.features())

print([f.name for f in folders])

trios, hemispheric, paired, geographical, habitat, _, geoblock, _ = folders

panpour_azelf, pansage_uxie, pansear_mespirit = list(trios.features())

chatot = list(hemispheric.features())[0]

print(chatot.geometry)

s = shape(chatot.geometry)
print(s)
counter = 0
for airport in airports:
    lat, lon = airport[6:8]
    if s.contains(Point(float(lat), float(lon))):
        counter += 1
        print(airport[1], 'contains chatot')

print(counter, 'out of', len(airports))
