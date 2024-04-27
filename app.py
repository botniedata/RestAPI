from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

# ProductReference.csv
products = {
    10: {"productName": "P1", "productManufacturing": "C1"},
    20: {"productName": "P2", "productManufacturing": "C1"},
    30: {"productName": "P3", "productManufacturing": "C2"},

}

# Transaction_20180101101010.csv
transactions = {
    1: {"productId": 10, "transactionAmount": 1000.0, "transactionDatetime": "2018-10-01 10:10:10"},
    2: {"productId": 10, "transactionAmount": 1000.0, "transactionDatetime": "2018-10-01 10:15:10"},
    3: {"productId": 20, "transactionAmount": 2000.0, "transactionDatetime": "2018-10-01 10:15:20"},
    4: {"productId": 10, "transactionAmount": 1000.0, "transactionDatetime": "2018-10-01 10:10:10"},
    5: {"productId": 30, "transactionAmount": 3000.0, "transactionDatetime": "2018-10-01 10:20:10"},
    6: {"productId": 20, "transactionAmount": 2000.0, "transactionDatetime": "2018-10-01 10:15:30"},
}


@app.get("/assignment/transaction/{transaction_id}")
async def get_transaction_by_id(transaction_id: int = Path(...)):
    
    transaction = transactions.get(transaction_id)
    if not transaction:
        return {"message": f"Transaction with ID {transaction_id} not found"}

    product_id = transaction.get("productId")
    if not product_id:
        return {"message": f"Product information for transaction ID {transaction_id} not found"}

    product_name = products.get(product_id, {}).get("productName")

    result = {
        "transactionId": transaction_id,
        "productName": product_name,
        "transactionAmount": transaction["transactionAmount"],
        "transactionDatetime": transaction["transactionDatetime"],
    }
    return result


@app.get('assignment/transactionSummaryByProducts/{last_n_days}')
async def get_last_n_days_by_products(last_n_days: str):
    # Return Values should be the following
    # productName, totalAmount
    return {"lastNdays": lastNdays}

@app.get('assignment/transactionSummaryByManufacturingCity/{last_n_days}')
aysnc def get_last_n_days_by_manufacturing_city(last_n_days: str):
    # Return Values should be the following
    # cityName, totalAmount
    return {"lastNdays": lastNdays}