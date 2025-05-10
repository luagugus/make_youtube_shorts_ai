# make_youtube_shorts_ai

# 🤖 YouTube Shorts 자동 생성기

AI 기반으로 유튜브 쇼츠 콘텐츠를 자동 생성하는 스트림릿 앱입니다.  
GPT를 사용해 스크립트를 작성하고, Typecast를 통해 음성을 생성하며, 배경음악 및 이미지 삽입 기능도 제공합니다.

---

## 🔧 주요 기능

- 🎯 주제 수동 입력 또는 AI 자동 추천
- ✍️ GPT 기반 쇼츠용 스크립트 생성
- 🔊 Typecast API 기반 음성 생성
- 🎵 배경음악 드래그 앤 드롭
- 🖼️ 이미지 생성 여부 및 생성 주기 설정 (예정)
- 🌐 다국어 지원 (한국어, 영어 등)

---

## 🚀 실행 방법

### 📌 1. 저장소 클론
```bash
git clone https://github.com/luagugus/make_youtube_shorts_ai.git
cd make_youtube_shorts_ai
```

### 📌 2. 가상환경 생성, 실행

🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run run.py
```

🍎 macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run run.py
```


