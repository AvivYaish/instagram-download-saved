import sys
import pathlib
import instaloader

if "__main__" == __name__:
    if not len(sys.argv) == 3:
        sys.exit("Invalid usage, please use: python script.py <username-to-login-with> <username-to-download>")

    username_login: str         = sys.argv[1]
    username_to_download: str   = sys.argv[2]

    L = instaloader.Instaloader()
    L.interactive_login(username_login)     # This will ask for your password
    profile = str(instaloader.Profile.from_username(L.context, username_to_download).userid)
    download_path = pathlib.Path('.')

    for post in instaloader.Profile.from_username(L.context, username_login).get_saved_posts():
        if post.owner_id == profile:
            L.download_pic(str(download_path.joinpath(pathlib.Path(str(int(post.date.timestamp()))))), url=post.url, mtime=post.date)