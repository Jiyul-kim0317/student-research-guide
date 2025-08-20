# main.py
import streamlit as st

st.set_page_config(page_title="학생 탐구·생기부 가이드", layout="wide")
st.title("📚 학생 탐구·생기부 가이드")
st.markdown("학생들의 주제탐구와 생기부 관리를 돕는 사이트와 활용 팁 모음입니다.")

# 사이트 정보 (설명과 활용 팁 포함)
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
    "논문 사이트": {
        "RISS": {
            "link": "http://www.riss.kr/",
            "desc": "논문과 학술자료 검색에 최적화, 탐구 주제 자료 수집에 유용."
        },
        "사이언스온": {
            "link": "https://scienceon.kisti.re.kr/",
            "desc": "과학 관련 뉴스와 자료 제공, 탐구 주제 아이디어 확보 가능."
        },
        "빅카인즈": {
            "link": "https://www.bigkinds.or.kr/",
            "desc": "언론 기사 검색 플랫폼, 사회/시사 주제 탐구에 유용."
        },
        "사이언스타임즈": {
            "link": "https://www.sciencetimes.co.kr/",
            "desc": "과학 뉴스와 트렌드 확인 가능, 탐구 주제 아이디어 수집."
        }
    },
    "학술 검색": {
        "Google 학술 검색": {
            "link": "https://scholar.google.com/",
            "desc": "논문, 학술 자료 검색, 탐구 주제 자료 조사에 활용."
        },
        "NAVER Academic": {
            "link": "https://academic.naver.com/",
            "desc": "한국어 논문과 학술 자료 검색, 탐구 주제 자료 수집에 적합."
        }
    },
    "강의 사이트": {
        "KOCW": {
            "link": "http://www.kocw.net/",
            "desc": "대학 강의 동영상 제공, 주제탐구 보충 학습에 유용."
        },
        "K-MOOC": {
            "link": "https://www.kmooc.kr/",
            "desc": "온라인 공개 강좌 플랫폼, 탐구 주제 관련 심화 학습 가능."
        }
    },
    "AI 도구": {
        "ChatGPT": {
            "link": "https://chat.openai.com/",
            "desc": "탐구 주제 아이디어, 글쓰기 도움, 자료 정리 지원."
        },
        "Perplexity": {
            "link": "https://www.perplexity.ai/",
            "desc": "질문 기반 정보 검색, 탐구 자료 요약 활용 가능."
        },
        "Felo": {
            "link": "https://felo.ai/",
            "desc": "AI 기반 글쓰기/정리 도구, 탐구 기록 작성에 도움."
        },
        "Lilys AI": {
            "link": "https://lilys.ai/",
            "desc": "AI 학습 도우미, 탐구 아이디어 정리와 참고 자료 제공."
        },
        "NotebookLM": {
            "link": "https://notebooklm.google/",
            "desc": "AI 노트북, 탐구 기록과 분석에 활용 가능."
        }
    },
    "발표자료": {
        "Canva": {
            "link": "https://www.canva.com/",
            "desc": "디자인 중심 프레젠테이션 제작, 탐구 결과 발표용."
        },
        "MiriCanvas": {
            "link": "https://www.miricanvas.com/",
            "desc": "웹 기반 발표 자료 제작, 시각적 자료 편집 용이."
        },
        "Google Slides": {
            "link": "https://slides.google.com/",
            "desc": "온라인 프레젠테이션 제작, 협업 가능."
        }
    },
    "교과서": {
        "비상교육 교재": {
            "link": "https://book.visang.com/",
            "desc": "학교 교과서와 참고서 확인, 탐구 주제 이해에 활용."
        }
    }
}

# 사이트 표시
for category, sites in categories.items():
    st.header(f"📂 {category}")
    for name, info in sites.items():
        with st.expander(name):
            st.write(info["desc"])
            st.markdown(f"[사이트 바로가기]({info['link']})")
    st.markdown("---")
