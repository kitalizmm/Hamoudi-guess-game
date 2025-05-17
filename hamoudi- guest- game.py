import streamlit as st
import random


st.title("لعبة تخمين الرقم")
st.write("أنا مخبي رقم من 1 إلى 10، حاول تخمنه!")


if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)


guess = st.number_input("اكتب رقمك:", min_value=1, max_value=10, step=1)


if st.button("خمن"):
    if guess == st.session_state.secret:
        st.success("برافو! خمنت الرقم صح")
        st.session_state.secret = random.randint(1, 10)
    else:
        st.error("غلط! حاول تاني")