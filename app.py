st.write("Transformed Data")
            st.dataframe(df.head())  # Display the first few rows with the new columns
            
            # Create an in-memory buffer
            excel_buffer = io.BytesIO()

            # Use Pandas to write the DataFrame to the buffer
            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Transformed Data', index=False)

            excel_buffer.seek(0)

            # Create a download button
            st.download_button(
                label="Download Transformed Data as Excel",
                data=excel_buffer,
                file_name="transformed_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
