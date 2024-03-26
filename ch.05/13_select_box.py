import pandas as pd
import streamlit as st
import seaborn as sns


@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df


def main():
    st.title("Select Box")
    iris = load_data()
    st.markdown('## Raw Data')
    st.dataframe(iris)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("## Select")
    val = st.selectbox("select 1 sp", iris.species.unique())
    st.write("선택된 species : ", val)
    st.dataframe(iris.loc[iris['species']==val, :].reset_index(drop=True))
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("## MultiSelect")
    cols = st.multiselect("select multiple cols", iris.columns)
    st.write("선택된 columns : ", cols)
    st.dataframe(iris.loc[:, cols])

if __name__ == '__main__':
    main()