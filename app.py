import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
@st.cache
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    data = pd.read_csv(url, sep=';')
    return data

data = load_data()

# Streamlit app title
st.title("Explorateur de la qualité des vins : faites des comparaisons entre les vins, sans avoir le mal de crâne ^^")

# Explication de l'application
st.markdown("""
Cette application vous permet d'explorer les données sur la qualité des vins rouges.
Vous pouvez filtrer les vins en fonction de différentes caractéristiques à l'aide des curseurs sur le côté.

### Comment utiliser les curseurs :
- **Aciditey**: Filtrez les vins selon leur acidité volatile, qui peut influencer la perception d'arômes désagréables.
- **Alcool**: Ajustez la plage du taux d'alcool des vins que vous souhaitez examiner.
- **Qualitey**: Ajustez la qualité souhaitée. Le tableau sera filtré en conséquence.
""")

# Sidebar for user inputs
st.sidebar.header("Filter Options")

# Create sliders for user input
acidity = st.sidebar.slider("Aciditey", 4.6, 14.0, (5.0, 10.0))
alcohol = st.sidebar.slider("Alcool (%)", 8.0, 14.0, (9.0, 12.0))
quality = st.sidebar.slider("Qualitey", 3, 8, (5, 7))

# Filter data based on user input
filtered_data = data[
    (data['fixed acidity'].between(acidity[0], acidity[1])) &
    (data['alcohol'].between(alcohol[0], alcohol[1])) &
    (data['quality'].between(quality[0], quality[1]))
]

# Display results
st.write(f"Filtered Wines: {filtered_data.shape[0]}")
st.dataframe(filtered_data)


# Visualize the distribution of wine quality
plt.figure(figsize=(10, 5))
plt.hist(data['quality'], bins=range(3, 9), alpha=0.7, color='red', edgecolor='black')
plt.title('Distribution des vins de qualité')
plt.xlabel('Qualité')
plt.ylabel('Fréquence')
st.pyplot(plt)
