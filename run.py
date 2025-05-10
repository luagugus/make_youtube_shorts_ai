from shorts_ai import shorts_ai
import streamlit as st
from pathlib import Path
import time





st.set_page_config(page_title="📹 YouTube Shorts 자동 생성기", menu_items={
    'About': "Made by [YourName] - [GitHub](https://github.com/yourgithub) | [후원하기](https://buymeacoffee.com/yourlink)"
})


with st.sidebar:
    st.header("🔧 설정 메뉴")
    openai_key = st.text_input("OpenAI API Key", type="password")
    typeapi_key = st.text_input("Typescript API Key", type="password")
    lang = st.selectbox("언어 설정", ["한국어", "English", "日本語", "Español"])
    gpt_model = st.selectbox("GPT 모델", ["gpt-4o", "gpt-4o-mini", "gpt-4"])
    ai_topic_search = st.checkbox("AI가 주제 자동 추천", value=True)
    topic = ""
    if not ai_topic_search:
        topic = st.text_input("주제 입력")
    
    st.markdown("---")
    st.subheader("🎨 이미지 생성")
    img_generate = st.checkbox("이미지 생성 ON/OFF", value=True)
    img_interval = st.slider("이미지 생성 주기 (초)", min_value=1, max_value=10, value=3)

    #st.markdown("---")
    #st.subheader("🎵 배경음악 업로드")
    #bgm_file = st.file_uploader("배경음악 파일 드래그 또는 선택", type=["mp3", "wav"])


st.title("🤖 유튜브 쇼츠 자동 생성기")
st.write("OpenAI API와 미디어 툴을 활용한 쇼츠 자동 제작 플랫폼")

if st.button("🚀 생성 시작"):
    if not openai_key:
        st.warning("⚠️ OpenAI API 키를 입력해주세요.")
    else:
        st.success("✅ 설정 완료! 자동 생성 시작")

        progress = st.progress(0)
        status_text = st.empty()

        status_text.info("📌 [1/3] 주제 수집 중...")
        time.sleep(1.5)
        if ai_topic_search:
            topic_result = shorts_ai.generate_topic(openai_key, gpt_model)
        else:
            topic_result = topic
        st.write(f"🎯 선택된 주제: **{topic_result}**")
        progress.progress(33)


        status_text.info("✍️ [2/3] 스크립트 생성 중 (GPT)")
        time.sleep(1.5)
        script = shorts_ai.generate_scripts(topic_result, openai_key, gpt_model, lang)
        progress.progress(66)


        status_text.info("🎬 [3/3] 음성 제작 및 이미지 제작 중...")
        time.sleep(2)
        length = shorts_ai.generate_voice(script, topic_result, typeapi_key)
        st.write("🎧 음성 제작 완료")
        time.sleep(0.1)
        if img_generate:
            shorts_ai.generate_img(openai_key, script, img_interval,topic_result,length)
            time.sleep(1)
            st.write("🖼️ 이미지 생성 완료")
        


        status_text.success("✅ 자동 생성 완료!")
        progress.progress(100)


