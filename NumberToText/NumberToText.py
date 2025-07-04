def number_to_words(num, system='international'):
    """Convert a number into words (supports Indian & International systems)."""
    if num == 0:
        return "Zero"

    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
             "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", 
            "Seventy", "Eighty", "Ninety"]

    def convert_less_than_hundred(n):
        if n < 10:
            return units[n]
        elif 10 <= n < 20:
            return teens[n - 10]
        else:
            ten, unit = divmod(n, 10)
            return tens[ten] + (" " + units[unit] if unit != 0 else "")

    def convert_less_than_thousand(n):
        hundred, remainder = divmod(n, 100)
        res = []
        if hundred > 0:
            res.append(units[hundred] + " Hundred")
        if remainder > 0:
            res.append(convert_less_than_hundred(remainder))
        return " ".join(res)

    if system == 'indian':
        # Indian numbering system (Lakhs, Crores)
        crore = num // 10000000
        num %= 10000000
        lakh = num // 100000
        num %= 100000
        thousand = num // 1000
        num %= 1000

        parts = []
        if crore > 0:
            parts.append(convert_less_than_thousand(crore) + " Crore")
        if lakh > 0:
            parts.append(convert_less_than_thousand(lakh) + " Lakh")
        if thousand > 0:
            parts.append(convert_less_than_thousand(thousand) + " Thousand")
        if num > 0:
            parts.append(convert_less_than_thousand(num))
        
        return " ".join(parts)

    else:
        # International numbering system (Thousands, Millions, Billions)
        parts = []
        if num >= 1000000000:
            billion, num = divmod(num, 1000000000)
            parts.append(convert_less_than_thousand(billion) + " Billion")
        if num >= 1000000:
            million, num = divmod(num, 1000000)
            parts.append(convert_less_than_thousand(million) + " Million")
        if num >= 1000:
            thousand, num = divmod(num, 1000)
            parts.append(convert_less_than_thousand(thousand) + " Thousand")
        if num > 0:
            parts.append(convert_less_than_thousand(num))
        
        return " ".join(parts)

def main():
    print("Number to Words Converter")
    print("Choose numbering system:")
    print("1. International (Million, Billion)")
    print("2. Indian (Lakh, Crore)")
    choice = input("Enter choice (1 or 2): ").strip()
    system = 'international' if choice == '1' else 'indian'

    with open("numbers.txt", "a") as file:
        while True:
            user_input = input("Enter a number (or press Enter to quit): ").strip()
            if not user_input:
                break
            try:
                num = int(user_input)
                if num < 0:
                    print("Please enter a positive number.")
                    continue
                words = number_to_words(num, system)
                output = f"{num} - {words}"
                print(output)
                file.write(output + "\n")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()