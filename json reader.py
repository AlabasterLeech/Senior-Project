import json
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

BASE_URL = "https://www.fussball.de/homepage#!/"

options = Options()
options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
driver = webdriver.Chrome(options=options)

driver.get(BASE_URL)
sleep(5)

logs_raw = driver.get_log("performance")
# Logs is mostly Headers and Initiators from Netowrk in DevTools
logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

def log_filter(log_):
    return (
        log_["method"] == "Network.responseReceived" 
        and "json" in log_["params"]["response"]["mimeType"]
    )

for log in filter(log_filter, logs):
    request_id = log["params"]["requestId"]
    resp_url = log["params"]["response"]["url"]
    open(str(resp_url)[-6:], "w").write(json.dumps(driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})),indent=4)