from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_options = Options()
firefox_options.headless = False

driver = webdriver.Firefox(options=firefox_options)

driver.get('https://atg.party/?redirect_uri=article')

x=driver.find_element(By.XPATH,'/html/body/nav/div/div/div/div[2]/div/button[2]')
x.click()
y=driver.find_element(By.ID,"email_landing")
y.send_keys("wiz_saurabh@rediffmail.com")
z=driver.find_element(By.ID,"password_landing")
z.send_keys("Pass@123")
driver.find_element(By.XPATH,"/html/body/div[5]/header/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button").click()

a=driver.find_element(By.ID,'title')
a.send_keys("hello world")
b=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div/div/div")
b.send_keys("abc")

c=driver.find_element(By.XPATH,'//*[@id="hpost_btn"]')
c.click()

driver.implicitly_wait(500)
driver.quit()
