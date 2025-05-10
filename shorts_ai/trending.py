
from openai import OpenAI
import os

def get_trending_topic(api, model):
    client = OpenAI(api_key= api)
    prompt = f"""
    유튜브 쇼츠 트렌드에 맞는 주제 하나를 하나 적어(ex) ~가 ~한 이유)(필수. 아무런 부가말 없이 주제만. 난 이걸 다른 ai 프롬프트에 이용할거니까.)
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()