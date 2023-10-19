import requests

# Define your API key
api_key = "pqlcywj9X23Yr9Xls0VhUaX4SOaHqAwJ8X3bjUlD"

# ...

# get count of jokes on server
count_response = requests.get("https://api.cancer.gov" + "/count", headers={"Authorization": f"Bearer {api_key}"})
count_json = count_response.json()
count = count_json['count']

# update likes/dislikes test sequence
num = str(random.randint(0, count - 1))  # test a random record
responses.append(
    requests.get("https://api.cancer.gov" + "/" + num, headers={"Authorization": f"Bearer {api_key}"})  # read joke by id
)
responses.append(
    requests.put("https://api.cancer.gov" + "/like/" + num, headers={"Authorization": f"Bearer {api_key}"})  # add to like count
)
responses.append(
    requests.put("https://api.cancer.gov" + "/jeer/" + num, headers={"Authorization": f"Bearer {api_key}"})  # add to jeer count
)

# obtain a random joke
responses.append(
    requests.get("https://api.cancer.gov" + "/random", headers={"Authorization": f"Bearer {api_key}"})  # read a random joke
)

# ...
