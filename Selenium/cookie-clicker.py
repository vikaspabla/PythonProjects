from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver = "C:/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

five_sec = time.time() + 5
five_min = time.time() + 300

cookie = driver.find_element(By.ID, "cookie")


while True:
    cookie.click()
    if time.time() > five_sec:

        try:
            products = driver.find_elements(By.CSS_SELECTOR, "#store div")
            product_ids = [item.get_attribute("id") for item in products]
            product_ids.reverse()
            cookie = driver.find_element(By.ID, "cookie")
        except:
            pass
        for product in product_ids:
            try:
                buy = driver.find_element(By.CSS_SELECTOR, f"#{product}")
                buy.click()

            except:
                pass

            five_sec = five_sec + 5
    if time.time() > five_min:
        cookies_per_sec = driver.find_element(By.ID, "cps")
        print(cookies_per_sec.text)

        break

driver.close()


# while True:
#     cookie.click()
#
#     if time.time() > five_sec:
#
#         grayed_products = driver.find_elements(By.CSS_SELECTOR, ".grayed b")
#         not_available_products = [g.text.split("-")[0].strip() for g in grayed_products]
#         available_products = [a for a in all_products if a not in not_available_products]

        # if len(available_products) > 0:
            #
            # buy = available_products[-1]
            # buy_product = driver.find_element(
            # # bought_product = buy_product.get_attribute("onclick")
            #
            #
            # print(f"Bought:{buy}")

    #     five_sec = time.time() + 5
    #
    # if time.time() > five_min:
    #
    #     cookies_per_sec = driver.find_element(By.ID, "cps")
    #     print(cookies_per_sec.text)
    #     break
    #






