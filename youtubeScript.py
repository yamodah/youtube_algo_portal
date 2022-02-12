from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 

search_for = input("what side of youtube would you like to see ? ")
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(f"https://www.youtube.com/results?search_query={search_for}&sp=CAI%253D")
browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a").click()
sleep(10)