import shapely
import fiona


class zc:
    linkslist = list()

    def loadfromshp(self, filename):
        self.shp = fiona.open(filename)
