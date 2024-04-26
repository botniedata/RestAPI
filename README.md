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
