import requests


def ai(content: str):
    url = "http://10.38.60.151:4023/api/openai/chat"
    data = {"model": "qwen3-30b-a3b",
            "stream": True,
            "frequency_penalty": 0.1,
            "presence_penalty": 0,
            "temperature": 0.3,
            "top_p": 0.7,
            "messages": [{"content": content, "role": "user"}]}

    respons = requests.post(url=url, json=data).text
    return respons


if __name__ == '__main__':
    content = "你好"
    respons = ai(content)
    print(respons)
