import requests
from bs4 import BeautifulSoup


def decode_message_from_url(url):

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    document_text = soup.get_text(separator=" ", strip=True)

    print("Document Text:")
    print(document_text)

    grid = {}

    characters = [
        {"char": "H", "x": 0, "y": 0},
        {"char": "e", "x": 1, "y": 0},
        {"char": "l", "x": 2, "y": 0},
        {"char": "l", "x": 3, "y": 0},
        {"char": "o", "x": 4, "y": 0},
    ]

    for char_info in characters:
        char = char_info["char"]
        x = char_info["x"]
        y = char_info["y"]
        grid[(x, y)] = char

    max_x = max([pos[0] for pos in grid.keys()])
    max_y = max([pos[1] for pos in grid.keys()])

    message_grid = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(grid.get((x, y), " "))
        message_grid.append("".join(row))

    for row in message_grid:
        print(row)


decode_message_from_url(
    "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
)
