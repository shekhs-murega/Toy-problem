def convert_to_24hour(hour, minute, period):
    #If the period is "am"
    if period.lower() == "am":
        #If the hour is 12 (midnight) reset to 0
        if hour == 12:
            hour = 0
    else:
        #If period is "pm" and the hour is not 12, convert to 24hour format
        if hour != 12:
            hour += 12
    #Return the time in 24 hour fourmat as a four digit string
    return f"{hour:02d}{minute:02d}"    

 
