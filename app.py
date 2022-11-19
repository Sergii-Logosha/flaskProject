# 16.11.2022, Sergii Logosha, sergiilogosha@gmail.com
# Last modified: 18.11.2022

from flask import Flask
from urllib.request import urlopen
import json

url = "http://api.open-notify.org/astros.json"
page = urlopen(url)
page = page.read()
page = page.decode("utf-8")
astro_dict = json.loads(page)

app = Flask(__name__)


@app.route('/astro/list')
def astro_list():
    astro_list = astro_dict["people"]
    list_of_astronauts = []
    for item in astro_list:
        list_of_astronauts.append(item["name"])
    return list_of_astronauts


@app.route('/astro/craft/<craft_name>')
def craft_crew(craft_name):
    craft_list = astro_dict["people"]
    crew_list = []
    for item in craft_list:
        if item["craft"] == craft_name:
            crew_list.append(item["name"])
    return crew_list


if __name__ == '__main__':
    app.run()
