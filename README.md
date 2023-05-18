# InstaUnfollower

This Python script helps you analyze your Instagram followers and following lists to identify unfollowers. It also provides the ability to open the profiles of the unfollowers in a web browser for further inspection.

## How it Works

1. The script reads two HTML files, `followers.html` and `following.html`, which contain the follower and following information, respectively.
2. It uses the BeautifulSoup library to parse the HTML content and extract relevant data.
3. The usernames of your followers and following are extracted from the HTML files and stored in separate lists.
4. The lists are converted to sets to filter out duplicates.
5. The script compares the sets of followers and following to identify unfollowers (users who follow you but you don't follow back) and users whom you don't follow.
6. The results are printed to the console, including the number of followers, following, unfollowers, and users you don't follow.
7. The script opens a web browser and displays the profile of the first unfollower.

## Setup

1. Clone this repository to your local machine or download the script file.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running the following command in your terminal:pip install beautifulsoup4


## Usage

1. Export your Instagram follower and following lists as HTML files. You can do this by using a tool or service that provides this functionality.
2. Place the `followers.html` and `following.html` files in the same directory as the script.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the following command: python insta_unfollower.py

5. The script will process the HTML files, compare the lists, and print the results to the console.
6. It will also open a web browser with the profile of the first unfollower for further inspection.

**Notes:**
- Make sure the HTML files are named `followers.html` and `following.html` and are located in the same directory as the script. If your files have different names or are located elsewhere, update the file paths in the script accordingly.
- The script assumes that the HTML files have a specific structure. If the structure of the HTML files changes, you may need to modify the script to match the new structure.
- Be cautious when running scripts that access and parse HTML files. Make sure the files come from trusted sources to avoid potential security risks.

**Disclaimer:**
This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any misuse or damages caused by the script.

Feel free to customize and modify the script to fit your specific needs.
