from toapi import Api
from items.page import Page
from items.post import Post
from items.user import User
from settings import MySettings

api = Api('https://news.ycombinator.com/', settings=MySettings)
api.register(User)
api.register(Page)
api.register(Post)

if __name__ == '__main__':
  api.serve()
