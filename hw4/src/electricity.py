
import pandas as pd

def calculate_electricity_bill (kwh, household_type):
    #if kwh < 0 or kwh > 10000 or household_type != 'residential' or household_type != 'business': 
    if kwh < 0 or kwh > 10000 or (household_type != 'residential' and household_type != 'business'):
        return 'Đầu vào không hợp lệ'
    
    if household_type == "residential":
        rates = [1678, 1734, 2014, 2536]
    else:  # "business"
        rates = [2500, 2800, 3000, 3500]

    result = 0
    if kwh <= 50:
        result = kwh * rates[0]
    elif kwh <= 100:
        result = (kwh - 50) * rates[1] + 50 * rates[0]
    elif kwh <= 200:
        result = (kwh - 100) * rates[2] + 50 * rates[1] + 50 * rates[0]
    else:
        result = (kwh - 200) * rates[3] + 100 * rates[2] + 50 * rates[1] + 50 * rates[0]
    
    return round(result)


