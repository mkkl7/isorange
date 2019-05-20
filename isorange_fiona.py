import fiona
import shapely as spl
import shapely.geometry as geom

links_inp = fiona.open("P:\Python\isorange\mock\mock_links.shp")
link_items = list(links_inp.items())
print(len(link_items))

# for x in range(0,2):
#     s=""
#     for k, v in l_itms[x][1]["properties"].items():
#         s+=('k: ' + str(k) + ' v: ' + str(v) + ' | ')
#     print(s)
lines = []

for x in range(0,3):    
    f = link_items[x]
    fgc = link_items[x][1]["geometry"]["coordinates"]
    print(len(fgc))
    for c in range(1,len(fgc)):
        # p1 = geom.Point(fgc[c-1])
        # p2 = geom.Point(fgc[c])        
        l = geom.LineString([fgc[c-1], fgc[c]])
        lines.append(l)
        print(l)
     
        