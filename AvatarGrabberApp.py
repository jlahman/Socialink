from flask import Flask, jsonify, request, abort
from markupsafe import escape
import AvatarGrabber

app = Flask(__name__)

grabbableSites = ["github"]

@app.route("/api/v1/Avatars/<string:sitename>/<string:username>", methods=['GET'])
def githubAvatarEndpoint(sitename, username):
	sitename = escape(sitename)
	username = escape(username)
	if(sitename.lower() not in grabbableSites):
		abort(400)
	grabber = AvatarGrabber.AvatarGrabber()
	url = grabber.grabAvatarGithub(username)
	if(url == "Not Found"):
		abort(404)
	return jsonify({"src_url" : url})

@app.route("/api/v1/ReachableSites", methods=['GET'])
def sitesEndpoint():
	return jsonify({"sites" : ["github"]})
