@echo off
cd city-recipe-recommender
call venv\Scripts\activate
set FLASK_APP=app.py
flask run
