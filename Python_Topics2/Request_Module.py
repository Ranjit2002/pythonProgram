import requests
from bs4 import BeautifulSoup
# response = requests.get("https://www.codewithharry.com")
# print(response.text)

# from json placeholder learn how to do all this

# url = 'https://jsonplaceholder.typicode.com/posts'
#
# data = {
#     "title": 'Ranjit',
#     "body": 'Bhai',
#     "userId": 12,
# }
#
# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
#
# response = requests.post(url, headers=headers, json=data)
# print(response.text)

# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
#
# r = requests.get(url)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())
#
# for heading in soup.find_all("h2"):
#     print(heading.text)

from win10toast import ToastNotifier


def show_notification():
    toaster = ToastNotifier()
    toaster.show_toast("Hello", "This is a notification message.", duration=20)


# Example usage:
show_notification()

