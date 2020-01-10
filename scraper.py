_author_ = "Joey w/ help from coaches"

from bs4 import BeautifulSoup
import argparse
import requests
import re

def fetch_html(url):
    res = requests.get(url)
    return res.text

def scrape_url(html):
    urls = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
    return list(set(urls))

def scrape_emails(html):
    emails = re.findall(
        r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", html)
    return list(set(emails))


def scrape_phone_numbers(html):
    digis = re.findall(
        r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?", html)
    return list(set(digis))


def img_tags(content):
    return list(set(content.select('img')))


def link_tags(content):
    return list(set(content.select('a[href]')))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('website')
    args = parser.parse_args()
    website = args.website
    html = fetch_html(website)
    urls = scrape_url(html)
    emails = scrape_emails(html)
    digis = scrape_phone_numbers(html)
    print("URLS:")
    for url in urls:
        print(url)
    print("Emails:")
    for email in emails:
        print (email)
    print("Phone Numbers:")
    for digi in digis:
        print("{}-{}-{}".format(digi[0], digi[1], digi[2]))
    content = BeautifulSoup(html, "html.parser")
    imgs = img_tags(content)
    print(type(imgs))
    links = link_tags(content)
    for img in imgs:
        print("# {} #".format(img))
    for link in links:
        print(str(link))


if __name__ == "__main__":
    main()

