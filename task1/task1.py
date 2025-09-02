import re
import datetime

def convert_date(match):
        date = match.group(0)
        year,month,day = date.split("-")

        day = str(int(day))

        if day.endswith("1") and day!="11":
            day = day + "st"
        elif day.endswith("2") and day!="12":
            day = day + "nd"
        elif day.endswith("3") and day!="13":
            day = day + "rd"
        else:
            day = day + "th"

        months = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"Spetember","10":"October","11":"November","12":"December"}
        month_name = months[month]

        return f"{day} {month_name} {year}"


def transform_text(input_text):
    input_text = re.sub(r'\d\d\d-\d\d\d-\d\d\d','[REDACTED]',input_text)


    input_text = input_text.replace("Python","🐍 ")
    input_text = input_text.replace("python","🐍 ")

    input_text = input_text.replace("teh","the")
    input_text = input_text.replace("youre","you're")
    input_text = input_text.replace("taht","that")
    input_text = input_text.replace("adn","and")
    input_text = input_text.replace("dont","don't")

    input_text = re.sub(r'\d\d\d\d-\d\d-\d\d',convert_date,input_text)

    return input_text


input_text = input("Enter your text: ")
print(transform_text(input_text))
