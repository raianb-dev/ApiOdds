from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import uuid
import re
import platform
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display

def scrap_flashscore(url):
    # Inicie o Xvfb
    display = Display(visible=0, size=(1920, 1080))
    display.start()

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=9222')

    # Especifique o caminho do binário do Chrome
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Atualize este caminho se necessário

    if platform.system() == 'Linux':
        service = Service(executable_path='./chromedriver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        try:
            banner_cookies = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'onetrust-banner-sdk')))
            accept_button = banner_cookies.find_element(By.ID, 'onetrust-accept-btn-handler')
            accept_button.click()
        except Exception as e:
            print(f"Erro ao aceitar cookies: {e}")

        try:
            odds_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="live-table"]/div[1]/div[1]/div[3]/div'))
            )
            odds_tab.click()
        except Exception as e:
            print(f"Erro ao clicar em 'Odds': {e}")

        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, 'html/div')))
        except Exception as e:
            print(f"Erro ao esperar a seção de jogos ao vivo: {e}")

        jogos_elements = driver.find_elements(By.XPATH, '//*[@id="live-table"]/section/div/div[1]//div[contains(@class, "event__time")]/ancestor::div[contains(@class, "event__match")]')

        lista_horarios_times_odds = []
        time.sleep(15)

        for jogo_element in jogos_elements:
            try:
                horario_element = jogo_element.find_element(By.XPATH, './/div[contains(@class, "event__time")]')
                horario_encontrado = horario_element.text.strip()

                times_elements = jogo_element.find_elements(By.XPATH, './/div[contains(@class, "event__participant")]')

                if len(times_elements) == 2:
                    times_encontrados = [time_element.text.strip() for time_element in times_elements]

                    odds_elements = jogo_element.find_elements(By.XPATH, './/div[contains(@class, "odds__odd")]')
                    odds_encontradas = []

                    for odd_element in odds_elements:
                        odd_text = odd_element.get_attribute("title")
                        odd_value = re.search(r'\[u\](\d+\.\d+)|\[d\](\d+\.\d+)', odd_text)
                        if odd_value:
                            odds_encontradas.append(odd_value.group(1) or odd_value.group(2))

                    if (horario_encontrado and len(times_encontrados) == 2) or (horario_encontrado and odds_encontradas):
                        id = str(uuid.uuid4())
                        jogo_info = {
                            "id": f"{id}",
                            "home": {
                                "name": times_encontrados[0],
                                "odd-home": float(odds_encontradas[0])
                            },
                            "out": {
                                "name": times_encontrados[1],
                                "odd-out": float(odds_encontradas[2])
                            },
                            "tie": {
                                "odd": float(odds_encontradas[1])
                            },
                            "time": horario_encontrado
                        }
                        lista_horarios_times_odds.append(jogo_info)
            except Exception as e:
                print(f"Erro ao extrair informações de um jogo: {e}")

        if lista_horarios_times_odds:
            return lista_horarios_times_odds
        else:
            return {"message": "Nenhum jogo encontrado", "jogos": []}

    except Exception as e:
        print(f"Erro durante a execução do script: {e}")

    finally:
        if driver:
            driver.quit()
        display.stop()
