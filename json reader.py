import json
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

BASE_URL = "https://www.fussball.de/homepage#!/"

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.ChromeOptions()

driver.set_capability("loggingPrefs", {"performance": "ALL"})

driver = webdriver.Remote(
    service=service,options=driver
)

driver.get(BASE_URL)
sleep(5)

logs_raw = driver.get_log("performance")
logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

def log_filter(log_):
    return (
        log_["method"] == "Network.responseReceived"
        and "json" in log_["params"]["response"]["mimeType"]
    )

for log in filter(log_filter, logs):
    request_id = log["params"]["requestId"]
    resp_url = log["params"]["response"]["url"]
    print(f"Caught {resp_url}")
    print(driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id}))