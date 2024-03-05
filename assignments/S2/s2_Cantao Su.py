import inflect 
''' How it works:
1.Digit Verbalization:
I use the inflect library to convert digits into decimal numbers in words. This helps in verbalizing numeric parts of the phone numbers.

2.Special Cases Handling:
Special cases are handled for characters like '+', '-', and digits.
'+' is verbalized as 'PLUS'.
Country codes are verbalized as decimal numbers using the inflect library, and the result is converted to uppercase. The verbalization is followed by a space.
A short pause <PAU> is introduced when four digits occur continuously.
A longer break <BR> is introduced when '-' occurs.

3.Digit Grouping:
Digits are grouped into words, and each word is separated by a space.
The grouping follows certain rules, such as introducing pauses or breaks based on the context of the digits.

4.Prosody Prediction:
The code considers prosody prediction by introducing pauses and breaks to mimic natural speech patterns. 
This is particularly evident in the handling of continuous digits and the presence of '+' and '-' characters.

5.Digit Words Mapping:
The convert_digit_to_word function maps each digit to its verbal representation using a dictionary (digit_words). This function is used to verbalize individual digits.


My Motivation for Digit Grouping:
My idea of digit grouping is motivated by the desire to simulate natural speech patterns. 
My code introduces pauses and breaks to make the verbalization sound more human-like and improve prosody. 
This enhances the intelligibility and naturalness of the verbalized phone numbers.'''

def verbalize_phone_number(phone_numbers):
    verbalized = []

    for phone_number in phone_numbers:
        current_verbalized = ''
        
        # Run through every digits
        for i, digit in enumerate(phone_number):
            # Check if the current digit and the two preceding and following digits are digits
            # <PAU> will be inserted to introduce a short pause when four digits occur continuously
            if i > 1 and i + 1 < len(phone_number) and phone_number[i-2:i+2].isdigit():
                current_verbalized += '<PAU> '

            # Handle special cases for '+', '-', and digits
            # Vervalize '+' as 'PLUS'
            if digit == '+':
                current_verbalized += 'PLUS '
            # Verbalize country_code as decimal numbers 
            elif (digit.isdigit()) and (phone_number[i-1] == '+'):
                country_code = phone_number[i:phone_number.find('-')]
                current_verbalized += (inflect.engine().number_to_words(country_code, andword=False)).upper() + ' '
            # Ingore the following digits of the country code since it would be verbalized from the first digits
            # NB: country code could be two or three digits, so a parallel 'or' was made here
            elif (phone_number[i-2]) == '+' and ((phone_number[i+1]) == '-' or (phone_number[i+2]) == '-'):
                pass
            # Convert all the digits after country code into individual words 
            elif digit.isdigit():
                current_verbalized += convert_digit_to_word(digit) + ' '
            # <BR> will be inserted to introduce a longer break when '-' occurs
            elif digit == '-': 
                current_verbalized += '<BR> '

        verbalized.append(current_verbalized.strip())

    return verbalized

def convert_digit_to_word(digit):
    # Convert a single digit to its verbal representation
    digit_words = {
        '+': 'PLUS',
        '0': 'OH',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE'
    }
    return digit_words.get(digit, '')

# Normalized phone numbers from Labbook 1
phone_numbers = [
    '+31-20-123-4567',
    '+31-6-98-76-54-32',
    '+31-70-987-6543',
    '+31-55-123-4567',
    '+31-36-876-5432',
    '+31-45-234-5678',
    '+31-58-765-4321',
    '+31-10-345-6789',
    '+31-30-876-5432',
    '+31-23-456-7890'
]

# Verbalize and print each example phone number
verbalized_phone_numbers = verbalize_phone_number(phone_numbers)
for verbalized_phone_number in verbalized_phone_numbers:
    print(verbalized_phone_number)
