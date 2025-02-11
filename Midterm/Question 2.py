def convert_date(date_str):
    """Convert date from mm/dd/yyyy to a more human-readable format."""


    month, day, year = date_str.split('/')
    


    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    


    month_index = int(month) - 1  
    month_name = month_names[month_index]
    




    formatted_date = f"{month_name} {int(day)}, {year}"
    return formatted_date


#-----------------------MAIN-----------------------#

if __name__ == "__main__":

    date_input = input("Enter the date (mm/dd/yyyy): ")
    

    try:
        date_output = convert_date(date_input)
        print(f"Date Output: {date_output}")
    except (ValueError, IndexError):
        print("Invalid date format. Please enter the date in mm/dd/yyyy format.")