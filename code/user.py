from image import Image

class User():
	def __init__(self, followers = 0, following = 0, nodes = []):
		self.followers = followers
		self.following = following
		self.posts = []
		for node in nodes:
			post = Image(node["code"], node["gating_info"], node["dimensions"]["height"], node["dimensions"]["width"],\
						node["thumbnail_resources"], node["comments_disabled"], node["__typename"],\
						node["comments"]["count"], node["date"], node["media_preview"], node["likes"]["count"],\
						node["owner"], node["thumbnail_src"], node["is_video"], node["id"], node["display_src"])
			print post.display_src
			self.posts.append(post)