import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    df = pd.read_csv("./data/profile.csv", parse_dates=["birthdate"]).dropna()
    return df



def main():
    st.title("data Display st.data_editor()")
    data = load_data()
    st.data_editor(data)
  


if __name__ == "__main__":
    main()