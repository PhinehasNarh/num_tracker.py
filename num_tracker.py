import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Define the phone number you want to track
number = "+1234567890"  # Replace with the actual number you want to track

# Parse the phone number
phoneNumber = phonenumbers.parse(number)

# OpenCage API Key
Key = "eac2d56b30b14966baaedb7335dc02a8"  # Replace with your actual API key

# Get the location description using the geocoder module
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("Location: " + yourLocation)

# Get the service provider using the carrier module
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("Service provider: " + yourServiceProvider)

# Initialize OpenCageGeocode with your API key
geocoder = OpenCageGeocode(Key)

# Query for latitude and longitude
query = str(yourLocation)
results = geocoder.geocode(query)

# Check if results are available
if results:
    # Assign latitude and longitude
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map centered at the location
    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    # Add a marker with the location name
    folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("Location.html")
    print("Map has been saved as 'Location.html'. Open it in your browser to view the location.")
else:
    print("No results found for the given location.")


#ph1n3y
