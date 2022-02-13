import undetected_chromedriver as uc
from time import sleep 

username = input("username: ")
password = input("password: ")
search_for = input("what side of youtube would you like to see ? ").replace(" ", "+")
# open web browser and site
browser = uc.Chrome(use_subprocess=True)
browser.get("https://www.youtube.com/")
sleep(2)
#sign into youtube

browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer").click()
browser.find_element_by_name("identifier").send_keys(username)
sleep(1)
browser.find_element_by_class_name("VfPpkd-vQzf8d").click()
sleep(2)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_class_name("VfPpkd-vQzf8d").click()
sleep(1)
browser.get(f"https://www.youtube.com/results?search_query={search_for}")

# browser.get(f"https://www.youtube.com/results?search_query={search_for}&sp=CAI%253D") use this to search by most recent
for i in range(1,10):
    browser.find_element_by_xpath(f"/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/ytd-thumbnail/a").click()
    sleep(30)
    browser.execute_script("window.history.go(-1)")