from django.shortcuts import render

def home(request):
    import json
    import requests


    if request.method == "POST": #if form has been filled out. program recognises a POST has happened
        zipcode = request.POST['zipcode'] #Grabs zipcode from the form that we filled out (line 37 base.html)

        #zip code gets added to request URL
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=A0E7CDD0-9795-465F-A6F5-EB72DBC62691")

        #Runs code below with a new zip code entered in line 9.
        try:
            api = json.loads(api_request.content) #load content from api variable
        except Exception as e:
            api = "Error..."

        if api[0]['AQI'] <= 50:
            category_description = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"

        elif api[0]['AQI'] <= 100:
            category_description = "(51 - 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"

        elif api[0]['AQI'] <= 150:
            category_description = "(101 - 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "unhealthyforsensitivegroups"

        elif api[0]['AQI'] <= 200:
            category_description = "(151 - 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"

        elif api[0]['AQI'] <= 300:
            category_description = "(201 - 300) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy" 

        else:
            category_description = "(301+) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"
                
        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color 
            }) #transfers variable using context api dictionairy. Can now access on home page 

    #Runs code below with default zip code 49024.
    else:

        #gets request
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=49024&distance=5&API_KEY=A0E7CDD0-9795-465F-A6F5-EB72DBC62691")

        try:
            api = json.loads(api_request.content) #load content from api variable
        except Exception as e:
            api = "Error..."

        if api[0]['AQI'] <= 50:
            category_description = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"

        elif api[0]['AQI'] <= 100:
            category_description = "(51 - 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"

        elif api[0]['AQI'] <= 150:
            category_description = "(101 - 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "unhealthyforsensitivegroups"

        elif api[0]['AQI'] <= 200:
            category_description = "(151 - 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"

        elif api[0]['AQI'] <= 300:
            category_description = "(201 - 300) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy" 

        elif api[0]['AQI'] > 301:
            category_description = "(301+) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"
                
        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color 
            }) #transfers variable using context api dictionairy. Can now access on home page 


def about(request):
    return render(request, 'about.html', {})
