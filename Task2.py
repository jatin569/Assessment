import requests
from bs4 import BeautifulSoup

# Taking the URL from the user
url = input('Enter a website URL: ')

# Making the request
r = requests.get(url)

# Parsing the response
soup = BeautifulSoup(r.content, 'lxml')

# Printing the Social Links
print("\nSocial Links:")
social_links = soup.find_all('a', href=True)
for link in social_links:
    if 'facebook' in link['href'] or 'twitter' in link['href'] or 'youtube' in link['href'] or 'linkedin' in link['href']:
        print(link['href'])

# Printing the Email
print("\nEmail:")
email_address = soup.find('a', attrs={'href': lambda x: x and 'mailto' in x})
if email_address is not None:
    print(email_address.get('href')[7:])

# Printing the Contact
print("\nContact:")
contact_details = soup.find('a', attrs={'href': lambda x: x and 'tel' in x})
if contact_details is not None:
    print(contact_details.get('href')[4:])