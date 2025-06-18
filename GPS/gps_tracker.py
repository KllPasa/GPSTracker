# Importing Necessary Modules
import os
import requests
from selenium import webdriver
import folium
import datetime
import time

# this method will return us our actual coordinates
# using our ip address

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except Exception as e:
        print("Internet Not available:", e)
        exit()


# this method will fetch our coordinates and create a html file
# of the map
def gps_locator():

    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state = locationCoordinates()
        print("You Are in {},{}".format(city, state))
        print("Your latitude = {} and longitude = {}".format(lat, long))
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        folder = "C:/screengfg"
        os.makedirs(folder, exist_ok=True)  # Klasör yoksa oluşturur
        fileName = folder + "/Location" + str(datetime.date.today()) + ".html"

        obj.save(fileName)

        return fileName

    except Exception as e:
        print("Error:", e)
        return False


# Main method
if __name__ == "__main__":

    print("---------------GPS Using Python---------------\n")

    # function Calling
    page = gps_locator()
    if page:
        print("\nOpening File.............")
        dr = webdriver.Chrome()
        dr.get(page)
        time.sleep(100)  # Wait for 100 seconds to view the map
        dr.quit()
        print("\nBrowser Closed..............")
    else:
        print("Map could not be created.")