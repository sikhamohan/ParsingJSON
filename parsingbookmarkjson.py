import json

def parse_bookmark_node(node, urls):
    if "children" in node:
        for child in node["children"]:
            if "url" in child:
                urls.append(child["url"])
            else:
                parse_bookmark_node(child, urls)

def parse_chrome_bookmarks(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        urls = []
        for root in data["roots"].values():
            parse_bookmark_node(root, urls)
        return urls

# Example usage:
file_path = r"C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Bookmarks"
bookmark_urls = parse_chrome_bookmarks(file_path)
for url in bookmark_urls:
    print(url)
