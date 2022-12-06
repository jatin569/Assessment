import re

def validate_phone_number(phone):
  #validating a US number
  pattern = re.compile("^\+?1?[-\s]?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$")
  result = re.search(pattern, phone)
  if result:
    return True
  else:
    return False

#Test Cases
print(validate_phone_number("2124567890"))
print(validate_phone_number("212-456-7890"))
print(validate_phone_number("(212)456-7890"))
print(validate_phone_number("(212)-456-7890"))
print(validate_phone_number("212.456.7890"))
print(validate_phone_number("212 456 7890"))
print(validate_phone_number("+12124567890"))
print(validate_phone_number("+1 212.456.7890"))
print(validate_phone_number("+212-456-7890"))
print(validate_phone_number("1-212-456-7890"))