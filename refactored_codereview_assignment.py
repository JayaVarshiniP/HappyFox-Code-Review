from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Constants for configuration
GECKO_DRIVER_PATH = "./drivers/geckodriver.exe"
BASE_URL = "https://interview.supporthive.com/staff/"
USERNAME = "Agent"
PASSWORD = "Agent@123"
STATUS_COLOR = "#47963f"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Testcase101:

    def run_test_case(self):
        driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        try:
            driver.get(BASE_URL)
            driver.implicitly_wait(10)

            driver.find_element(By.ID, "id_username").send_keys(USERNAME)
            driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
            driver.find_element(By.ID, "btn-submit").click()

            tickets = wait.until(EC.presence_of_element_located((By.ID, "ember29")))
            ActionChains(driver).move_to_element(tickets).perform()

            driver.find_element(By.LINK_TEXT, "Statuses").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//header/button"))).click()
            driver.find_element(By.TAG_NAME, "input").send_keys("Issue Created")

            driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']").click()
            color_input = driver.find_element(By.XPATH, "//input[@class='sp-input']")
            color_input.clear()
            color_input.send_keys(STATUS_COLOR)

            first_element = wait.until(EC.element_to_be_clickable((By.ID, "first-link")))
            first_element.click()
            driver.find_element(By.ID, "second-link").click()

            driver.find_element(By.TAG_NAME, "textarea").send_keys("Status when a new ticket is created in HappyFox")
            driver.find_element(By.XPATH, "//button[contains(@class,'hf-primary-action')]").click()

            move_to = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class,'lt-cell')]")))
            ActionChains(driver).move_to_element(move_to).perform()
            move_to.click()

            issue = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Issue Created')]")))
            ActionChains(driver).move_to_element(issue).perform()
            driver.find_element(By.LINK_TEXT, "Make Default").click()

            driver.find_element(By.LINK_TEXT, "Priorities").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//header/button[1]"))).click()
            driver.find_element(By.TAG_NAME, "input").send_keys("Assistance required")
            driver.find_element(By.TAG_NAME, "textarea").send_keys("Priority of the newly created tickets")
            driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']").click()

            tickets2 = wait.until(EC.presence_of_element_located((By.ID, "ember29")))
            ActionChains(driver).move_to_element(tickets2).perform()
            driver.find_element(By.LINK_TEXT, "Priorities").click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//table/tbody/tr[last()]/td[2]"))).click()
            driver.find_element(By.LINK_TEXT, "Delete").click()
            driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']").click()

            wait.until(EC.element_to_be_clickable((By.XPATH, "//header/div[2]/nav/div[7]/div/div"))).click()
            driver.find_element(By.LINK_TEXT, "Logout").click()

        finally:
            driver.quit()


class PagesforAutomationAssignment:

    def execute_login_flow(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)

        try:
            driver.get("https://www.happyfox.com")
            login_page = LoginPage(driver)
            login_page.login("username", "password")

            home_page = HomePage(driver)
            home_page.verify_home_page(wait)

        finally:
            driver.quit()


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()


class HomePage(BasePage):

    def verify_home_page(self, wait):
        wait.until(EC.url_contains("/home"))
        if "/home" not in self.driver.current_url:
            raise Exception("Home page not loaded correctly.")

    def navigate_to_profile(self):
        self.driver.find_element(By.ID, "profileLink").click()


class TablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.row_locator = (By.XPATH, "//table[@id='dataTable']/tbody/tr")

    def retrieve_row_texts(self):
        rows = self.driver.find_elements(*self.row_locator)
        for i, row in enumerate(rows):
            logging.info(f"Row {i} Text: {row.text}")


if __name__ == "__main__":
    Testcase101().run_test_case()
