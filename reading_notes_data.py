# 14/10/2023
# Kaan Baspinar

# How to use:
# There is a function called findFeature. It takes 3 elements: file_name, find, and n respectively.
# "file_name" is the file name of your file (e.g., "TopNotes").
# "find" is the element which you want to filter
# (e.g., "Name" (Name of the perfume) or "Brand" (Brand name of the perfume)).
# n is the row number.
# Example can be found after the function block.

# You can use this function with these codes:
# from reading_notes_data import findFeature
# findFeature("BaseNotes", "Brand", n)

import pandas as pd

def findFeature(file_name, find, n):
    csv_file_path = "{}.csv".format(file_name)
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)
    # Extract the value from the specified row and column
    finder = df["Name:Brand:Launched"][n]
    # Check if the value is NaN (missing)
    if pd.isna(finder):
        pass  # If it's missing, do nothing
    else:
        finder = finder.split("-*-")  # Split the string into a list based on the separator "-*-"
        found = []
        for i in finder:
            i = i.split(":")  # Split each element in the list based on the separator ":"
            if find == "Name":
                found.append(i[0])  # If finding the name, append the first element to the found list
            elif find == "Brand":
                found.append(i[1])  # If finding the brand, append the second element to the found list
            elif find == "Launched":
                found.append(i[2])  # If finding the launched date, append the third element to the found list
            else:
                print("Check the inputs for the function!")  # If the specified find argument is incorrect, print an error message
        return found  # Return the list of found elements


# Example usage: find the brand from the "BaseNotes" file at row number i
print(findFeature("BaseNotes", "Brand", i))
