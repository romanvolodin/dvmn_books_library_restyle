import os
from urllib.parse import urljoin, urlparse, unquote

import requests
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def parse_book_title(html_page):
    soup = BeautifulSoup(html_page, "lxml")
    title, *_ = soup.find("h1").text.split("::")
    return title.strip()


def parse_book_cover_url(html_page):
    soup = BeautifulSoup(html_page, "lxml")
    cover = soup.find("div", class_="bookimage").find("a").find("img")["src"]
    return cover


def parse_book_comment_texts(html_page):
    comment_texts = []
    soup = BeautifulSoup(html_page, "lxml")
    comments = soup.find_all("div", class_="texts")
    for comment in comments:
        comment_texts.append(comment.find("span", class_="black").text)
    return comment_texts


def parse_book_genres(html_page):
    soup = BeautifulSoup(html_page, "lxml")
    genres = soup.find("span", class_="d_book").find_all("a")
    return [genre.text for genre in genres]


def download_txt(url, filename, params=None, folder='books/'):
    response = requests.get(url, params)
    response.raise_for_status()

    save_path = "{}.txt".format(
        os.path.join(folder, sanitize_filename(filename))
    )
    with open(save_path, "w") as file:
        file.write(response.text)
    return save_path


def download_image(url, params=None, folder='images/'):
    response = requests.get(url, params)
    response.raise_for_status()

    parsed_url = urlparse(unquote(url))

    save_path = os.path.join(folder, os.path.basename(parsed_url.path))
    with open(save_path, "wb") as file:
        file.write(response.content)
    return save_path


def save_comments(filename, comment_texts, folder='comments/'):
    save_path = os.path.join(folder, filename)
    with open(save_path, "w") as file:
        file.write('\n\n'.join(comment_texts))
    return save_path


def main():
    books_dir = "books"
    images_dir = "images"
    comments_dir = "comments"

    os.makedirs(books_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(comments_dir, exist_ok=True)

    for book_id in range(1, 11):
        book_url = f"http://tululu.org/b{book_id}/"
        book_text_url = f"https://tululu.org/txt.php?id={book_id}"

        response = requests.get(book_url)
        response.raise_for_status()
        try:
            check_for_redirect(response)
            title = parse_book_title(response.text)
            cover_url = urljoin(
                response.url, parse_book_cover_url(response.text)
            )
            comments = parse_book_comment_texts(response.text)

            download_txt(book_text_url, f"{book_id}. {title}")
            download_image(cover_url)
            if comments:
                save_comments(f"{book_id}. {title}.txt", comments)

        except requests.HTTPError:
            pass


if __name__ == "__main__":
    main()
