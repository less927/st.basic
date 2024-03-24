# -*- coding: utf-8 -*-


import streamlit as st


def main():
    st.title("this is text elements")
    st.header("this is header/헤더")
    st.subheader("this is subheader")
    st.write("파이선 문법 사용가능")
    st.write("-" * 50)
    
    
    
    st.markdown("""
    ### SubChapter 1.
    - 피타고라스 정리 : red[$\sqrt{x^2+y^2}=1$] is Pythagorean identity. :pencil:    
    """)
    

if __name__ == "__main__":
    main()

