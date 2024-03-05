'''This code is only for extracting websites and phone numbers in the Netherlands from the input text.
After extration, the website will be checked again to make sure there is no punctuation from the text extracted and normalized.
And also all the phone numbers extracted will be normalized base on three types:
1. In the Netherlands, geographical phone numbers have nine digits and consist of an area code of two or three digits 
and a subscriber number of seven or six digits, respectively. 
An area code consists of two or three digits. 
The larger cities and areas have two digits with a subscriber number of seven digits, permitting more local numbers. 
Smaller areas use three digits with a six-digit subscriber number. 
So the normalized telephone would be either [+31-xx-xxx-xxxx] for larger cities
or [+31-xxx-xx-xx-xx] for smaller cities.
2. In the Netherlands, mobile telephone numbers, however, always have 9 digits totally and always start with '6'
So the normalized mobile phone number will be [+31-6-xx-xx-xx].

Reading reference on:
1. Description of Phone Numbers in the Netherlands, https://www.eur.nl/en/about-eur/house-style/guidelines/style-guide/phone-numbers
2. World Telephone Numbering Guide, http://www.wtng.info/wtng-31-nl.html
3. Telephone Numbers in the Netherlands , https://en.wikipedia.org/wiki/Telephone_numbers_in_the_Netherlands'''

import re
import string

test_content = '''This is an article with Dutch phone numbers and websites embedded in sentences for code testing.

In the bustling city of Amsterdam, you can contact our local office at +31 20 123 4567. For urgent matters, you can reach our mobile support at +31 6 98765432.

If you're exploring The Hague, our office number is +31 70 9876543. Enjoy the scenic beauty of Leeuwarden, and if you need assistance, dial +31 55 1234567. For a taste of history in Maastricht, call us at +31 36 8765432.

Venture into Rotterdam, where our office line is +31 45 2345678. Discover the charm of Groningen and connect with us at +31 58 7654321. For business inquiries in Rotterdam, call +31 10 3456789.

Planning a trip to Utrecht? Reach our local team at +31 30 8765432. If you find yourself in Haarlem, don't hesitate to call +31 23 4567890. We are here to assist you.

Visit our website at https://www.example.com to explore our services. Learn more about regular expressions on Wikipedia: https://en.wikipedia.org/wiki/Regular_expression#Syntax. For Python regex queries, search on Google: https://www.google.com/search?q=python%20re.

For information about the University of Groningen, check their official contact page: https://www.rug.nl/info/contact. Collaborate with us on GitHub: https://www.github.com. Get coding help on Stack Overflow: https://stackoverflow.com/questions/tagged/python.

Stay updated on Dutch news with DutchNews: https://www.dutchnews.nl. Read the latest headlines on NU.nl: https://www.nu.nl. Check the weather forecast on The Weather Channel: https://www.weather.com. Connect professionally on LinkedIn: https://www.linkedin.com.
'''

def extract_features(text):
    '''This function is to simply extract phone numbers and website links but without doing any normalization'''
    
    # Regular expression for extracting phone numbers in international format
    phone_number_pattern = r'\+(?:\d[- ]?){1,14}\d'

    # Regular expression for extracting website links
    website_link_pattern = r'https?://\S+'

    # Find all matches for phone numbers
    extracted_numbers = re.findall(phone_number_pattern, text)

    # Find all matches for web links
    website_links = re.findall(website_link_pattern, text)

    return extracted_numbers, website_links

def normalize_website_links(website_links):
    '''Sometimes the punctuations from the text would be extraced.
    this function is to check and normalize the extracted websites
    if there is any possible punctuation at the end of the link'''
    normalized_website_links = []
    for website in website_links:
        if website[-1] in string.punctuation and website[-1] != '/': 
            website = website[:-1]
            normalized_website_links.append(website)
        else:
            normalized_website_links.append(website)
    return normalized_website_links

    
def normalize_phone_numbers(extracted_numbers):
    '''This function is to normalize phone numbers in the Netherlands based on three different types: 
    1. mobile phone numbers
    2. geographical phone numbers from larger cities
    3. geographical phone numbers from smaller cities.'''

    normalized_phone_numbers = []
    for number in extracted_numbers:
        # To initialize phone numbers by removing non-digit characters but still with '+'
        initialized_number = '+' + re.sub(r'\D', '', number) 

        # To normalize phone numbers into mobile format, which always starts with '6' after the country code '31'
        if initialized_number[3] == '6':
            insert_positions = [2, 3, 5, 7, 9]
            normalized_number = ''.join([initialized_number[i] + '-' if i in insert_positions 
                                         else initialized_number[i] for i in range(len(initialized_number))])
            normalized_phone_numbers.append(normalized_number)
        # To normalize phone numbers into geographical format from larger cities, when the area codes corresponds with the followings
        elif initialized_number[3:5] in ['10', '13', '15', '20', '23', '24', '26', '30', '33', '35', 
                                         '36', '38', '40', '43', '45', '46', '50', '53', '55', '58', 
                                         '70', '71', '72', '73', '74', '75', '76', '77', '78', '79']:
            insert_positions = [2, 4, 7]
            normalized_number = ''.join([initialized_number[i] + '-' if i in insert_positions 
                                         else initialized_number[i] for i in range(len(initialized_number))])
            normalized_phone_numbers.append(normalized_number)
        # To normalize phone numbers into geographical format from smaller cities
        else:
            insert_positions = [2, 5, 7, 9]
            normalized_number = ''.join([initialized_number[i] + '-' if i in insert_positions 
                                         else initialized_number[i] for i in range(len(initialized_number))])
            normalized_phone_numbers.append(normalized_number)
    return normalized_phone_numbers


# Extract phone numbers and websites from the text
extracted_phone_numbers, extracted_website_links = extract_features(test_content)

# Normalize extracted phone numbers and websites
normalized_phone_numbers = normalize_phone_numbers(extracted_phone_numbers)
normalized_website_links = normalize_website_links(extracted_website_links)

# Print the results
print("Normalized Phone Numbers:", normalized_phone_numbers)
print("Normalized Website Links:", normalized_website_links)
