import urllib.request
blog_content = urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts").read()
print(blog_content)