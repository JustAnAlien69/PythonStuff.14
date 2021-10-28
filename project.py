import pandas as pd
import csv

df = pd.read_csv("project.csv")

del df ["index"]

df = df.rename({
    "Star_name":"starName",
    "Mass":"mass",
    "Radius":"radius"
},axis="columns")

df.to_csv("projectFinal.csv")