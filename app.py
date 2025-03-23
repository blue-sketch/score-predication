import http.client

conn = http.client.HTTPSConnection("free-cricbuzz-cricket-api.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "6342f7da9emshfdc337fa9bea93ap183088jsn485a25451373",
    'x-rapidapi-host': "free-cricbuzz-cricket-api.p.rapidapi.com"
}

conn.request("GET", "/cricket-match-info?matchid=102040", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
