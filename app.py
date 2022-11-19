# 16.11.2022, Sergii Logosha, sergiilogosha@gmail.com
# Last modified: 19.11.2022

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
    astros = astro_dict["people"]
    return [item["name"] for item in astros]


@app.route('/astro/craft/<craft_name>')
def craft_crew(craft_name):
    craft_list = astro_dict["people"]
    return [item["name"] for item in craft_list if item["craft"] == craft_name]


if __name__ == '__main__':
    app.run()
