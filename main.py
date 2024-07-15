from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def load_proxies(filename):
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

def watch_youtube_videos(video_urls, watch_time, proxies):
    video_index = 0
    while True:
        if video_index >= len(video_urls):
            video_index = 0

        url = video_urls[video_index]
        proxy = random.choice(proxies)
        print(f'using proxy: {proxy}')

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f'--proxy-server=http://{proxy}')

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.126/127 Safari/537.36"
        chrome_options.add_argument(f'user-agent={user_agent}')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get(url)
            print(f'Watching video: {url}')
            time.sleep(watch_time)
            print(f'Finished watching video for {watch_time} seconds')
        except Exception as e:
            print(f'Error watching video {url}: {str(e)}')
        finally:
            driver.quit()

        video_index += 1

proxies = load_proxies('httpProxy.txt')

video_urls = input("enter the YouTube video urls and seperate them by commas: ").split(",")

watch_time = int(input("watchtime in sec: "))
watch_youtube_videos(video_urls, watch_time, proxies)