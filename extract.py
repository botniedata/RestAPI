import pandas as pd
import os

products = [
    [10, "P1", "C1"],
    [10, "P1", "C1"],
    [20, "P2", "C2"],
    [10, "P1", "C1"],
    [30, "P3", "C3"],
    [20, "P2", "C2"]
]

# Define the column names
HeaderNames = ["productId", "productName", "productManufacturingCity"]

df = pd.DataFrame(products, columns=HeaderNames)

# Create the data folder if it doesn't exist
folderDir = "products"
if not os.path.exists(folderDir):
    os.makedirs(folderDir)

# Save the DataFrame to a CSV file inside the data folder
df.to_csv(os.path.join(folderDir, "ProductReference.csv"), index=False)

print("CSV file created successfully in the data directory!")
