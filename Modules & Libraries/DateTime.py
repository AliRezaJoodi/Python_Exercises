# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:      https://www.w3schools.com/python/python_datetime.asp

from display import *

def datetime_today():
    from datetime import datetime
    x = datetime.now()
    dispaly("DateTime Today:", x)
    x = datetime.now().date()
    dispaly("Date Today:", x)
    x = datetime.now().time()
    dispaly("Time Today:", x)

def datetime_create():
    from datetime import datetime
    x1 = datetime(2020, 5, 17, 12, 50, 00)
    dispaly("DateTime Created:", x1)
    x2 = datetime.now()
    dispaly("DateTime Today:", x2)
    dispaly("Distance:", (x2-x1).days)

def datetime_formatting():
    from datetime import datetime
    dispaly("Function:", "datetime_formatting")
    x = datetime.now()
    dispaly("DateTime Today:", x)
    dispaly("Year Number:", x.strftime("%Y"))
    dispaly("Month Number (01~12):", x.strftime("%m"))
    dispaly("Day Number (01~31):", x.strftime("%d")) 

def date_tody(): 
    from datetime import date  
    x1 = date.today()
    dispaly("Year Number:", x1)

def date_create():
    from datetime import date
    x1 = date(1984, 12, 30)
    dispaly("Date Created:", x1)
    x2 = date.today()
    dispaly("Date Today:", x2)
    dispaly("Distance:", (x2-x1).days)

def date_formatting():
    from datetime import date   
    x1 = date.today()
    dispaly("Year Number:", x1)
    dispaly("Year Number:", x1.year)
    dispaly("Month Number (01~12):", x1.month)
    dispaly("Day Number (01~31):", x1.day)
        

def main():          
    datetime_formatting()
    
if __name__ == "__main__":
    main()