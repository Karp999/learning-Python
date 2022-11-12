import json

def getInfo():
    with open("file.json", "r", encoding = "utf-8") as f:
        game = json.load(f)
        return (game)