        # Variable transformation
        st.header("Variable Transformation")
        variable_name = st.selectbox("Select a variable to transform", df.columns)
        if st.button("Transform Variable"):
            unique_values = df[variable_name].dropna().unique()
            for value in unique_values:
                df[f'{variable_name}_{value}'] = df[variable_name].apply(lambda x: 1 if x == value else 0)
            st.write("Transformed Data")
            st.dataframe(df.head())  # Display the first few rows with the new columns
