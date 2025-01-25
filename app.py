from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

print('hello!')
print(webdriver.__version__)

DRIVER_PATH = '../../Downloads/chromedriver-mac-arm64/chrome/mac_arm-131.0.6778.267/chrome-mac-arm64/Google Chrome for Testing.app'
options = Options()

# options.add_argument('--headless')  # Optional, run Chrome in headless mode (no UI)
service = Service('../../Downloads/chromedriver-mac-arm64/chromedriver')  # Adjust path to the driver

driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://www.python.org")
driver.get("https://www.amazon.sg/PUMA-Teamgoal-Unisex-Knitted-Shorts/dp/B0C3RRYHC6/ref=sr_1_1?content-id=amzn1.sym.5e505bc2-b07e-47e6-b40c-4822c9c12b88&dib=eyJ2IjoiMSJ9.AgxcRJGeI7JlvMuj6Ma1lTMCvEi-oQO_oCBethE0E2_vhYaZNuP4fbAEFfM3adDKYparfeC1MK7PJoPC9n8RTDWzOX3PhUQLn6yuZ64tHZeXpLa_L_mrrAy2IDMgK-u1fjA3UgqbTXDhS40UWQ20NQ7pd-SYT0xuXJbNQsPeqhmzLUECexy1c96RaqRASZeK40TF8503zTvbXBU1JylTYOaS0Nf6QrJVR3l6MD4dxdE7UKAwLVH_3c4NtUKgtK_AqPD4up07FVfCDaT51dCQfg-k8HICtEOt-lmV3rAo5Xf3D6b-zo7mbuGU4Q3RIkyvb3g8OsGTGs2bETQmgNacqnVeppQ-UksVmjXTbqKbY8xB4Mo2iKs08v0yIy1ORYMoom3LS9b-WSbOSjxL-g5oTIzBKGkstoX3MJsY04BqG_Wu4KkVHEHl7Na9mkMTC1ii.M2TI6e39RiYtwHL-Yygsaf3GMi2WAlK5tyVWYooV6_s&dib_tag=se&m=AYH85219XLWXU&pd_rd_r=0c6cde10-08d8-489b-96fd-b43162f8c19e&pd_rd_w=9ZaaW&pd_rd_wg=2h50f&qid=1737724722&refinements=p_6%3AAYH85219XLWXU&s=fashion&sr=1-1")
time.sleep(3)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

# Now you can use BeautifulSoup methods to locate elements
# element = soup.select_one('img[src]')  # Example: Find the first <img> with an src attribute
# div_element = soup.find('div', id="imgTagWrapperId")
level1_div = soup.find('div', id = 'dp')
level2_div = level1_div.find('div', id = 'dp-container')
lvl3_div = level2_div.find('div', id = 'ppd')
# lvl4_div = lvl3_div.find('div', id = 'a-row')
lvl5_div = lvl3_div.find('div', id = 'leftCol')
lvl6_div = lvl5_div.find('div', id = 'imageBlock_feature_div')
lvl7_div = lvl6_div.find('div', id = 'imageBlock')
lvl8_div = lvl7_div.find('div', id = 'main-image-container')
lvl9_div = lvl8_div.find('div', id = 'imgTagWrapperId')

if lvl9_div:
    # print("level 9 : "+ lvl9_div)
    img_component = lvl9_div.find('img', string='src')
    img_url = lvl9_div.select_one('img[src]')
    # print("Image URL:", lvl9_div['src'])
    print("image url: ", img_component)

print(driver.title)

# xpathstr = '/html/body/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[1]/span/span/div/img'
# element = driver.find_element(By.XPATH, xpathstr)

# # Extract the 'src' attribute using Selenium or find it again in the parsed soup if needed
# image_src = element.get_attribute('src')
# print("Image URL:", image_src)

driver.quit()