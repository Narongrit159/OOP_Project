@echo off
call myenv\Scripts\activate
uvicorn main:app --reload
