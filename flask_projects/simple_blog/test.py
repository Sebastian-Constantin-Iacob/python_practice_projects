import requests
import post


post_json = post.Post
print(post_json.data)

# Get all posts
def get_all_posts(post_json):
    for x in post_json:
        print(x['title'])


get_all_posts(post_json)
