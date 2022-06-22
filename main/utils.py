import json


def read_json():
    """Unpacking json file"""
    with open("./posts.json") as file:
        all_posts = json.load(file)
    return all_posts


def search_post(all_posts, word):
    """Find the posts by the word"""
    founded_posts = []
    for post in all_posts:
        if word.lower() in post["content"].lower():
            founded_posts.append(post)
    return founded_posts


def json_writer(post):
    """Write down a new post"""
    all_posts = read_json()
    all_posts.append(post)
    with open("./posts.json", "w") as file:
        json.dump(all_posts, file, indent=1, ensure_ascii=False)


def check_extension(picture):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    filename = picture.filename.lower()
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False

