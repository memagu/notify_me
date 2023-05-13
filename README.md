# notify_me

A simple interactive CLI application for managing automatic notifications on Windows.

## Installation guide

1. Clone this repo.

2. Navigate to the directory to which this repo has been cloned.

3. Create a venv, activate it and install the requirements found in `requiremets.txt`. This can be performed by using
   the following command:

       $ py -m venv venv && .\venv\Scripts\activate && pip install -r requirements.txt

## Usage

1. Navigate to the directory to which this repo has been cloned.

2. Use the following command to activate the venv:

       $ .\venv\Scripts\activate

3. Run **notify_me** using the following command:

       $ .\src\notify_me.py

4. When done deactivate the venv using the following command:

       $ deactivate

These actions can be chained and used in one command:

    $ .\venv\Scripts\activate && py .\src\notify_me.py && deactivate

## Contribution

Feel free to contribute to this project!