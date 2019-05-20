import geopandas
import matplotlib.pyplot as plt


class isorange:
    def __init__(self, filepath, maxdistance, zonesize):
        self.file_path = filepath
        self.max_distance = maxdistance
        self.zone_size = zonesize

    def run(self):
        #1. open file
        gdf_shp = geopandas.read_file(self.file_path)

        #2. explode links to simple geometry        
        # gdf_split = geopandas.GeoDataFrame()
        # for o in gdf_shp.itertuples():
        #     print(o)

        for c in range(0,10):
            f = gdf_shp[c]
            print(f)

        #3. split lines to simple lines
        # for g in gdf_shp.iterrows():            
        #     gdf_split.insert(g)
        
        #print(gdf_split.head())
        #gdf.plot()
        #plt.show()





i = isorange("P:\Python\isorange\mock\mock_links.shp",10000,1000)
i.run()
