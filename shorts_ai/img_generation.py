
import  openai
import requests
import re
import math
def split_string_n_parts(s, n):
    avg = len(s) // n
    return [s[i*avg:(i+1)*avg] for i in range(n-1)] + [s[(n-1)*avg:]]


def image_gen(api, script, cycle, topic, lenth):
    openai.api_key = api
    topic = re.sub(r'[\\/:*?"<>|]', '_', topic)

    count = math.ceil((lenth/cycle))
    
    parts = split_string_n_parts(script, count)

    for i in range(0,count):
        response = openai.images.generate(
            model="dall-e-3",
            prompt=f"{parts[i]}는 내가 쓴 유튜브 쇼츠 대본중 하나인데 이것과 관련된 사진 만들어봐",
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        img_data = requests.get(image_url).content
        with open(f"{topic}/output_{i}.png", "wb") as handler:
            handler.write(img_data)

