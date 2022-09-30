#!/usr/bin/env python3
import cgi
import os

from templates import login_page, secret_page

import secret




# from http.cookies import SimpleCookie

# This code was taken from the lab.

def parse_cookies(cookie_string):
    if not cookie_string:
        return cookie_string
    cookies = cookie_string.split(";")
    result = {}
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]

    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")

header = ""
header += "Content-Type: text/html\r\n"

body = ""

auth = (username == secret.username and password == secret.password)

""" 
if we want to prevent people from accessing the secret page using 'logged;true' cookie,
we would change the logic from or to and on row 45 column 9
"""
if auth or ('logged' in cookies and cookies['logged'] == "true"):
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += login_page()

print(header)
print()
print(body)