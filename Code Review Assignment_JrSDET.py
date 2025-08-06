from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Testcase101:

    def main(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\Johny\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver.get("https://interview.supporthive.com/staff/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element(By.ID, "id_username").send_keys("Agent")
        driver.find_element(By.ID, "id_password").send_keys("Agent@123")
        driver.find_element(By.ID, "btn-submit").click()
        tickets = driver.find_element(By.ID, "ember29")
        action = ActionChains(driver)
        action.move_to_element(tickets).perform()
        statuses = driver.find_element(By.LINK_TEXT, "Statuses")
        statuses.click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/section/section/div/header/button").click()
        driver.find_element(By.TAG_NAME, "input").send_keys("Issue Created")
        statusColourSelect = driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']")
        statusColourSelect.click()
        statusColourEnter = driver.find_element(By.XPATH, "//input[@class='sp-input']")
        statusColourEnter.clear()
        statusColourEnter.send_keys("#47963f")
        r = Robot()
        r.keyPress(KeyEvent.VK_ESCAPE)
        firstElement = driver.find_element(By.XPATH, "//a[@id='first-link']")
        firstElement.click()
        secondElement = driver.find_element(By.XPATH, "//a[@id='second-link']")
        secondElement.click()
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Status when a new ticket is created in HappyFox")
        addCreate = driver.find_element(By.XPATH, "//button[@class ='hf-entity-footer_primary hf-primary-action ember-view']")
        addCreate.click()
        time.sleep(3)
        moveTo = driver.find_element(By.XPATH, "//td[@class ='lt-cell align-center hf-mod-no-padding ember-view']")
        action.move_to_element(moveTo).perform()
        moveTo.click()
        time.sleep(9)
        issue = driver.find_element(By.XPATH, "//div[contains(text(),'Issue Created')]")
        action.move_to_element(issue).perform()
        make = driver.find_element(By.LINK_TEXT, "Make Default")
        make.click()
        driver.find_element(By.LINK_TEXT, "Priorities").click()
        driver.find_element(By.XPATH, "//header/button[1]").click()
        driver.find_element(By.TAG_NAME, "input").send_keys("Assistance required")
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Priority of the newly created tickets")
        button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']")
        button.click()
        time.sleep(9)
        tickets2 = driver.find_element(By.ID, "ember29")
        action.move_to_element(tickets2).perform()
        priorities2 = driver.find_element(By.LINK_TEXT, "Priorities")
        priorities2.click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[9]/td[2]").click()
        driver.find_element(By.LINK_TEXT, "Delete").click()
        delete = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']")
        delete.click()
        time.sleep(9)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/header[1]/div[2]/nav[1]/div[7]/div[1]/div[1]").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

class PagesforAutomationAssignment:

    def main(self):
        driver = webdriver.Chrome()
        driver.get("https://www.happyfox.com")

        loginPage = LoginPage(driver)
        loginPage.login("username", "password")

        homePage = HomePage(driver)
        homePage.verifyHomePage()

        driver.quit()

class BasePage:

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()

    def forgotPassword(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()

class HomePage(BasePage):

    def verifyHomePage(self):
        if self.driver.current_url != "https://www.happyfox.com/home":
            raise Exception("Not on the home page")

    def navigateToProfile(self):
        self.driver.find_element(By.ID, "profileLink").click()

class TablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.rowLocator = By.XPATH("//table[@id='dataTable']/tbody/tr")

    def retrieveRowTexts(self):
        rows = self.driver.find_elements(self.rowLocator)

        for i in range(len(rows)):
            row = rows[i]
            rowText = row.text
            print("Row " + str(i) + " Text: " + rowText)
