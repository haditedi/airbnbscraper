del C:\Hadi\airbnbscraper\custom-rate-tracker\public\graph\*.* /q
del C:\Hadi\airbnbscraper\graph\*.* /q
cd C:\Hadi\airbnbscraper
call venv\scripts\activate
python main.py
@REM xcopy C:\Hadi\airbnbscraper\graph\* C:\Hadi\airbnbscraper\custom-rate-tracker\public\graph /y