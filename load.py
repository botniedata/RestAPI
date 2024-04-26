import pandas as pd
import os

# Create a list of data
products = [
    ["1", "10", "1000.0", "2018-10-01 10:10:10"],
    ["2", "10", "1000.0", "2018-10-01 10:15:10"],
    ["3", "20", "2000.0", "2018-10-01 10:15:20"],
    ["4", "10", "1000.0", "2018-10-01 10:10:10"],
    ["5", "30", "3000.0", "2018-10-01 10:20:10"],
    ["6", "20", "2000.0", "2018-10-01 10:15:30"],
]

# Define the column names
HeaderNames = ["transactionId", "productId", "transactionAmount", "transactionDatetime"]

# Create a pandas DataFrame from the data
df = pd.DataFrame(products, columns=HeaderNames)

# Create the data folder if it doesn't exist
data_folder_path = "data"
if not os.path.exists(data_folder_path):
    os.makedirs(data_folder_path)

# Save the DataFrame to a CSV file inside the data folder
df.to_csv(os.path.join(data_folder_path, "products.csv"), index=False)

print("CSV file created successfully in the data directory!")
