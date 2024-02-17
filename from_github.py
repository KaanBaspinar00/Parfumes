import numpy as np
import pandas as pd

# Define the path to your CSV file
csv_file_path = "perfume2.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

TopNotesList = []
MiddleNotesList = []
BaseNotesList = []
all_scents = []
for i in df["TopNotes"]:
    all_scents.append(str(i).split(" / "))
    TopNotesList.append(str(i).split(" / "))


for i in df["MiddleNotes"]:
    all_scents.append(str(i).split(" / "))
    MiddleNotesList.append(str(i).split(" / "))

for i in df["BaseNotes"]:
    all_scents.append(str(i).split(" / "))
    BaseNotesList.append(str(i).split(" / "))


all_scents_flatten = list(set([item for sublist in all_scents for item in sublist]))
all_scents_clear = []

for i in all_scents_flatten:
    if i == "":
        pass
    else:
        all_scents_clear.append(i)



all_scents_clear = np.array(all_scents_clear)
TopNotesList2 = []
MiddleNotesList2 = []
BaseNotesList2 = []

for scent in all_scents_clear:
    per_scent_top =[]
    per_scent_middle = []
    per_scent_base = []
    for notes in range(0,len(df["TopNotes"])-1):
        if scent in TopNotesList[notes]:
            list_for_scent = ["{}:{}:{}".format(df["Name"][notes],df["Company"][notes],df["Launched"][notes])]
            per_scent_top.append(list_for_scent)

        if scent in MiddleNotesList[notes]:
            list_for_scent = ["{}:{}:{}".format(df["Name"][notes], df["Company"][notes], df["Launched"][notes])]
            per_scent_middle.append(list_for_scent)

        if scent in BaseNotesList[notes]:
            list_for_scent = ["{}:{}:{}".format(df["Name"][notes], df["Company"][notes], df["Launched"][notes])]
            per_scent_base.append(list_for_scent)

    if len(per_scent_top) == 0:
        per_scent_top = ""
        TopNotesList2.append(per_scent_top)
    else:
        per_scent_top = np.array(per_scent_top)
        per_scent_top = str("-*-".join(["//".join(item) for item in per_scent_top]))
        TopNotesList2.append(per_scent_top)

    if len(per_scent_middle) == 0:
        per_scent_middle = ""
        MiddleNotesList2.append(per_scent_middle)
    else:
        per_scent_middle = np.array(per_scent_middle)
        per_scent_middle = str("-*-".join(["//".join(item) for item in per_scent_middle]))
        MiddleNotesList2.append(per_scent_middle)

    if len(per_scent_base) == 0:
        per_scent_base = ""
        BaseNotesList2.append(per_scent_base)
    else:
        per_scent_base = np.array(per_scent_base)
        per_scent_base = str("-*-".join(["//".join(item) for item in per_scent_base]))
        BaseNotesList2.append(per_scent_base)

all_scents_clear = np.reshape(all_scents_clear,(557,1))
"""
print(all_scents_clear[0:50])
print(all_scents_clear[50:100])
print(all_scents_clear[100:150])
print(all_scents_clear[150:200])
print(all_scents_clear[200:250])
print(all_scents_clear[250:300])
print(all_scents_clear[300:350])
print(all_scents_clear[350:400])
print(all_scents_clear[400:450])
print(all_scents_clear[450:500])
print(all_scents_clear[500:556])
"""
TopNotesList2 = np.reshape(np.array(TopNotesList2),(557,1))
MiddleNotesList2 = np.reshape(np.array(MiddleNotesList2),(557,1))
BaseNotesList2 = np.reshape(np.array(BaseNotesList2),(557,1))

# Reshape the data to make them 1-dimensional
all_scents_clear_1d = [item[0] for item in all_scents_clear]
TopNotesList2_1d = [item[0] for item in TopNotesList2]
MiddleNotesList2_1d = [item[0] for item in MiddleNotesList2]
BaseNotesList2_1d = [item[0] for item in BaseNotesList2]


df_top = pd.DataFrame({'Fragrance': all_scents_clear_1d, 'Name:Brand:Launched': TopNotesList2_1d})
df_top.to_csv("TopNotes.csv",index=False)
#print(df_top)

df_middle = pd.DataFrame({'Fragrance': all_scents_clear_1d, 'Name:Brand:Launched': MiddleNotesList2_1d})
df_top.to_csv("MiddleNotes.csv",index=False)
#print(df_middle)

df_base = pd.DataFrame({'Fragrance': all_scents_clear_1d, 'Name:Brand:Launched': BaseNotesList2_1d})
df_top.to_csv("BaseNotes.csv",index=False)
#print(df_base)

categories = ["Herbal", "Green","Mint", "Foodlike", "Vanilla", "Woody","Animalic", "Fruity","Citrus","Floral","Spicy","Camphoraceous"]
"""
print(all_scents_clear_1d[0:100])
print(all_scents_clear_1d[100:200])
print(all_scents_clear_1d[200:300])
print(all_scents_clear_1d[300:400])
print(all_scents_clear_1d[400:500])
print(all_scents_clear_1d[500:557])
"""
Herbal1 = ["Nettle Flower"]

Green1 = ["Bamboo", "Green violet", "Wood notes", "Basil", "Clover Leaf", "Cedarwood", "Garden Roses", "Vetiver", "Black Thyme", "Blackcurrant Leaves", "Green Banana", "Green tea leaves", "Eucalyptus", "Cedar Leaf", "Angelica", "Suede"]

Mint1 = ["Peppermint"]

Foodlike1 = ["Hazelnut", "Licorice"]

Vanilla1 = ["Vanilla infusion", "Bourbon vanilla", "Vanilla"]

Woody1 = ["Orris root", "Flint accord", "Somalian myrrh", "Wood notes", "Cedarwood", "Sambac jasmine", "Amirys wood", "Woody Notes", "Opopanax", "Jacarander Wood", "Sandalwood", "Massoia bark"]

Animalic1 = ["Musk Cetone", "Musk notes"]

Fruity1 = ["Litchi", "Cranberry", "Green Banana", "Wild berries", "Coconut", "Fruity notes"]

Citrus1 = ["Bitter Orange", "Citrus", "Pink grapefruit", "Mandarin Orange", "Italian winter lemon", "Tangerine", "Kumquat", "Mandarin orange"]

Floral1 = ["Ylang-ylang", "Centiflora Rose", "Bulgarian Rose", "Tuscan iris", "Garden Roses", "Cassie", "Mimosa", "Freesia petals", "Lily", "Ginger Lily", "White Orchid", "Jasmine", "Everlasting flower", "Tiare flower"]

Spicy1 = ["Cardamom", "Spicy Notes", "Nutmeg", "Black Thyme", "Pink Pepper", "Cascarilla"]

Camphoraceous1 = ["Camphor wood"]



Herbal2 = ["Basil", "Tarragon", "Basil", "Peppermint", "Davana", "Green Mandarin", "basil"]

Green2 = ["Woody", "Atlas Cedar", "Cypress", "Rosemary", "Calamus", "Driftwood", "Maté", "Florentine iris", "Fir Trees", "Sycamore"]

Mint2 = ["Mint Leaves"]

Foodlike2 = ["Calamus", "Tobacco", "Cactus Flesh", "Saffron", "Almond blossoms"]

Vanilla2 = ["Soft vanilla", "Hint of Vanilla", "Vanilla orchid", "Bourbon Vanilla"]

Woody2 = ["Woody", "Atlas Cedar", "Cypress", "New Caledonia sandalwood", "Iris wood", "Sandalwood", "Sandalwood.", "Amyris wood", "Driftwood", "Rockrose", "Opoponaux"]

Animalic2 = ["White musk", "White musks"]

Fruity2 = ["Red fruits", "Cherry", "Citron Zest", "Pear Flower", "Apricot"]

Citrus2 = ["Amalfi lemon", "Italian Bergamot", "Seville Orange", "Mandarine"]

Floral2 = ["Geranium Leaves", "Magnolia", "May Rose", "Star Jasmine", "Wild Rose", "Damascan rose", "Lentiscus.", "Carnation", "Sambac Jasmine", "Petals", "White peony", "Lily of the Valley (Muguet)", "Clary Sage", "Orange Flower", "Orange Blossom"]

Spicy2 = ["Clove", "Aniseed", "Pink pepper", "Grand Vert Basil", "Indonesian Patchouli", "Hesperidic notes", "Jasmin sambac", "Petitgrain.", "Mimosa Leaf", "Hesperidian Notes", "Red Pepper"]

Camphoraceous2 = []



Herbal3 = ["Candied Fruit", "Shiso", "Quince", "Green Notes", "Green Notes", "Basil Leaves", "Elem", "Fresh Notes", "Iralia", "Basil.", "Powder", "Pimento"]

Green3 = ["Banana accords", "Green tea", "Green notes", "Green Notes", "Hibiscus Seed", "Magnolia leaf", "Green Fig", "Violet Leaf Accord", "Grenadine", "Cool Grapefruit", "Cassis", "Russian Leather", "Oakmoss", "Exotic Spices", "Genista", "Scotch Pine", "Wood", "Mineral Notes", "New Hedione", "Pimento", "Syringa", "Cocoa", "Frangipani", "Mimosa Blossom", "Tonka", "Capiscum"]

Mint3 = ["Iced Mint.", "Spearmint"]

Foodlike3 = ["Ebony.", "French Vanilla", "Cinnamon"]

Vanilla3 = []

Woody3 = ["Tolu Balm", "White cedar", "Oak", "Woods", "Tonka bean and musk", "Virginia Cedar.", "Tonka"]

Animalic3 = ["Laotian Oud Essence", "Oud"]

Fruity3 = ["Redcurrant", "Red berries", "Blood orange", "Blackberry", "Blueberry", "Peach", "Yellow and green lemon"]

Citrus3 = ["Calabrain Bergamot", "Mandarin Leaf", "Sicilian orange", "Sicilian Tangerine", "Bigarade Orange", "Winter Bergamot", "Lemon", "Sicilian lemon"]

Floral3 = ["Peony", "Jasmine Absolute", "Jasmin", "Rose", "Orange", "Cocoa", "Frangipani", "Mimosa Blossom", "Tonka", "Yellow and green lemon", "White Orchid"]

Spicy3 = ["Nutmeg", "Cinnamon", "Cumin", "Rhubarb Leaf."]

Camphoraceous3 = []


Herbal4 = ["Rosemary flower", "Anise", "Coriander", "Tea", "Mint", "Artemisia", "Verbana", "Lavender of Vaucluse", "Chinese Galanga", "Ivy leaves"]

Green4 = ["Lemon tree leaves", "Green accents", "Green freshness", "Wild Reed", "Ivy leaves"]

Mint4 = ["Mint"]

Foodlike4 = ["Apple", "Gingerbread", "Ginger", "Black Pepper", "Hot Pepper", "Civet", "Mace"]

Vanilla4 = ["Mayotte vanilla", "Madagascar vanilla"]

Woody4 = ["Warm woods", "Ambergris", "Amber Notes", "Hinoki", "Gaiac Wood", "Teak", "Gaiac wood", "Cedarwood from China", "Blonde woods", "Oak wood absolute", "Luminous Woody Base"]

Animalic4 = ["Musk", "Leather", "Hyacinth"]

Fruity4 = ["Cherry Blossom", "Water Lily", "Cashmere Wood", "Apricot Rose", "Agarwood", "Black elder", "Pear", "Raspberry", "Pomegranate", "Maxillaria orchid", "Hedione", "Clementine"]

Citrus4 = ["Citron", "Sicilian Lemon", "Sicilian mandarin"]

Floral4 = ["Sweet pea", "Rose", "Tender Rose", "Silk Tree Flower", "Narcissus", "Bulgarian rose", "Heliotrope", "Damascena rose", "Hyacinth", "Turkish rose", "Jasmine Sambac", "Damascus rose", "Almonds", "Madagascar vanilla", "Bay Rose", "White leather accord", "Damask Rose", "Jasmine Sambac", "Vetiver"]

Spicy4 = ["Chinese ginger", "Clove", "Almond", "Pallida", "Amarillys", "Mandrake root."]

Camphoraceous4 = []


Herbal5 = ["Lavender", "Aromatic", "Black pepper", "Pepper", "Verbena"]

Green5 = ["Mango", "Melon", "Water jasmine", "Water flowers", "Green", "Green and Fresh", "Lily of the Valley", "Juniper Berry"]

Mint5 = ["Hesperedic Notes", "Frozen Cedrat", "Bitter Lemon Peel", "Candied orange", "Lime", "Sugar and Vanilla"]

Foodlike5 = ["Syrax", "Cistus", "Myrrh", "Ambrox", "Muguet", "Virginia Cedar", "Lilac", "Rosebud", "Cedarwood", "Patchouli", "Treemoss", "Oak moss", "Almond Blossom"]

Vanilla5 = []

Woody5 = ["Buddleia", "Firbalsam", "Indian Jasmine", "Silver Birch", "Pear tree wood", "Cedarwood"]

Animalic5 = ["Tonkin Musk", "Vetyver", "Mysore", "Somalian Incense", "Frankincense", "Almond Wood"]

Fruity5 = ["Star anise", "Mango", "Melon", "Blackcurrant bud", "Rum", "Mandarin  from Calabria and Essence of Saffron", "Vetiver from Haiti", "Vétiver", "Violets", "Black pepper", "Fig tree wood", "Caviar", "Lime"]

Citrus5 = ["Calabrian bergamot", "Bergamot", "Bitter Lemon Peel", "Lime"]

Floral5 = ["Floral notes", "Night Queen Flower", "Water jasmine", "Tiaré flower", "Orchid", "Rose Bud", "Gardenia", "Lily of the valley-ylang-jasmin", "Japanese wild rose", "Lily of the Valley"]

Spicy5 = ["Jamaican Pepper", "Star Anise crystals", "Clove Oil", "Tonka bean", "Spices", "Sensual Note"]

Camphoraceous5 = []


Herbal6 = ["Curcuma", "Thyme", "Sage", "Juniper", "Laurel"]

Green6 = ["Violet leaf", "Italian Jasmine", "Bitter Almond", "Caraway", "Animalic notes", "Hesperidic Notes", "Grapefruit", "Italian Lemon", "Limette", "Pine", "Blackcurrant", "Boronia", "Anethol", "Black tea", "Woody notes", "Pine needles", "Galbanum.", "Asil", "Lychee", "White Musk Cocktail", "Coriander leaf"]

Mint6 = ["Cardamom.", "White Pepper", "White Pepper", "Black cherry"]

Foodlike6 = ["Honey", "Powdery Notes", "Pineapple", "Ozone aquatic accords", "Apricot Stone", "Labdanum"]

Vanilla6 = []

Woody6 = ["Sandal", "Wild Berries", "Plessis robinson rose", "Pine", "Chinese Cypriol", "Indonesia Patchouli", "Elemi resin", "Rhodes Wood"]

Animalic6 = []

Fruity6 = ["Mayrose", "Violetta-Rose", "Lychee"]

Citrus6 = ["Bigarade", "Citrus notes", "Grapefruit", "Italian Lemon", "Limette", "White Pepper", "Hesperidic Notes"]

Floral6 = ["Lenstiscus", "Italian Jasmine", "Plessis robinson rose", "Mayrose", "Turkish Rose", "Violetta-Rose"]

Spicy6 = ["Cardamom.", "White Pepper", "Coriander leaf"]

Camphoraceous6 = []

Herbal_all = Herbal1+Herbal2+Herbal3+Herbal4+Herbal5+Herbal6
Green_all = Green1+Green2+Green3+Green4+Green5+Green6
Mint_all = Mint1+Mint2+Mint3+Mint4+Mint5+Mint6
Foodlike_all = Foodlike1+Foodlike2+Foodlike3+Foodlike4+Foodlike5+Foodlike6
Vanilla_all = Vanilla1+Vanilla2+Vanilla3+Vanilla4+Vanilla5+Vanilla6
Woody_all = Woody1+Woody2+Woody3+Woody4+Woody5+Woody6
Animalic_all = Animalic1+Animalic2+Animalic3+Animalic4+Animalic5+Animalic6
Fruity_all = Fruity1+Fruity2+Fruity3+Fruity4+Fruity5+Fruity6
Citrus_all = Citrus1+Citrus2+Citrus3+Citrus4+Citrus5+Citrus6
Floral_all = Floral1+Floral2+Floral3+Floral4+Floral5+Floral6
Spicy_all = Spicy1+Spicy2+Spicy3+Spicy4+Spicy5+Spicy6
Camphoraceous_all = Camphoraceous1+Camphoraceous2+Camphoraceous3+Camphoraceous4+Camphoraceous5+Camphoraceous6

All_all = []
All_all.append([Herbal_all,Green_all,Mint_all,Foodlike_all,
               Vanilla_all,Woody_all,Animalic_all,Fruity_all,
               Citrus_all,Floral_all,Spicy_all,Camphoraceous_all])
All_copy = []
for i in All_all[0]:
    new_all = np.concatenate((np.array(i),np.zeros(86-len(i))))
    All_copy.append(list(new_all))
print(All_copy)

# Assuming All_all[0] is a list of data that you want to use as elements
data = All_copy

# Create a dictionary to associate categories with their respective data
data_dict = {category: sublist for category, sublist in zip(categories, data)}

# Create the DataFrame
df = pd.DataFrame(data_dict)

# Specify the file path where you want to save the CSV file
file_path = 'Categorized_Scents.csv'

# Write the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(df)


