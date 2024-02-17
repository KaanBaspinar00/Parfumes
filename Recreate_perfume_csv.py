import pandas as pd

# Specify the input file name and encoding
input_file = "perfume.csv"
input_encoding = "latin-1"

# Read the CSV file with the specified encoding
df = pd.read_csv(input_file, encoding=input_encoding)

# Specify the output file name and encoding
output_file = "perfume2.csv"
output_encoding = "latin-1"

# Write the DataFrame to a new CSV file with the specified encoding
df.to_csv(output_file, encoding=output_encoding, index=False)

print(f"File '{input_file}' has been read with '{input_encoding}' encoding and written to '{output_file}' with '{output_encoding}' encoding.")
