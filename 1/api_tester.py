import subprocess
import json

def make_request(url):
    result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
    return result.stdout

def test_endpoint(url, key_elements):
    response = make_request(url)
    try:
        data = json.loads(response)
        for element in key_elements:
            if element not in data:
                print(f"Test {url}: FAILED (missing {element})")
                return
        print(f"Test {url}: PASSED")
    except json.JSONDecodeError:
        print(f"Test {url}: FAILED (invalid JSON)")

tests = [
    {
        "url": "https://jsonplaceholder.typicode.com/posts/1",
        "key_elements": ["userId", "id", "title", "body"]
    },
    {
        "url": "https://jsonplaceholder.typicode.com/comments/1",
        "key_elements": ["postId", "id", "name", "email", "body"]
    },
    {
        "url": "https://jsonplaceholder.typicode.com/albums/1",
        "key_elements": ["userId", "id", "title"]
    }
]

for test in tests:
    test_endpoint(test["url"], test["key_elements"])
