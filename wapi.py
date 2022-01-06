import requests
import json
from PIL import Image, ImageFont, ImageDraw 
import datetime

api_key = "0123456789abcdef0123456789abcdef"
Japan_list = ["Tokyo", "Osaka", "Kyoto", "Nagoya", "Nara"]
Emirates_list = ["Dubai", "Abu Dhabi", "Ajman", "Sharjah", "Hatta"]
US_list = ["New York", "Chicago", "Boston", "Los Angeles", "Las Vegas"]

country_list = [Japan_list, Emirates_list, US_list]

position = [285, 414, 542, 676, 808]

e = datetime.datetime.now()

for country in country_list:

    image = Image.open("post.png")
    Draw = ImageDraw.Draw(image)

    Font = ImageFont.truetype('font.otf', size=50)
    content = "天気予報"
    color = 'rgb(255, 255, 255)'
    Draw.text((425,51), content, color, font=Font)
    # here 15,15 are the co-ordinates on the image where you wanna print your text
    # how to find these co-ordinates ?
    # right click on image --> go to edit --> find the co-ordinates at left bottom
    Font1 = ImageFont.truetype('font.otf', size=30)
    content1 = e.strftime("%I:%M:%S %p")
    Draw.text((94,143), content1, color, font=Font1)

    content2 = e.strftime("%a, %b %d, %Y")
    Draw.text((760,145), content2, color, font=Font1)

    index = 0
    for city in country:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=8979fc6fe74b863ae2f5042f48ff82f9".format(city)
        response = requests.get(url)
        data = json.loads(response.text)

        Font3 = ImageFont.truetype('font.otf', size=50)
        color3 = 'rgb(0, 0, 0)'
        Draw.text((155,position[index]), city, color3, font=Font3)

        color4 = 'rgb(255, 255, 255)'
        content = data['main']['temp']
        content = content - 273
        content = round(content, 2)
        Draw.text((590,position[index]), str(content) + u"\N{DEGREE SIGN}", color4, font=Font3)

        content = data['main']['humidity']
        Draw.text((830,position[index]), str(content) + "%", color4, font=Font3)

        index += 1

    # image.save("result.png")
    # if you save the image of every iteration by same name
    # your program will save/display the output of anly last country
    # coz, outputs of first two countries will get overlapped my next one
    image.save(country[0] + ".png")
    # we need to store each image into different variable
    # i.e. : here we program will create 3 times post.png (once for every loop iteration)

# Changes done !
# 1. added city variable
# 2. changed the URL (we got our URL from API doc page of the OpenWeatherMap API)