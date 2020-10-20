def number_in_english(n):
    n1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
          6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
    n2 = {11: "eleven", 12: "twelve", 13: "thirteen",
          14: "fourteen", 15: "fifteen", 16: "sixteen",
          17: "seventeen", 18: "eighteen", 19: "nineteen"}
    n3 = {20: "twenty", 30: "thirty", 40: "forty",
          50: "fifty", 60: "sixty", 70: "seventy",
          80: "eighty", 90: "ninety"}
    if n == 0:
        return "zero"
    elif n <= 10:
        return n1.get(n)
    elif 10 < n <= 19:
        return n2.get(n)
    elif 20 <= n <= 99:
        if n % 10 == 0:
            return n3.get(n)
        else:
            return str(n3.get(n - n % 10)) + ' ' + str(n1.get(n % 10))
    elif 100 <= n <= 999:
        if n % 100 == 0:
            return str(n1.get(n // 100)) + " hundred"
        elif 1 <= n % 100 <= 9:
            return str(n1.get(n // 100)) + " hundred and " + str(n1.get(n % 10))
        elif 11 <= n % 100 <= 19:
            return str(n1.get(n // 100)) + " hundred and " + str(n2.get(n % 100))
        elif n % 100 >= 20 and (n % 100) % 10 == 0:
            return str(n1.get(n // 100)) + " hundred and " + str(n3.get(n % 100 - n % 10))
        else:
            return str(n1.get(n // 100)) + " hundred and " + str(
                n3.get(n % 100 - n % 10)) + ' ' + str(n1.get(n % 10))
