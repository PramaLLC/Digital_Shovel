

import gc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sys



import base64

# import concurrent.futures


from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager





# from sklearn.metrics.pairwise import cosine

                            

def random_num_half_a_second():
    return random.uniform(0.4, 0.6)
                        









 
    
def generating_urls_for_image_processor(product_name, start):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    # Create a new instance of the Chrome driver using webdriver_manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to DuckDuckGo
    url = "https://www.duckduckgo.com/"
    driver.get(url)

    good_urls = []


    search_box = driver.find_element("name", "q")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)


    # Navigate to the Images tab
    images_tab = driver.find_element("link text", "Images")
    images_tab.click()

    # Wait for the images to load
    time.sleep(4)  # Add a delay to allow images to load
    time.sleep(2)

    # Take a screenshot of the page and save it as "screenshot.png"

    image_elements = driver.find_elements(By.CSS_SELECTOR, '.tile.tile--img.has-detail')
    total_images = len(image_elements)
    print(total_images, file=sys.stderr)
    time.sleep(2)


 
    #TODO start end 


    try:
        # for i, element in enumerate(image_elements[start:end], start=start):
        for i, element in enumerate(image_elements):




                time.sleep(random_num_half_a_second())

                try:
                    print(len(good_urls))
                    element.click()
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.c-detail__btn.c-detail__btn--bottom.btn.js-image-detail-link')))
                    href_element = driver.find_element(By.CSS_SELECTOR, '.c-detail__btn.c-detail__btn--bottom.btn.js-image-detail-link')
                    href_value = href_element.get_attribute('href')

                    if any(keyword in href_value.lower() for keyword in ["amazon", ]):
                        continue

                    if any(keyword in href_value.lower() for keyword in ["playforce", ]):
                        continue

                    good_urls.append(href_value)
       
                    
                 
                except Exception as e:
                    print("Error:", file=sys.stderr)
                    print(e, file=sys.stderr)
                    continue



    except Exception as e:
        print("Error:", file=sys.stderr)
        print(e, file=sys.stderr)

    driver.close()
    gc.collect
    return good_urls


