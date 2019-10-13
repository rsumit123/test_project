from flask import Flask
import geocoder
import geopy
from geopy.geocoders import Nominatim
from datetime import datetime

app = Flask(__name__)


@app.route('/get_location')
def get_location():
    g = geocoder.ip('me')
    lat_long=g.latlng
    coord=', '.join(list(map(str,lat_long)))
    geolocator = Nominatim(user_agent="test_project")
    location = geolocator.reverse(coord)

    return location.address

@app.route('/get_shops')
def get_shops():
    return_data = dict()
    curr_address = get_location()
    return_data["location"] = curr_address
    return_data["store_name"] = ["Dummy_Shop1","Dummy_shop2","Dummy_shop3","Dummy_shop4","Dummy_shop5"]
    return_data["date_time"]=str(datetime.now())
    return return_data




if __name__ == '__main__':
    app.run()