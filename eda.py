
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib as plt

# Load the dataset
@st.cache_data
def load_data():
    # Replace 'bank_customer_churn.csv' with the path to your dataset
    data = pd.read_csv("notebook/data/Churn_Modelling.csv")
    return data

data = load_data()

# Display the dataset
st.title("🛡️🏦 BankShield : Customer Churn Prediction EDA")
st.write("### Dataset")
st.write(data.head())

# Display basic information
st.write("### Basic Information")
st.write(data.describe())

# Display the distribution of the target variable (Exited)
st.write("### Distribution of Churn (Exited)")
category_counts = data["Exited"].value_counts()
st.bar_chart(category_counts)

# Geography
st.subheader("Geography Distribution")
geo_counts = data["Geography"].value_counts()
fig = px.pie(data, values=geo_counts.values, names=geo_counts.index,
             color_discrete_sequence=px.colors.sequential.Purp,
             opacity=0.9, hole=0.3)
st.plotly_chart(fig)


def age_group(age):
    if age < 10:
        return '0-10'
    elif age < 20:
        return '10-20'
    elif age < 30:
        return '20-30'
    elif age < 40:
        return '30-40'
    elif age < 50:
        return '40-50'
    elif age < 60:
        return '50-60'
    elif age < 70:
        return '60-70'
    elif age < 80:
        return '70-80'
    elif age < 90:
        return '80-90'
    else:
        return '90+'

# Apply the function to create a new 'AgeGroup' column
data['AgeGroup'] = data['Age'].apply(age_group)

# Count the number of occurrences in each age group
age_group_counts = data['AgeGroup'].value_counts().sort_index()

# Create a pie chart
fig = px.pie(data, values=age_group_counts.values, names=age_group_counts.index,
             color_discrete_sequence=px.colors.sequential.Mint,
             opacity=0.9, hole=0.3)

# Display the chart in Streamlit
st.subheader("Age Group Distribution")
st.plotly_chart(fig)


fig = px.bar(data, x=age_group_counts.index, y=age_group_counts.values,
             color=age_group_counts.index, color_discrete_sequence=px.colors.sequential.RdBu,
             opacity=0.9, labels={'x': 'Age Group', 'y': 'Count'},
             title='Age Distribution')

st.plotly_chart(fig)


# Count the number of occurrences of each age
age_counts = data['Age'].value_counts().sort_index()

# Create a line chart
fig = px.line(x=age_counts.index, y=age_counts.values,
              labels={'x': 'Age', 'y': 'Count'},
              title='Age Distribution')

# Display the line chart in Streamlit
st.subheader("Age Distribution Line Chart")
st.plotly_chart(fig)


st.subheader("Distribution of features using bar chart")
# Create a line chart
fig = px.bar(x=age_counts.index, y=age_counts.values,
              labels={'x': 'Age', 'y': 'Count'},
              color=age_counts.index, 
            #   color_discrete_sequence=px.colors.sequential.BuPu,
              title='1) Age Distribution')

# Display the line chart in Streamlit
st.plotly_chart(fig)


CreditScore_counts = data['CreditScore'].value_counts().sort_index()
# Create a line chart
fig = px.bar(x=CreditScore_counts.index, y=CreditScore_counts.values,
              labels={'x': 'Credit Score', 'y': 'Count'},
              color=CreditScore_counts.index, 
            #   color_discrete_sequence=px.colors.sequential.BuPu,
              title='2) Credit Score Distribution')

# Display the line chart in Streamlit
st.plotly_chart(fig)


# Visualize the distribution of Geography
st.write("### Distribution of Categorical Features and Churn")

fig_geography = px.histogram(
    data, 
    x='Geography', 
    title='1) Geography and Churn', 
    color='Exited', 
    barmode='group',
    color_discrete_sequence=['#f9d0de', '#ef74a0']
)
st.plotly_chart(fig_geography)


# Visualize the distribution of Gender
fig_gender = px.histogram(
    data, 
    x='Gender', 
    title='2) Gender and Churn', 
    color='Exited', 
    barmode='group',
    color_discrete_sequence=['#b8b1cc', '#716399']
)
st.plotly_chart(fig_gender)


st.write("### Distribution of Numerical Features and Churn")

option = st.selectbox(
    "Select distribution entity?",
    ("HasCrCard", "IsActiveMember"))


category_counts = data[option].value_counts()
st.bar_chart(category_counts)


# Visualize relationships between features and churn
st.write("### Box plots for Relationships between Features and Churn")

# Credit Score vs Churn
fig = px.box(data, x='Exited', y='CreditScore', title='Credit Score vs Churn')
st.plotly_chart(fig)

# Age vs Churn
fig = px.box(data, x='Exited', y='Age', title='Age vs Churn')
st.plotly_chart(fig)

# Balance vs Churn
fig = px.box(data, x='Exited', y='Balance', title='Balance vs Churn')
st.plotly_chart(fig)

# Tenure vs Churn
fig = px.box(data, x='Exited', y='Tenure', title='Tenure vs Churn')
st.plotly_chart(fig)

# NumOfProducts vs Churn
fig = px.box(data, x='Exited', y='NumOfProducts', title='Num Of Products vs Churn')
st.plotly_chart(fig)

# EstimatedSalary vs Churn
fig = px.box(data, x='Exited', y='EstimatedSalary', title='Estimated Salary vs Churn')
st.plotly_chart(fig)




# Correlation heatmap
numeric_data = data.select_dtypes(include=['float64', 'int64'])

corr_matrix = numeric_data.corr()

# Plotting the correlation heatmap
fig = go.Figure(data=go.Heatmap(
                   z=corr_matrix.values,
                   x=corr_matrix.columns,
                   y=corr_matrix.index,
                   colorscale='tempo_r'))
fig.update_layout(title='Correlation Heatmap')

# Display the chart in Streamlit
st.write("### Correlation Heatmap")
st.plotly_chart(fig)