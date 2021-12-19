import pathlib
import instaloader

username_login: str         = "<enter-your-login-username-here>"
username_to_download: str   = "<enter-the-username-to-download-here>"

L = instaloader.Instaloader()
L.interactive_login(username_login)     # This will ask for your password
profile = str(instaloader.Profile.from_username(L.context, username_to_download).userid)
download_path = pathlib.Path('.')

for post in instaloader.Profile.from_username(L.context, username_login).get_saved_posts():
    if post.owner_id == profile:
        L.download_pic(str(download_path.joinpath(pathlib.Path(str(int(post.date.timestamp()))))), url=post.url, mtime=post.date)