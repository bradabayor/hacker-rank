s = "12:40:03AM"

def timeConversion():
    hour = int(s[0] + s[1])
    
    if s[8] == "P":
        if hour != 12:
            hour += 12

    if s[8] == "A":
        if hour == 12:
            hour = 0

    if hour < 10:
        hour = "0" + str(hour)

    return f"{hour}:{s[3] + s[4]}:{s[6] + s[7]}"

print(timeConversion())