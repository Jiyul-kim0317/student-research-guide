import streamlit as st

st.set_page_config(page_title="학생 탐구·생기부 가이드", layout="wide")
st.title("📚 학생 탐구·생기부 가이드")
st.markdown("학생들의 주제탐구와 생기부 관리를 돕는 사이트와 활용 팁 모음입니다.")

# 사이트 정보 (대학 홈페이지 포함, 설명/활용 팁 포함)
categories = {
    "대학 홈페이지": {
        "서울대학교": {
            "link": "https://www.snu.ac.kr/",
            "desc": "서울대학교 공식 홈페이지, 대학 정보와 학과 안내 확인 가능."
        },
        "서울대학교 입학처": {
            "link": "https://admission.snu.ac.kr/",
            "desc": "서울대 입학 관련 정보를 제공, 학과 소개와 입시 요강 확인 가능."
        },
        "고려대학교": {
            "link": "https://www.korea.ac.kr/",
            "desc": "고려대학교 공식 홈페이지, 대학 정보와 학과 안내 확인 가능."
        },
        "고려대학교 입학처": {
            "link": "https://oku.korea.ac.kr/",
            "desc": "고려대 입학처 공식 사이트, 입학 전형과 학사 안내 확인 가능."
        },
        "연세대학교": {
            "link": "https://www.yonsei.ac.kr/",
            "desc": "연세대학교 공식 홈페이지, 대학 정보와 학과 안내 확인 가능."
        },
        "연세대학교 입학처": {
            "link": "https://admission.yonsei.ac.kr/",
            "desc": "연세대 입학 정보 제공, 학과별 안내와 지원 방법 확인 가능."
        },
        "성균관대학교": {
            "link": "https://www.skku.edu/",
            "desc": "성균관대학교 공식 홈페이지, 대학 정보와 학과 안내 확인 가능."
        },
        "성균관대학교 입학처": {
            "link": "https://admission.skku.edu/",
            "desc": "성균관대 입시 안내 사이트, 전형 정보와 학사 자료 제공."
        },
        "KAIST": {
            "link": "https://www.kaist.ac.kr/",
            "desc": "KAIST 공식 홈페이지, 대학 정보와 학과 안내 확인 가능."
        },
        "KAIST 입학처": {
            "link": "https://admission.kaist.ac.kr/",
            "desc": "KAIST 입학 안내 사이트, 학과 소개와 전형 일정 확인 가능."
        }
    },
    # 추가 카테고리(논문, 학술검색, AI 등)도 이전과 동일하게 삽입 가능
}

# 카테고리별 사이트 표시
for category, sites in categories.items():
    st.header(f"📂 {category}")
    for name, info in sites.items():
        with st.expander(name):
            st.write(info["desc"])
            st.markdown(f"[사이트 바로가기]({info['link']})")
    st.markdown("---")
