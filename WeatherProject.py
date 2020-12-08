import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "d407e1cdc0c8ec267d808bc0038c9b09"  # Update Your API Here
position = [300, 430, 555, 690, 825]

us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]
famous_cities1 = ["Paris", "London", "Hong Kong", "Rome", "Tokyo"]
famous_cities2 = ["Shanghai", "Beijing", "Moscow", "Venice", "Berlin"]
country_list = [us_list, famous_cities1, famous_cities2]

save_number = 1

for country in country_list:
    image = Image.open("post.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Inter.ttf", size=50)
    content = "Latest Weather Forecast"
    color = "rgb(255, 255, 255)"
    (x, y) = (46, 77)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype("Inter.ttf", size=30)
    today = date.today()
    content = date.today().strftime("%A - %B %d, %Y")
    color = "rgb(255, 255, 255)"
    (x, y) = (46, 145)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        # city
        font = ImageFont.truetype('Inter.ttf', size=50)
        color = 'rgb(0, 0, 0)'
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        # temp
        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255, 255, 255)'
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        # humidity
        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(255, 255, 255)'
        (x, y) = (810, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1

    image.show()
    image.save(str(date.today()) + " Image Number " + str(save_number) + ".png")
    save_number += 1
