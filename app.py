import streamlit as st
import pandas as pd
from collections import Counter



# Function to categorize age
def categorize_age(age):
    if age < 5:
        return "<5"
    elif 5 <= age <= 14:
        return "5-14"
    else:
        return ">15"

# Function to standardize gender
def standardize_gender(gender):
    if pd.isna(gender):
        return None
    gender = gender.strip().lower()
    if gender in ['male', 'm']:
        return 'Male'
    elif gender in ['female', 'f']:
        return 'Female'
    else:
        return None

# Streamlit app
def main():
    st.title("Data Cleaning and Transformation App")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            try:
                df = pd.read_excel(uploaded_file)
            except Exception as e:
                st.error(f"Error reading file: {e}")
                return

        st.write("Original Dataframe")
        st.dataframe(df)

        # Variable transformation
        st.header("Variable Transformation")
        variable_name = st.selectbox("Select a variable to transform", df.columns)
        if st.button("Transform Variable"):
            # Split the comma-separated values and get unique values
            all_values = df[variable_name].dropna().str.split(', ', expand=False).sum()
            unique_values = sorted(list(set(all_values)))

            # Create new columns for each unique value
            for value in unique_values:
                df[value] = df[variable_name].apply(lambda x: 1 if value in str(x).split(', ') else 0)

            st.write("Transformed Data")
            st.dataframe(df.head())  # Display the first few rows with the new columns
        
        # Age categorization
        st.header("Age Categorization")
        if 'age' in df.columns:
            df['age_category'] = df['age'].apply(categorize_age)
            st.write("Age Categorized Data")
            st.dataframe(df[['age', 'age_category']].head())
        else:
            st.write("No 'age' column found.")

        # Gender standardization
        st.header("Gender Standardization")
        if 'gender' in df.columns:
            df['gender_standardized'] = df['gender'].apply(standardize_gender)
            st.write("Gender Standardized Data")
            st.dataframe(df[['gender', 'gender_standardized']].head())
        else:
            st.write("No 'gender' column found.")

if __name__ == "__main__":
    main()
