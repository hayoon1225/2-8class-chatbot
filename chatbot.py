# 📚 우리 반 도우미 챗봇 (한국 시간 적용 버전)

from datetime import datetime, timedelta, timezone
import random
import streamlit as st

# 🌟 한국 시간대 설정 (UTC+9)
KST = timezone(timedelta(hours=9))
today_str = datetime.now(KST).date().isoformat()

# 🌟 급식 데이터
meals = {
    "2025-06-11": "곤드레나물밥, 유부우동국, 양배추샐러드, 단무지무침, 등심돈까스, 설레임, 수박",
    "2025-06-12": "찰보리밥, 콩나물무채국, 매운감자조림, 치킨스테이크, 열무김치, 요플레",
    "2025-06-16": "차수수밥, 들깨미역국, 돼지고기김치볶음, 계맛살오이냉채, 멜론사, 깻잎김치, 자두주스",
    "2025-06-17": "찰보리밥, 된장찌개, 삼치구이, 취나물무침, 로제떡볶이, 배추김치, 아이스크림",
    "2025-06-18": "투움바파스타, 마늘빵, 오이피클, 무장아찌무침, 양상추샐러드, 새우춘권튀김, 콩나물밥",
    "2025-06-19": "쇠고기강된장, 시금치나물, 토마토달걀찜, 매운돼지불고기, 배추김치, 검은콩우유",
    "2025-06-20": "찰보리밥, 콩국수, 오이지무침, 감자고추장볶음, 등갈비구이, 열무김치, 수박",
    "2025-06-24": "현미잡밥, 건새우근대된장국, 청경채된장무침, 우렁쌈장상추쌈, 미역줄기볶음, 배추겉절이, 수박",
    "2025-06-25": "깍두기볶음밥, 황도양상추샐러드, 바베큐로스트치킨, 백김치, 우유&귤빵, 미숫가루",
    "2025-06-26": "찰보리밥, 김치콩나물국, 숙주된장무침, 마라맛떡볶이, 치킨텐더, 총각김치, 두유",
    "2025-06-27": "차수수밥, 도토리묵사발, 닭갈비, 꽈리고추멸치볶음, 츄러스, 배추김치, 농축요구르트",
    "2025-06-30": "흑미밥, 닭곰탕, 도라지오이무침, 들기름두부구이, 소떡소떡, 갓김치, 피크닉"
}

# 🌟 시험 시간표 (2학년)
exam_schedule = """📚 2025학년도 1학기 2차 지필평가 시간표 (2학년)

6월 30일(월)
- 1교시: 진로영어 / 자습
- 2교시: 동아시아사 / 자습
- 3교시: 수학 I

7월 1일(화)
- 1교시: 경제 / 자습
- 2교시: 생활과윤리 / 자습
- 3교시: 정보 (2학년)

7월 2일(수)
- 1교시: 물리학 I / 자습
- 2교시: 국어의 기본 I
- 3교시: 생명과학 I

7월 3일(목)
- 1교시: 통합과학
- 2교시: 문학

7월 4일(금)
- 1교시: 영어 I
- 2교시: 한국사
"""

# 🌟 과학 퀴즈
science_quizzes = [
    {"question": "물이 100도에서 끓는 이유는?", "answer": "기압 하에서 물의 증기압이 대기압과 같아지기 때문"},
    {"question": "태양은 무슨 별인가요?", "answer": "항성"},
    {"question": "지구 대기의 가장 많은 기체는?", "answer": "질소"},
    {"question": "DNA는 무엇의 약자일까요?", "answer": "Deoxyribonucleic Acid"},
    {"question": "소리보다 빛이 빠른 이유는?", "answer": "빛은 진공에서도 전달되고, 소리는 매질이 있어야 해서"}
]

# 오늘 급식 가져오기
today_meal = meals.get(today_str, "오늘은 급식 정보가 없어요. (주말이거나 데이터가 없을 수 있어요.)")

# 과학 퀴즈 랜덤 1문제
quiz = random.choice(science_quizzes)

# 🌟 Streamlit 앱 시작
st.title("📚 우리 반 도우미 챗봇")

# 사용자 입력 받기
user_input = st.text_input("👤 하고 싶은 말을 입력해 보세요:")

# 응답 처리
if user_input:
    lowered = user_input.lower()

    # 급식 기능
    if any(keyword in lowered for keyword in ["급식", "오늘 급식", "오늘 점심"]):
        st.markdown(f"🍱 오늘({today_str})의 급식:\n\n{today_meal}")

    # 시험 시간표 기능
    elif any(keyword in lowered for keyword in ["시험", "시험 시간표"]):
        st.markdown(f"📝 시험 시간표 안내:\n\n{exam_schedule}")

    # 과학 퀴즈 기능
    elif any(keyword in lowered for keyword in ["퀴즈", "과학", "문제"]):
        st.markdown(f"🧪 과학 퀴즈!\n\n**Q. {quiz['question']}**\n\n(정답: ||{quiz['answer']}||)")

    elif any(keyword in lowered for keyword in ["돼지"]):
        st.markdown("꿀꿀")

    # 기타
    else:
        st.markdown("🤖 미안, 아직 그 질문은 잘 몰라. '급식', '시험', '퀴즈' 같은 말을 써볼래?")
