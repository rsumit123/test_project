from flask import Flask
import geocoder
import geopy
from geopy.geocoders import Nominatim
from datetime import datetime
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    #print(request.environ['REMOTE_ADDR'])
    #request.remote_addr
    return {'ip': request.remote_addr}, 200


@app.route('/get_location')
def get_location():
    ip,_ = get_my_ip()
    #print(ip["ip"])
    try:
        g = geocoder.ip(ip["ip"])
        lat_long=g.latlng
        coord=', '.join(list(map(str,lat_long)))
        geolocator = Nominatim(user_agent="test_project")
        location = geolocator.reverse(coord)

        return location.address
    except:
        return "Sorry..! Could not determine location"



@app.route('/get_shops')
def get_shops():
    return_data = dict()
    curr_address = get_location()
    return_data["location"] = curr_address
    return_data["store_name"] = ["Dummy_Shop1","Dummy_shop2","Dummy_shop3","Dummy_shop4","Dummy_shop5"]
    return_data["date_time"]=str(datetime.now())
    return return_data




if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")