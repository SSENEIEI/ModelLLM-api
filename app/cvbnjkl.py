import requests

prompt = {
    "prompt":" ",
    "n_predict":256,
    "temperature":0.7,
    "stop": ["</eos>"]
}

# response = requests.post("http://127.0.0.1:8080/completion",json=prompt)
headers = {}
response = requests.post("https://model.abdul.in.th/izanagi/completion",json=prompt,headers=headers)

print(response.json())