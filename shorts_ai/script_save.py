import os
import re

def script_save(script,topic):
    topic = re.sub(r'[\\/:*?"<>|]', '_', topic)
    output_dir = f"./{topic}"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{topic}.txt")
    with open(file_path, "wb") as f:
        f.write(script.encode("utf-8"))