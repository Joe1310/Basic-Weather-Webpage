from django.shortcuts import render
import json
# urllib.request to make a request to api
import urllib.request

def kelvinToCelcius(kelvin):
    return kelvin - 273.15

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # source contain JSON data from API
        try:
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q='
                + city + '&appid=83cb6b5b79f2350dd478a0427955ffbb').read()

            # converting JSON data to a dictionary
            list_of_data = json.loads(source)
            temperature = kelvinToCelcius(list_of_data['main']['temp'])

            # data for variable list_of_data
            data = {
                "city": city.capitalize(),
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                              + str(list_of_data['coord']['lat']),
                "temp": str(round(temperature, 2)) + 'C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
        except:
            data = {}
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)