import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df


def plot_matplotlib(df):
    st.title('Scatter Plot with Matplotlib')
    fig, ax = plt.subplots()
    ax.scatter(df['sepal_length'], df['sepal_width'])
    st.pyplot(fig)
    
def plot_seaborn(df):
    st.title('Scatter Plot with Seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig)
    
def plot_plotly(df):
    st.title('Scatter plot with Ploty')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x = df['sepal_length'],
                   y = df['sepal_width'],
                   mode = 'markers')
    )
    st.plotly_chart(fig)
    
def main():
    st.title("Choose a plotting library")
    iris = load_data()
    st.data_editor(iris)
    
    plot_type = st.radio(
        "which scatter plot",
        ("Matplotlib", "Seaborn", "Plotly"))
    
    st.write(plot_typeimport streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df
)
    
    if plot_type == "Matplotlib":
        plot_matplotlib(iris)
    elif plot_type == "Seaborn":
        plot_seaborn(iris)
    elif plot_type == "Plotly":
        plot_plotly(iris)
    
    
if __name__ == '__main__':
    main()