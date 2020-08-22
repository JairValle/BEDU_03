import requests

# Direcciones para consultar información segun criterios https://api.github.com/users/JairValle

# CONSTANTS
URL_BASE='https://api.github.com/'

def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def download_user_avatar(image_url):
    response = requests.get(image_url)
    if response.status.code == 200:
        print(response.content)
    return None

# username = input('Give the username:\t')
# user = get_github_user(username)


# print(user.get('avatar_url'))

download_user_avatar('https://avatars2.githubusercontent.com/u/67514107?v=4')
