import urllib.request
import json
blog_content = urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts").read()
print(blog_content)
str_blog_content=blog_content.decode("utf-8")
list_blog_content = json.loads(str_blog_content)
print(str_blog_content)
user_post_id = input("What is your post id?")

values = range(100)
for i in values:
    print(i)
    

    




 