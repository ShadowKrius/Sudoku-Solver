import requests

def fetch_sudoku_board():
    url = "https://sudoku-generator3.p.rapidapi.com/generate"
    payload = {
        "difficulty": "hard",
        "spaces": ".",
        "candidates": True,
        "list": False,
        "grid": True
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "d6aea4a5a0msh62b897a578090bcp14e351jsn5491467e9233",
        "X-RapidAPI-Host": "sudoku-generator3.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()["grid"]
