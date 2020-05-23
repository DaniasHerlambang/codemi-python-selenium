from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

def login_twitter(username, password, text, path_image):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    driver.maximize_window()

    #login
    username_field = driver.find_element_by_xpath("//input[contains(@name,'username')]")
    # username_field = driver.find_element_by_name("session[username_or_email]")
    password_field = driver.find_element_by_name("session[password]")

    username_field.send_keys(username)
    driver.implicitly_wait(5)

    password_field.send_keys(password)
    driver.implicitly_wait(5)

    #click login
    driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(8) > div").click()
    driver.implicitly_wait(5)

    #post text
    autotw1 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-xoduu5 r-1sp51qo r-mk0yit r-13qz1uu']")))
    ActionChains(driver).move_to_element(autotw1).click(autotw1).send_keys("post test codemi 2020").perform()

    #post image
    element = driver.find_element_by_xpath("//input[@type='file']")
    driver.execute_script("arguments[0].style.display = 'block';", element)
    element.send_keys(path_image)

    #click tweet
    tweet = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]')))
    tweet.click()
    sleep(15)

if __name__ == "__main__":
    # username = '08998934074'
    # password = 'herlambang13'
    # text     = 'post test codemi 2020'
    # # print ('\n')
    # # print ('example full path image = /home/dns/BACKGROUND/photo-1500907789384-0c3b4c3bdce4.jpeg')
    # path_image     = '/home/dns/BACKGROUND/photo-1500907789384-0c3b4c3bdce4.jpeg'

    username = input("user name : ")
    password = getpass("password  : ")
    text     = input("text tweet : ")
    print ('\n')
    print ('example full path image = /home/dns/BACKGROUND/photo-1500907789384-0c3b4c3bdce4.jpeg')
    print ('\n')

    path_image     = input("full path image : ")
    # username = input("user name : ")
    # password = getpass("password  : ")
    login_twitter(username, password, text , path_image)
