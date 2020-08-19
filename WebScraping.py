import requests
result = requests.get("http://www.example.com")

import bs4

# GRABBING A TITLE
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
print("\n"* 4)
print(soup.select('title'))
print(soup.select('title')[0])
print(soup.select('title')[0].getText())
print("\n" * 10)

# GRABBING A CLASS
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, "lxml")
first_item = soup.select('.toctext')[0]
print(first_item.text)

for item in soup.select('.toctext'):
    print(item.text)
print("\n" * 10)

# GRABBING AN IMAGE
req = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(req.text, 'lxml')
images = soup.select('.thumbimage')
print(images)
computer = soup.select('.thumbimage')[0]

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
f = open('C:\\Users\\myname\\Desktop\\New folder\\my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()

