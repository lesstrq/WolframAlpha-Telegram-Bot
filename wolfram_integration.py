import requests
from config import WOLFRAM_APP_ID
from PIL import Image
from io import BytesIO
import urllib.parse

BASE_URL = "https://api.wolframalpha.com/v1/simple?i={}&appid={}"

def get_wolfram_response(query):
    response = requests.get(get_link(query)).content
    image = Image.open(BytesIO(response))
    image.save("test.png")

def get_link(query):
    return BASE_URL.format(urllib.parse.quote(query), WOLFRAM_APP_ID)


# get_wolfram_response(input())
