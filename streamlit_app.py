import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = get_driver()


    if True:
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
