import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyBxmKAcGrKpJCEf-mWsZDCJ4ttdqKnxhkE')
now = datetime.now()
directions_result = gmaps.directions("431 farmer rd townville, SC","209 warwick st, Anderson, SC",mode='driving', departure_time=now)

print(directions_result)