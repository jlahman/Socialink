from flask import Flask, jsonify, request
from markupsafe import escape
import AvatarGrabber

app = Flask(__name__)

@app.route("/Sites/Github/<username>", methods=['GET'])
def githubAvatarEndpoint(username):
	grabber = AvatarGrabber.AvatarGrabber()
	url = grabber.grabAvatarGithub(escape(username))
	return jsonify({"src_url" : url})
