# instagram-download-saved
A python script that downloads photos you saved from a specific profile.

The only dependency is [instaloader](https://instaloader.github.io/), an open-source python package for scraping instagram.

Usage:

    python script.py <username-to-login-with> <username-to-download>
    
Afterwards, you will be prompted by instaloader to enter your password.

According to instaloader's [code](https://github.com/instaloader/instaloader), the password is not saved anywhere.
