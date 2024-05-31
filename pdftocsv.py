import tabula
import pandas as pd
import getpass

# Specify the path to your PDF file
pdf_path = "./test.pdf"
pdf_password = getpass.getpass(prompt="Enter the PDF password: ")

# Define the output CSV file path
csv_path = "output_tables.csv"

# Extract tables from the PDF file
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, password=pdf_password)

# Combine all tables into a single DataFrame
combined_df = pd.concat(tables, ignore_index=True)

# Save the combined DataFrame as a CSV file
combined_df.to_csv(csv_path, index=False)
print(f"All tables saved in {csv_path}")

# this wiil create page wise tables
# Loop through extracted tables and save each as a CSV file
# for i, table in enumerate(tables):
#     # Convert the table to a DataFrame
#     df = pd.DataFrame(table)
    
#     # Define the output CSV file path
#     csv_path = f"output_table_{i + 1}.csv"
    
#     # Save the DataFrame as a CSV file
#     df.to_csv(csv_path, index=False)

#     print(f"Table {i + 1} saved as {csv_path}")