# -*- coding: utf-8 -*-


import streamlit as st
import streamlit.components.v1 as components


def main():
    st.markdown("HTML JS Streamlit")
    js_code = """
    <h3>hi</h3>
    <script>
    function sayHello() {
        alert('Hello from JavaScript in Streamlit Web');
    }
    </script>
    
    <button onclick="sayHello()">click me</button>
    """
    components.html(js_code)


if __name__ == "__main__":
    main()

