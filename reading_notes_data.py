# 14/10/2023
# Kaan Baspinar

# How to use:
# There is a function called findFeature. It takes 3 element which are file_name, find and n respectively.
# "file_name" is the file name of your file (e.g. "TopNotes")
# "find" is the element which you want to filter
# (e.g. "Name" (Name of the perfume) or "Brand" (Brand name of the perfume)).
# n is the row number
# Example can be found after the function block.

# You can use this function by these codes:
# from reading_notes_data import findFeature
# findFeature("BaseNotes", "Brand", n)


import pandas as pd

def findFeature(file_name, find, n):
    csv_file_path = "{}.csv".format(file_name)
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)
    finder = df["Name:Brand:Launched"][n]
    if pd.isna(finder):
        pass
    else:
        finder = finder.split("-*-")
        found = []
        for i in finder:
            i = i.split(":")
            if find == "Name":
                found.append(i[0])
            elif find == "Brand":
                found.append(i[1])
            elif find == "Launched":
                found.append(i[2])
            else:
                print("Check the inputs for the function!")
        return found


print(findFeature("BaseNotes", "Brand", i))



