SET PROJECT_ROOT=%~dp0..

py -m venv %PROJECT_ROOT%\venv && %PROJECT_ROOT%\venv\Scripts\activate && pip install -r %PROJECT_ROOT%\requirements.txt && deactivate