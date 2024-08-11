import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
from datetime import datetime

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)


try:
    driver.get("https://hypixel.net/online")

    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button--notice"))
        )
        accept_cookies_button.click()
        print("cookies whoah")
    except Exception as e:
        print(f"me when error:: {e}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login")) 
    )

    time.sleep(5)
    username_field = driver.find_element(By.NAME, "login")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("PerfectTierSquidward") 
    time.sleep(1)
    password_field.send_keys("nifurox123") 

    password_field.send_keys(Keys.RETURN)

    print ("Logged in")
    time.sleep(5)

    with open("element_data.txt", "a") as file:
        while True:
            try:
               
                driver.refresh()

                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "dl.pairs:nth-child(1) > dd:nth-child(2)"))
                )

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                file.write(f"{current_time}: {element.text}\n")
                file.flush()
                print(f"{current_time}: {element.text}")

            except Exception as e:
                print(f"sad error: {e}")

            time.sleep(5)

finally:
    driver.quit()
