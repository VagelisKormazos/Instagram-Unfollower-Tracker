# Instagram Unfollower Tracker

This application helps you track your Instagram followers, identify unfollowers, and open their profiles in a web browser.

![Instagram Logo](path/to/instagram_logo.png)

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

The Instagram Unfollower Tracker is a Python script that reads HTML files containing follower and following information from Instagram. It then compares the lists of followers and following to determine the users who have unfollowed you. Finally, it opens the profiles of the unfollowers in a web browser.

## Installation

To use this application, follow the steps below:

1. Clone the repository: `git clone https://github.com/your-username/instagram-unfollower-tracker.git`
2. Navigate to the project directory: `cd instagram-unfollower-tracker`
3. Install the required dependencies: `pip install -r requirements.txt`

Note: This application uses the `bs4` library, so make sure it is installed.

## Usage

To use the Instagram Unfollower Tracker, follow these steps:

1. Export your followers and following lists from Instagram as HTML files. Save the followers file as `followers.html` and the following file as `following.html`. Place these files in the project directory.
2. Open the Python script `instagram_unfollower_tracker.py` in a text editor.
3. Modify the `directory` variable to specify the path to the project directory where the HTML files are located. For example:
   ```python
   directory = r'C:\Users\YourUsername\instagram-unfollower-tracker'
