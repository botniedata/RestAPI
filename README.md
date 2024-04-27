### Steps
- Create Python Environment <br>
`python -m venv env`

- Create requirements.txt for libraries and packages requirements <br>
`code requirements.txt`

- Enable Environment (PowerShell) <br>
`.\env\Scripts\Activate.ps1`

- Load and Install Libraries and Packages <br>
`pip install -r requirements.txt`
- Add
`fastapi` `uvicorn`

- Deactivate the enviroment <br>
`deactivate`

- Create Python File <br>
`code app.py`

- Initialize local directory <br>
`git init .`

- Create gitignore file include `\env` folder <br>
`code .gitignore`

- Connect local git to GitHub Repository <br>
~

- Load the page
`uvicorn <name of the file>:app --reload`

---

### Data Engineer - Coding Assignment
As part of your evaluation, we will need you to complete a coding assignment that will help us understand your fit with the opening at OnebyZero. 

### Description of assignment
Assignment Environment:
1. This application populates and provides retrieval features for transactions of a company.
2. Transaction information is coming as files (let’s say every 5 minutes) in a folder.
3. Another folder contains a file, which contains reference data for products, against which the transactions are happening.
4. This application is an in-memory application so no persistent storage is required. i.e. You can reload the already available data in the transaction folder upon start-up of the application.
5. A transaction record contains following attributes in a comma separated format
    * transactionId
    * productId
    * transactionAmount
    * transactionDatetime
6. The product reference data have following attributes in a CSV.
    * productId
    * productName
    * productManufacturingCity
7. Reference data is static and transaction data keeps coming in real-time in their respective folders.

### Application functionalities
1. Processes the data in streaming fashion, meaning provides up to date view for below mentioned REST calls.
2. Following REST APIs should be implemented.
    * GET request <br> 
    `http://localhost:8080/assignment/transaction/{transaction_id}`
    - Type: GET
    - JSON Format
    ```
    { “transactionId”: 1,
      “productName”: “P1”, 
      “transactionAmount”: 1000.0, 
      “transactionDatetime”: 
      “2018-01-01 10:10:10”
    }
    ```
    * GET request <br>
    `http://localhost:8080/assignment/transactionSummaryByProducts/{last_n_days}`
    - Type: GET
    - JSON Format
    ```
    { “summary”: [ 
        {“productName”: “P1”, 
        {“totalAmount”: 3000.0}
        ]
    }
    ```
    * GET request <br>
    `http://localhost:8080/assignment/transactionSummaryByManufacturingCity/{last_n_days}`
    - Type: GET
    - JSON Format
    ```
    { “summary”:  [ 
        {“cityName”: “C1”, 
        {“totalAmount”: 3000.0}
        ]
    }
    ```
Note: 
- Rest call (a) will receive transactionId from input and provide details of transaction.
- Rest call (b), (c) will receive lastNDays in the input data, application will provide summary of transactions during the last 10 days from current date by product name or manufacturing city based on type of call.

Sample data format:
- File name: `Transaction_20180101101010.csv`
```
transactionId, productId, transactionAmount,transactionDatetime
1,             10,        1000.0,           2018-10-01 10:10:10
2,             10,        1000.0,           2018-10-01 10:15:10
3,             20,        2000.0,           2018-10-01 10:15:20
4,             10,        1000.0,           2018-10-01 10:10:10
5,             30,        3000.0,           2018-10-01 10:20:10
6,             20,        2000.0,           2018-10-01 10:15:30
```
- File name: `ProductReference.csv`
```
productId, productName, productManufacturing
10,        P1,          C1
20,        P2,          C1
30,        P3,          C2
```

What you’ll be judged on:
1. Completeness
2. Code quality
3. Design
    - How do you consider the implementation if 5-10s of concurrent requests come at once.?
    - Each API request should not be a repeatable task.
    - How does an API request module should not be blocked by the data processing module, when there are 100s or 1000s of transaction files?
    - Scalability should be in the design.