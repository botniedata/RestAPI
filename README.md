### Steps
- Create Python Environment <br>
`python -m venv env`

- Create requirements.txt for libraries and packages requirements <br>
`code requirements.txt`

- Enable Environment (PowerShell) <br>
`.\env\Scripts\Activate.ps1`

- Load and Install Libraries and Packages <br>
`pip install -r requirements.txt`

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

- Set app for running web <br>
`set FLASK_APP=app.py` <br>
`set FLASK_ENV=dev`

- Run the app.py <br>
`flask run`