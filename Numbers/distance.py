"""
Calculates the distance between two cities and allows the user to
specify a unit of distance.
"""

#usage: python2 distance.py

import math
import geopy

class City(object):

    def __init__(self, name, lat, lon):

        self.name = name
        self.lon = float(lon)
        self.lat = float(lat)

    def __str__(self):

        return name + " : " + str(lon) + ", " + str(lat)

    def distanceFrom(self, lat2, lon2):
        """
        Return distance in km from city to any point (longitude and
        latitude).  The implementation is a simple haversine formula.
        It's precise at best of 0.5%, because earth is not a perfect
        sphere
        """

        # TODO add multimethods for accepting a City() as param
        
        lat1 = self.lat
        lon1 = self.lon
        # degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        r = 6367.5 # average radius of earth in km

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        part1 = math.sin(dlat / 2)**2
        part2 = math.cos(lat1) * math.cos(lat2)
        part3 = math.sin(dlon / 2)**2
        
        d = 2 * r * math.asin(math.sqrt(part1 + part2 * part3))

        return d


def createCity(name, nation):

    g = geopy.geocoders.GoogleV3()

    # example call
    # g.geocode("London"") == (u'London, UK', (51.51121389999999, -0.1198244))
    
    (lat, lon) = g.geocode(name + " " + nation)[1]
    
    return City(name, lat, lon)


def main():
    
    name1 = raw_input("Name of the first city name> ")
    nation1 = raw_input("Nation> ")

    name2 = raw_input("Name of the second city> ")
    nation2 = raw_input("Nation> ")

    g = geopy.geocoders.GoogleV3()

    c1 = createCity(name1, nation1)
    c2 = createCity(name2, nation2)

    d = c1.distanceFrom(c2.lat, c2.lon)

    print "The distance between %s and %s is %f km" % (c1.name, c2.name, d)


if __name__ == "__main__":

    print __doc__

    main()
