import requests
from bs4 import BeautifulSoup
from pytube import YouTube

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract relevant information (customize based on website structure)
    text = soup.get_text()
    return text

def scrape_youtube(url):
    yt = YouTube(url)
    # Download video or extract relevant information
    caption = yt.captions.get_by_language_code('en')
    if caption:
        return caption.generate_srt_captions()
    else:
        return "No captions available"
