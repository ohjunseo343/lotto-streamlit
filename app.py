import streamlit as st
import random

st.set_page_config(page_title="1~20 랜덤 숫자", page_icon="🎲", layout="centered")
st.title("🎲 1~20 랜덤한 횟수 뽑기")
st.markdown("버튼을 누르면 1~20 사이의 숫자가 랜덤으로 나옵니다! 나온 수 만큼 해야할 일을 해 봐요!")

# 버튼 클릭 이벤트
if st.button("숫자 뽑기"):
    num = random.randint(1, 20)
    st.success(f"🎯 결과: {num}")
else:
    st.caption("버튼을 눌러 숫자를 뽑아보세요!")
