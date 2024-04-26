import pandas as pd
import os

# Create a list of data
products = [
    [10, 1000.0, "2018-10-01 10:10:10"],
    [10, 1000.0, "2018-10-01 10:15:10"],
    [20, 2000.0, "2018-10-01 10:15:20"],
    [10, 1000.0, "2018-10-01 10:10:10"],
    [30, 3000.0, "2018-10-01 10:20:10"],
    [620, 2000.0, "2018-10-01 10:15:30"],
]

# Define the column names
HeaderNames = ["productId", "transactionAmount", "transactionDatetime"]

# Create a pandas DataFrame from the data
df = pd.DataFrame(products, columns=HeaderNames)

# Create the data folder if it doesn't exist
folderDir = "products"
if not os.path.exists(folderDir):
    os.makedirs(folderDir)

# Save the DataFrame to a CSV file inside the data folder
df.to_csv(os.path.join(folderDir, "products.csv"), index=False)

print("CSV file created successfully in the data directory!")
