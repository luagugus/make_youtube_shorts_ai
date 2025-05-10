import requests
import time
import os
import re
import time
import wave

    
def generate_voice(script, topic,typeapi_key):
    API_TOKEN = typeapi_key
    ACTOR_ID = "6059dad0b83880769a50502f"
    SCRIPT_TEXT = script
    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }


    speak_response = requests.post(
        "https://typecast.ai/api/speak",
        headers=HEADERS,
        json={
            "text": SCRIPT_TEXT,
            "lang": "ko",
            "tempo": 1.2,
            "pitch": 1,
            "actor_id": ACTOR_ID,
            "model_version": "latest",
            "xapi_hd": True
        }
    )
    speak_response.raise_for_status()
    speak_id = speak_response.json()["result"]["speak_v2_url"].split("/")[-1]


    status_url = f"https://typecast.ai/api/speak/v2/{speak_id}"
    while True:
        status_response = requests.get(status_url, headers=HEADERS)
        status_response.raise_for_status()
        status_data = status_response.json()["result"]
        if status_data["status"] == "done":
            audio_url = status_data["audio_download_url"]
            break
        time.sleep(1)

    topic = re.sub(r'[\\/:*?"<>|]', '_', topic)
    audio_response = requests.get(audio_url)
    output_dir = f"./{topic}"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{topic}.wav")



    with open(file_path, "wb") as f:
        f.write(audio_response.content)


    with wave.open(file_path, 'rb') as wf:
        frames = wf.getnframes()
        rate   = wf.getframerate()
        duration = frames / float(rate)

    return duration
    