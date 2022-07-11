from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import allure
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def createScreenshot(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def click_button(self, how, what):
        button_create = self.browser.find_element(how, what)
        button_create.click()

    def is_not_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def fill_login_form(self):
        login_form = self.browser.switch_to.alert
        login_form.send_keys("admin")
        login_form.send_keys("admin")
        login_form.accept()
        time.sleep(10)

    def check_expected_test(self,how,what,expected_text):
        actual_text = self.browser.find_element(how, what).text
        assert actual_text == expected_text,f"{actual_text} != {expected_text}"

    def choose_checkbox(self, how, what):
        checkbox = self.browser.find_element(how, what)
        checkbox.is_selected()

    def click_context_menu(self, how, what):
        right_click = ActionChains(self.browser)
        context_menu = self.browser.find_element(how, what)
        right_click.context_click(context_menu).perform()


    def choose_dropdown(self, how, what, text):
        drop_down = Select(self.browser.find_element(how, what))
        drop_down.select_by_visible_text(text)
        # selectByIndex

    def refresh_page(self, how, what):
        #        self.is_element_present(how, what)
        tries = 0
        self.browser.refresh()
        while self.is_not_element_present(how, what):
            tries += 1
            self.browser.refresh()
        print(tries)

    def drag_and_drop(self, how, what, how1, what1):
        element = self.browser.find_element(how, what)
        destination = self.browser.find_element(how1, what1)
        action = ActionChains(self.browser)
        drag = action.click_and_hold(element).move_to_element(destination).release(destination)
        drag.perform()

    def wait_text_to_be_present(self, how, what):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((how, what)))

    def wait_element_to_be_active(self, how, what):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((how, what)))

    def fill_input(self, how, what, key):
        input = self.browser.find_element(how, what)
        input.send_keys(key)

    def wait_visible_element_is_located(self, how, what):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how, what)))

    def go_to_outside(self):
        actions = ActionChains(self.browser)
        actions.move_by_offset(600, -1).build().perform()

    def file_upload(self, how, what):
        element = self.browser.find_element(how, what)
        current_dir = os.path.abspath(
            os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'step.xlsx')  # добавляем к этому пути имя файла
        element.send_keys(file_path)

    def scroll(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def horizontal_slider(self, how, what):
        slider = self.browser.find_element(how, what)
        action = ActionChains(self.browser)
        action.click_and_hold(slider).move_by_offset(60, 0).release().perform()


    def element_hover(self, how, what):
        element = self.browser.find_element(how, what)
        action = ActionChains(self.browser)
        action.click_and_hold(element).move_to_element(element).perform()

    def key_down(self):
        action = ActionChains(self.browser)
        action.key_down(Keys.ENTER).perform()


    def simple_alert(self):
        alertfield = self.browser.switch_to.alert
        alertfield.accept()

    def alert_promt(self):
        alertfield = self.browser.switch_to.alert
        alertfield.send_keys("admin")
        alertfield.accept()
