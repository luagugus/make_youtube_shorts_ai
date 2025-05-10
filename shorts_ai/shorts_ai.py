from .trending import get_trending_topic
from .gpt_script import generate_script
from .voice import generate_voice
from .script_save import script_save
from .img_generation import image_gen

def generate_scripts(topic, api, model, lang):
    a = generate_script(topic, api, model, lang)
    script_save(a, topic)
    return a

def generate_audio(script, topic, api):
    return generate_voice(script,topic, api)

def generate_topic(api, model):
    return get_trending_topic(api, model)

def generate_img(api, script, cycle, topic, len):
    return image_gen(api, script, cycle, topic,len)