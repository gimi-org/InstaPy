import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_os_env():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        return 'linux'
    elif platform == "darwin":
        return 'osx'
    elif platform == "win32":
        return 'windows'


class Settings:
    log_location = os.path.join(BASE_DIR, 'logs')
    database_location = os.path.join(BASE_DIR, 'db', 'instapy.db')
    os_env = get_os_env()

    # TODO: Make it dynamic
    chromedriver_location = os.path.join('/usr/local/share/chromedriver')

    chromedriver_min_version = 2.36
    # Set a logger cache outside the InstaPy object to avoid re-instantiation issues
    loggers = {}
    logger = None
    # Set current profile credentials for DB operations
    profile = {"id": None, "name": None}
