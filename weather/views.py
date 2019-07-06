from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
import requests
import json



# disabling csrf (cross site request forgery)

def mars(request):
    template = loader.get_template('weather/mars.html')
    return HttpResponse(template.render())

def earth(request):
    template = loader.get_template('weather/earth.html')
    return HttpResponse(template.render())


def references(request):
    template = loader.get_template('weather/references.html')
    return HttpResponse(template.render())
@csrf_exempt
def index(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        print("in if part")
        location = request.POST.get('location')
        print ("location=",location)
        geolocator = Nominatim(user_agent="as")
        loc = geolocator.geocode(location)
        latitude = loc.latitude
        longitude = loc.longitude
        # adding the values in a context variable
        capacity = 4000
        pv_power_params = dict(
            longitude=longitude,
            latitude=latitude,
            capacity = capacity,
            api_key='XtH2jWKvhFYcfRCHJkl4x3HH8LGsWIAl',
            format='json'
        )
        radiation_params = dict(
            longitude=longitude,
            latitude=latitude,
            api_key='XtH2jWKvhFYcfRCHJkl4x3HH8LGsWIAl',
            format='json'
        )

        #url = "https://api.solcast.com.au/pv_power/forecasts?longitude="+str(longitude)+"&latitude="+str(latitude)+"&capacity="+str(capacity)+"&api_key=XtH2jWKvhFYcfRCHJkl4x3HH8LGsWIAl&format=json"
        pv_power_url = "https://api.solcast.com.au/pv_power/forecasts"
        radiation_url = "https://api.solcast.com.au/radiation/forecasts"

        pv_power_resp = requests.get(url=pv_power_url, params=pv_power_params)
        radiation_resp = requests.get(url=radiation_url, params=radiation_params)

        pv_power_data = pv_power_resp.json()
        radiation_data = radiation_resp.json()
        #print(pv_power_data)
        #print(radiation_data)
        pv_tot_forecast = pv_power_data['forecasts']
        rad_tot_forecast = radiation_data['forecasts']
        json1 = json.dumps(pv_tot_forecast)
        f = open("static/weather/scripts/dict.json", "w")
        f.write(json1)
        f.close()

        print(pv_tot_forecast)
        '''file = open('out.txt','w')
        dic1=[]
        for forecast in pv_tot_forecast:
            print (forecast)
            dic1.insert(len(dic1),forecast['pv_estimate'])
        dic2=[]
        for forecast in rad_tot_forecast:
            dic2.insert(len(dic2),forecast['period_end'])


        print ("dic1="+str(dic1[0]))
        print ("dic2="+str(dic2[0]))
        if len(dic1) == len(dic2):
            print ("hola")
        diic = []

        for i in range(len(dic1)):
            dic=[]
            dic.insert(len(dic),dic1[i])
            dic.insert(len(dic),dic2[i])

            diic.insert(len(dic),dic)
        json1 = json.dumps(diic)
        f = open("dict.json", "w")
        f.write(json1)
        f.close()

'''
        file.close()

        context = {
            'latitude': latitude,
            'longitude': longitude,
        }


        # getting our showdata template

        template = loader.get_template('weather/radiation.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('weather/index.html')
        return HttpResponse(template.render())
