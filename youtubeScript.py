from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 

username = input("username: ")
password = input("password: ")
search_for = input("what side of youtube would you like to see ? ")
# open web browser and site
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.youtube.com/")
sleep(2)
#sign into youtube
browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer").click()
browser.find_element_by_name("identifier").send_keys(username)
sleep(1)
browser.find_element_by_class_name("VfPpkd-vQzf8d").click()
sleep(10)
browser.find_element_by_class_name("OabDMe cXrdqd Y2Zypf").send_keys(password)
browser.find_element_by_class_name("OabDMe cXrdqd Y2Zypf").click()
sleep(1)
browser.get(f"https://www.youtube.com/results?search_query={search_for}&sp=CAI%253D")

# browser.get(f"https://www.youtube.com/results?search_query={search_for}&sp=CAI%253D") use this to search by most recent
browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a").click()
sleep(10)