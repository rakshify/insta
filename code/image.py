

class Image():
	def __init__(self, code = None, gating_info = None, height = None, width = None, thumbnail_resources = None,\
				  comments_disabled = False, typename = None, comments = 0, date = None, media_preview = None,\
				  likes = 0, owner = None, thumbnail_src = None, is_video = False, id = None, display_src = None):
		self.code = code
		self.gating_info = gating_info
		self.height = height
		self.width = width
		self.thumbnail_resources = thumbnail_resources
		self.comments_disabled = comments_disabled
		self.typename = typename
		self.comments = comments
		self.date = date
		self.media_preview = media_preview
		self.likes = likes
		self.owner = owner
		self.thumbnail_src = thumbnail_src
		self.is_video = is_video
		self.id = id
		self.display_src = display_src