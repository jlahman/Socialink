import re
import time
from urllib.request import urlopen
import urllib.request

class AvatarGrabber:
	def grabAvatarGithub(self, username: str) -> str:
		url = "https://github.com/"+username
		try:
			page = urlopen(url)
		except:
			return "Not Found"
		html_bytes = page.read()
		html = html_bytes.decode("utf-8")

		pattern = "<img .* alt=\"Avatar\".*?>"
		result_ele = re.findall(pattern, html)
		img_url = re.findall("src=\".*\"", result_ele[0])
		img_url = re.sub("src=\"", "", img_url[0])
		img_url = re.sub("\"", "", img_url)
		#urllib.request.urlretrieve(img_url, "avatar_github.png") #for saving the image if needed
		return img_url

	def grabAvatarTwitter(self, username: str) -> str:
		return "Not Found"
		# Sadly, all of the content on twitter is dynamically loaded with javascript, so we will need an auth token to use the API

		url = "https://twitter.com/"+username+"/photo"
		try:
			page = urlopen(url)
		except:
			return "Not Found"

		time.sleep(5)
		html_bytes = page.read()
		html = html_bytes.decode("utf-8")
		#print(html)

		pattern = "<img .*? alt=\"Opens profile photo\".*?>"
		result_ele = re.findall(pattern, html)
		#print(result_ele)
		img_url = re.findall("src=\".*\"", result_ele[0])
		img_url = re.sub("src=\"", "", img_url[0])
		img_url = re.sub("\"", "", img_url)
		#urllib.request.urlretrieve(img_url, "avatar_github.png") #for saving the image if needed
		return img_url

#print(AvatarGrabber().grabAvatarGithub("https://github.com/Keilith-L"))