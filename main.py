import os
from bs4 import BeautifulSoup
import time
import webbrowser

directory = r'C:\Users\Vagelis\Desktop\Unfollowers'

# List all files in the directory
files = os.listdir(directory)
print(files)

# Open the HTML file with UTF-8 encoding
with open(r'C:\Users\Vagelis\Desktop\Unfollowers\followers.html', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    html_followers = file.read()

# Print the HTML content
#print(html_content)

# Parse the HTML content
soup = BeautifulSoup(html_followers, 'html.parser')

# Find all <div> tags
div_tags = soup.find_all('div')


# Extract the usernames from <a> tags within <div> tags
followers = []
for div_tag in div_tags:
    a_tags = div_tag.find_all('a')
    for a_tag in a_tags:
        followers.append(a_tag.text)

# Convert the list to a set to filter out duplicates
followers=list(set(followers))


# Open the HTML file with UTF-8 encoding
with open(r'C:\Users\Vagelis\Desktop\Unfollowers\following.html', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    html_following = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_following, 'html.parser')

# Find all <div> tags
div_tags = soup.find_all('div')

# Extract the usernames from <a> tags within <div> tags
following = []
for div_tag in div_tags:
    a_tags = div_tag.find_all('a')
    for a_tag in a_tags:
        following.append(a_tag.text)

following=list(set(following))

# Convert the lists to sets
set1 = set(followers)
set2 = set(following)

# Find the unique elements in each set
unfollowers = list(set2 - set1)
you_dont_follow = list(set1 - set2)


print("The unfollowers:", unfollowers)
#time.sleep(1)
print("You dont follow :", you_dont_follow)

print("\nUsers that follow you:")
print(len(followers))
print("\nUsers that they following:")
print(len(following))
print("\nThe unfollowers are:")
print(len(unfollowers))
print("\nYou dont follow :")
print(len(you_dont_follow))
print("\nFive(5) users who don't follow you:\n")

link = "https://www.instagram.com/"
for i in range(5):
    value = unfollowers[i]
    cleaned_value = value.replace("'", "")
    print(cleaned_value)

link=link+cleaned_value
print(link)
webbrowser.open(link)
