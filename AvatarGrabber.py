import re
from urllib.request import urlopen
import urllib.request

class AvatarGrabber:
	def grabAvatarGithub(self, url: str) -> str:
		page = urlopen(url)
		html_bytes = page.read()
		html = html_bytes.decode("utf-8")

		pattern = "<img .* alt=\"Avatar\".*?>"
		result_ele = re.findall(pattern, html)
		img_url = re.findall("src=\".*\"", result_ele[0])
		img_url = re.sub("src=\"", "", img_url[0])
		img_url = re.sub("\"", "", img_url)
		#urllib.request.urlretrieve(img_url, "avatar_github.png") #for saving the image if needed
		return img_url

print(AvatarGrabber().grabAvatarGithub("https://github.com/Keilith-L"))