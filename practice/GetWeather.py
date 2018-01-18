from pathlib2 import Path
import wkey
import pyowm
import codecs
import time

def get_weather_for_city(place):
    owm = pyowm.OWM(wkey.weather_key) # use the api key to connect to owm service
    observation = owm.weather_at_place(place) # search for current weather in the place
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    degree_sign = u"\u00b0"
    output = "\nThe weather of %s is %3.2f%sC\n" %(place, temperature['temp'], degree_sign)
    print(output)

    # write the output into the weather1.txt file
    my_file = Path("FILE_PATH")
    if my_file.exists():
        f = codecs.open("weatherInSarnia.txt", encoding='utf-8', mode='a+')
    else:
        f = codecs.open("weatherInSarnia.txt", encoding='utf-8', mode='w+')

    f.write(output)
    f.close()


# call the function
city = "Sarnia,CA"
for i in xrange(10):
    get_weather_for_city(city)
    time.sleep(30)