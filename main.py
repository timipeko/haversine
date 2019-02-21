import googlemaps 
from haversine import haversine

class GmapsWrapper:
    """This class wraps the googlemaps and haversine libraries to provide a convenient way to calculate the geodesic distance between any two locations
    
    Attributes:
        gmaps(Client) -- client used to make requests to Google cloud services API 
    """


    def __init__(self):
        """Initializes client used in making requests for geocoding

        Parameters:
            gmaps(Client) -- client used to make requests to Google cloud services API 
        """

        self.gmaps = googlemaps.Client(key='AIzaSyChg0CkeQ3jZ13j8-C9qCjqqD1rD9QEANM')

    def __str__(self):
        return "Gmaps Wrapper Instance"

    def geocode(self, address):
        """Wraps gmaps geocode function
        
        Arguments:
            address(str) -- contains location name string e.g. from API query, user input
        
        Returns:
            (JSON) -- Nested JSON containing geocode API response
        """

        return self.gmaps.geocode(address)

    def reverse_geocode(self, coords):
        """Wraps gmaps reverse_geocode function
        
        Arguments:
            coords(tuple) -- contains coordinates to query in form (lat(flt), lng(flt))
        
        Returns:
            (JSON) -- Nested JSON containing reverse_geocode API response
        """
        return self.gmaps.reverse_geocode(coords)

    def calculate_distance(self, origin, destination):
        """Calculates distance between two sets of coordinates using haversine formula
        
        Arguments:
            origin(tuple) -- origin coordinates in form (lat(flt), lng(flt))
            destination(tuple) -- destination coordinates in form (lat(flt), lng(flt))
        
        Returns:
            distance(str) -- string representation of calculated distance in either km or m
        """

        origin_coords = (self.geocode(origin)[0]['geometry']['location']['lat'], self.geocode(origin)[0]['geometry']['location']['lng'])
        destination_coords = (self.geocode(destination)[0]['geometry']['location']['lat'], self.geocode(destination)[0]['geometry']['location']['lng'])
        
        if haversine(origin_coords, destination_coords) > 1:
            distance = "{:.2f} km".format(haversine(origin_coords, destination_coords))
        else:
            distance = "{:.0f} m".format(haversine(origin_coords, destination_coords, unit='m'))
        
        return distance