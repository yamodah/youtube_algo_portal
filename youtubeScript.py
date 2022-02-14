import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep 
from getpass import getpass

username = input("username: ")
password = getpass("password: ")
search_for = input("what side of youtube would you like to see ? ").replace(" ", "+")
# open web browser and site
browser = uc.Chrome(use_subprocess=True)
browser.get("https://www.youtube.com/")
sleep(2)
#sign into youtube
browser.find_element(By.XPATH,"/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer").click()
browser.find_element(By.NAME,"identifier").send_keys(username)
sleep(2)
browser.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d").click()
sleep(2)
browser.find_element(By.NAME,"password").send_keys(password)
browser.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d").click()
sleep(1)
browser.get(f"https://www.youtube.com/results?search_query={search_for}")

# browser.get(f"https://www.youtube.com/results?search_query={search_for}&sp=CAI%253D") use this to search by most recent
for i in range(1,10):
    browser.find_element(By.XPATH,f"/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/ytd-thumbnail/a").click()
    sleep(33)
    browser.execute_script("window.history.go(-1)")