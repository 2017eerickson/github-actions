# create dict to hold roman nums high to low
# create var to hold converted num
# iterate through obj to find first smaller than num  number
# subtract from num
# restart loop until num is 0
# return converted num



def to_roman(num):
    romanNums = {
        "M" : 1000,
        "CM" : 900,
        "D" : 500,
        "CD" : 400,
        "C" : 100,
        "L" : 50,
        "XL" : 40,
        "X" : 10,
        "IX" : 9,
        "V" : 5,
        "IV" : 4,
        "I" : 1,
   }
    roman = ""
    while(num > 0):
        for letter in romanNums:
            if romanNums[letter] <= num:
                roman = roman + letter
                num = num - romanNums[letter] 
                break           
    return roman

print(to_roman(700))