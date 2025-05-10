
from openai import OpenAI
import os



def generate_script(topic, api, model, lang):
    client = OpenAI(api_key= api)
    prompt = f"""
    주제: {topic}
    너는 유명 쇼츠 정보 크리에이터야, 이 주제에 대해 20~25초 길이로 유익하면서 쇼츠용으로 흥미롭게 스크립트를 만들어줘. / ex) '몽골인들이 새우를 극혐하는 이유, 일하다가 다같이 과자사와서 풀어놓고 먹고있는데 몽골 친구 한명이 새우깡에는 절대로 손을 안댐 저거 왜 안먹냐고하니까 새우깡 보면서 이거 뭐냐고 함 몽골인이 갑자기 벌레라고 놀람, 알아보니까 몽골인들은 새우를 잘먹지 않는다함' / 이런말투와 느낌으로,  또한 줄임말이나 강조용 아주 약간의 비속어 이용도 추가해서, 암? 함 처럼 반말을 써야해 무조건. 그리고 무조건 {lang} 언어를 이용해 스크립트를 만들어 필수야!
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()
