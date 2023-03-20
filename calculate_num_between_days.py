from datetime import date 

firstDate = date(2019, 2, 2)
secondDate = date(2018,6,7)

delta = firstDate - secondDate

print(delta.days)