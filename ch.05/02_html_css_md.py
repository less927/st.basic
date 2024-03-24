# -*- coding: utf-8 -*-


import streamlit as st

def main():
    st.markdown("HTML CSS")
    html_css = """
    <style>
        table.customTable {
            width:100%
            background-color:#FFFFFF;
            border-collapse: collapse;
            border-width: 2px;
            border-color: #7ea8f8;
            border-style: solid;
            color: 000000;
        }
    </style>
    <table class="customTable">
        <thead>
            <tr>
                <th>이름</th>
                <th>나이</th>
                <th>직업</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>35</td>
                <td>glen</td>
                <td>NA</td>
            </tr>
        </tbody>
    </table>           
    """
    st.markdown(html_css, unsafe_allow_html=True)



if __name__ == "__main__":
    main()

