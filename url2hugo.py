#!/usr/bin/env python3

import os
import re
from datetime import datetime

import requests
import trafilatura
from bs4 import BeautifulSoup


def sanitize_filename(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def extract_title(html):
    soup = BeautifulSoup(html, "html.parser")

    if soup.title and soup.title.string:
        return soup.title.string.strip()

    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)

    return "Untitled"


def url_to_markdown(url):

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    response.raise_for_status()

    html = response.text

    title = extract_title(html)

    markdown_body = trafilatura.extract(
        html,
        output_format="markdown",
        include_links=True,
        include_images=False
    )

    if not markdown_body:
        raise RuntimeError("본문 추출 실패")

    today = datetime.now().strftime("%Y-%m-%d")

    frontmatter = f"""---
title: "{title}"
source_url: "{url}"
date: {today}
draft: false
---

"""

    filename = sanitize_filename(title) + ".md"

    os.makedirs("content/imported", exist_ok=True)

    output_file = os.path.join(
        "content/imported",
        filename
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(markdown_body)

    print(f"생성 완료: {output_file}")


if __name__ == "__main__":

    url = input("URL 입력: ").strip()

    url_to_markdown(url)

