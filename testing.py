

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

                            

def random_num_sleep ( range =(0.4, 0.6)):
    return random.uniform(range[0],range[1])
                        







from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import requests
from PIL import Image
from io import BytesIO
import uuid

import hashlib
import os
from PIL import Image
import io

def quality_check(url):
    
    
    
    try:
        response = requests.get(url,timeout=10)  # Disable SSL certificate verification
        if str(response.status_code)[0] == "2":
            image_bytes = response.content
            # Open the image using PIL
            image = Image.open(BytesIO(image_bytes))


            width, height = image.size
            if width > 300 or height > 300:
                
                return True, image

            else:False, None
    except: return False, None 





def save_img(img,topic, save_folder="./backgrounds",):
    # Convert image to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Generate hash
    hash_object = hashlib.md5(img_byte_arr)
    img_hash = hash_object.hexdigest()

    # Create filename using hash
    filename = f"{img_hash}.png"
    filepath = os.path.join(save_folder+f"/{topic}", filename)

    # Check if file already exists
    if os.path.exists(filepath):
        print(f"Image with hash {img_hash} already exists.")
        return None

    # Save the image
    img.save(filepath)
    print(f"Image saved as {filename}")



def main_scrape(topic_to_scrape, ignore_websites_that_ban=True, unique_urls = True, target_images =100, quality_function=quality_check, save_folder ="./backgrounds"):


    print("____________________")
    print(topic_to_scrape)
    print("____________________")


    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    

    if not os.path.exists(save_folder+ "/"+ topic_to_scrape):
        os.makedirs(save_folder+ "/"+ topic_to_scrape)
    

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")  # Add this line
    chrome_options.binary_location = "/usr/bin/google-chrome-stable"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.google.com")


    ActionChains(driver)\
        .send_keys(topic_to_scrape)\
        .key_up(Keys.SHIFT)\
        .send_keys(Keys.RETURN)\
        .perform()


    button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@jsname='bVqjv' and @class='YmvwI' and text()='Images']"))
            
            )

    button.click()




    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@jsname='dTDiAc']")))

   




    urls = set()



    # Loop through the elements and find the images within each
    for idx, element in enumerate(elements):
        try:

            random_num_sleep(range=(0.2,0.4))

            element =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@jsname='dTDiAc']")))[idx]





            print("back on top")
            original_url = driver.current_url
            wait.until(
            EC.element_to_be_clickable((element)))

            element.click()
            
            # Find the img element within the current div
            img = element.find_element(By.XPATH, ".//img")

            
            # Find the anchor element that contains the full-size image URL
            anchor = element.find_element(By.XPATH, ".//a[contains(@href, '/imgres')]")
            
            # Get the href attribute which contains the full URL
            full_url = anchor.get_attribute("href")
            
            # Extract the actual image URL from the href
            import urllib.parse
            parsed_url = urllib.parse.urlparse(full_url)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            full_image_url = query_params.get('imgurl', [''])[0]
            if any(keyword in full_image_url.lower() for keyword in ["amazon", ]):
                    pass


            else:
                res, img = quality_function(full_image_url)                
                
                
                if res == True and full_image_url not in urls:
                    save_img(img,topic=topic_to_scrape)

                    urls.add(full_image_url)



            see_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'CCYCud')]//div[text()='See more']")))


            see_more_button.click()



            #second loop

            wait = WebDriverWait(driver, 10)
            related_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@jsname='dTDiAc']")))

            print(f"related elements: {len(related_elements)}")


            # Loop through the elements and find the images within each
            for related_element in related_elements:
                try:
                    random_num_sleep(range=(0.2,0.6))

                    wait.until(
                    EC.element_to_be_clickable((related_element)))
                    related_element.click()



                    wait.until(
                    EC.element_to_be_clickable((By.XPATH, ".//img")))

                    # Find the img element within the current div
                    img = related_element.find_element(By.XPATH, ".//img")

                    wait.until(
                    EC.element_to_be_clickable((By.XPATH, ".//a[contains(@href, '/imgres')]")))
                    
                    
                    # Find the anchor element that contains the full-size image URL
                    anchor = related_element.find_element(By.XPATH, ".//a[contains(@href, '/imgres')]")
                    
                    # Get the href attribute which contains the full URL
                    full_url = anchor.get_attribute("href")
                    
                    # Extract the actual image URL from the href
                    import urllib.parse
                    parsed_url = urllib.parse.urlparse(full_url)
                    query_params = urllib.parse.parse_qs(parsed_url.query)
                    full_image_url = query_params.get('imgurl', [''])[0]
                    if any(keyword in full_image_url.lower() for keyword in ["amazon", ]):
                            pass


                    else:
                        res, img = quality_function(full_image_url)                
                        
                        
                        if res == True and full_image_url not in urls:
                            save_img(img,topic=topic_to_scrape)


                            urls.add(full_image_url)


                except Exception as e:

    
                    print(e)



            driver.get( original_url)



        except Exception as e:
            print(f"No image found in this element or error occurred: {str(e)}")
    
    
    driver.quit()

    return urls



import multiprocessing


array = ["desk design", "living room ideas", "work office ideas"]

with multiprocessing.Pool() as pool:
    results = pool.map(main_scrape, array)
    
# Unpack the results
urls, urls2, urls3 = results

# Now you can use urls, urls2, and urls3 as before
print(f"Desk design results: {len(urls)}")
print(f"Living room ideas results: {len(urls2)}")
print(f"Work office ideas results: {len(urls3)}")










    
# def generating_urls_for_image_processor(product_name,):
#     chrome_options = Options()
#     chrome_options.add_argument("--no-sandbox")
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1920,1080")
#     chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

#     # Create a new instance of the Chrome driver using webdriver_manager
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     # Navigate to DuckDuckGo
#     url = "https://www.duckduckgo.com/"
#     driver.get(url)

#     good_urls = []


#     search_box = driver.find_element("name", "q")
#     search_box.send_keys(product_name)
#     search_box.send_keys(Keys.RETURN)

#     time.sleep(2)


#     # Navigate to the Images tab
#     images_tab = driver.find_element("link text", "Images")
#     images_tab.click()

#     # Wait for the images to load
#     time.sleep(4)  # Add a delay to allow images to load
#     time.sleep(2)

#     # Take a screenshot of the page and save it as "screenshot.png"

#     image_elements = driver.find_elements(By.CSS_SELECTOR, '.tile.tile--img.has-detail')
#     total_images = len(image_elements)
#     print(total_images, file=sys.stderr)
#     time.sleep(2)

    
 
#     #TODO start end 


#     try:
#         # for i, element in enumerate(image_elements[start:end], start=start):
#         for i, element in enumerate(image_elements):




#                 time.sleep(random_num_half_a_second())

#                 try:
#                     print(len(good_urls))
#                     element.click()
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.c-detail__btn.c-detail__btn--bottom.btn.js-image-detail-link')))
#                     href_element = driver.find_element(By.CSS_SELECTOR, '.c-detail__btn.c-detail__btn--bottom.btn.js-image-detail-link')
#                     href_value = href_element.get_attribute('href')

#                     if any(keyword in href_value.lower() for keyword in ["amazon", ]):
#                         continue

#                     if any(keyword in href_value.lower() for keyword in ["playforce", ]):
#                         continue

#                     good_urls.append(href_value)
       
                    
                 
#                 except Exception as e:
#                     print("Error:", file=sys.stderr)
#                     print(e, file=sys.stderr)
#                     continue



#     except Exception as e:
#         print("Error:", file=sys.stderr)
#         print(e, file=sys.stderr)

#     driver.close()
#     gc.collect
#     return good_urls


# generating_urls_for_image_processor("desk",)