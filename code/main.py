import requests, re, json
from bs4 import BeautifulSoup as bs
from user import User

visited = {}
t = "http://rampinta.com/"
ti = "http://instagram.com/"
user_count = 0

def get_user(data):
	u = data["entry_data"]["ProfilePage"][0]["user"]
	followers = u["followed_by"]["count"]
	following = u["follows"]["count"]
	nodes = u["media"]["nodes"]

	return User(followers = followers, following = following, nodes = nodes)

def process_insta(url):
	r = requests.get(url)
	data = r.text
	soup = bs(data, 'html.parser')
	scripts = soup.find_all("script")
	p = re.compile('window\._sharedData = (.*?);')
	d = None
	for s in scripts:
		str = s.string
		if str:
			m = p.match(str)
			if m:
				d = json.loads(m.groups()[0])

	return get_user(d)


def process_url(uname):
	global user_count
	if user_count == 3:
		return
	print "*****************" + uname + "*************************"
	user_count += 1
	url = t + uname
	visited[uname] = process_insta(ti + uname)
	r = requests.get(url)
	data = r.text
	soup = bs(data, 'html.parser')
	user_divs = soup.find_all("div", class_ = "col-md-12 col-xs-12 users-box")
	followers = user_divs[1].find("ul")
	following = user_divs[2].find("ul")
	fersli = followers.find_all("li")
	fingli = following.find_all("li")
	for fers in fersli:
		anchor = fers.find("a")
		fers_name = anchor.attrs["title"].split("@")[1][:-1]
		# print fers_name
		process_url(fers_name)
	for fing in fingli:
		anchor = fing.find("a")
		fing_name = anchor.attrs["title"].split("@")[1][:-1]
		process_url(fing_name)

process_url("rakshify")