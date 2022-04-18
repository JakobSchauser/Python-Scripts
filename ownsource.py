import requests


url = "https://libraryofbabel.info/search.cgi"
r = requests.get(url)
print(r.text)


# print(r.Find("a", class_ = "intext"))

# with open(__file__) as f: 
#     print('\n'.join(f.read().split('\n')))