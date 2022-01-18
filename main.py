import os
import requests


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def main():
    url = "http://tululu.org/txt.php"
    books_dir = "books"

    os.makedirs(books_dir, exist_ok=True)


    for book_id in range(10):
        params = {"id": book_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        try:
            check_for_redirect(response)
            with open(f"{books_dir}/{book_id}.txt", "w") as book_file:
                book_file.write(response.text)
        except requests.HTTPError:
            pass


if __name__ == "__main__":
    main()