import pytest
import requests
from scr.pages.basePage import BasePage
from scr.pages.locators import Locators
import time
import allure


@allure.testcase('Add and remove element')
@allure.description('Check add and remove element')
def test_add_and_remove_element(browser):
    link = 'http://the-internet.herokuapp.com/add_remove_elements/'
    page = BasePage(browser, link)
    page.open()
    with allure.step("Check add button"):
        page.click_button(*Locators.button_add_element)
        page.is_element_present(*Locators.button_delete_element)
    with allure.step("Check delete button"):
        page.click_button(*Locators.button_delete_element)
        page.is_not_element_present(*Locators.button_add_element)


@allure.testcase('Basic Auth')
@allure.description('Check basic auth')
def test_basic_auth(browser):
    link = 'http://the-internet.herokuapp.com/basic_auth'
    page = BasePage(browser, link)
    page.open()
    with allure.step("Fill login form"):
        page.fill_login_form()


@allure.testcase('Broken Images')
@allure.description('Find broken images')
@pytest.mark.parametrize('image', ["asdf.jpg", "hjkl.jpg", "img/avatar-blank.jpg"])
def test_broken_images(browser, image):
    link = f'http://the-internet.herokuapp.com/{image}'
    result = requests.get(link)
    with allure.step("Check image is right"):
        assert 200 == result.status_code


@allure.testcase('Checkboxes')
@allure.description('Check checkboxes')
def test_checkboxes(browser):
    link = 'http://the-internet.herokuapp.com/checkboxes'
    page = BasePage(browser, link)
    page.open()
    with allure.step("Choose checkbox"):
        page.choose_checkbox(*Locators.checkbox)


@allure.testcase('Context Menu')
@allure.description('Check context menu')
def test_context_menu(browser):
    link = 'http://the-internet.herokuapp.com/context_menu'
    page = BasePage(browser, link)
    page.open()
    with allure.step("Click context menu"):
        page.click_context_menu(*Locators.context_menu)


@allure.testcase('Dropdown')
@allure.description('Check dropdown')
def test_dropdown(browser):
    link = 'http://the-internet.herokuapp.com/dropdown'
    page = BasePage(browser, link)
    page.open()
    with allure.step("Choose dropdown option 1"):
        page.choose_dropdown(*Locators.dropdown, "Option 1")


@allure.testcase('Disappearing Elements')
@allure.description('Check disappearing element')
def test_disappearing_elements(browser):
    link = 'http://the-internet.herokuapp.com/disappearing_elements'
    page = BasePage(browser, link)
    page.open()
    with allure.step("Refresh page"):
        page.refresh_page(*Locators.gallery)


@allure.testcase('Drag and Drop')
@allure.description('Check drag and drop')
def test_drag_and_drop(browser):
    link = 'http://the-internet.herokuapp.com/drag_and_drop'
    page = BasePage(browser, link)
    page.open()
    with allure.step("Check drag and drop"):
        page.drag_and_drop(*Locators.element, *Locators.destination)


@allure.testcase('Dynamic Controls')
def test_dinamic_control(browser):
    link = 'http://the-internet.herokuapp.com/dynamic_controls'
    page = BasePage(browser, link)
    page.open()
    page.choose_checkbox(*Locators.checkbox_dinamic)
    page.click_button(*Locators.button_remove)
    page.wait_text_to_be_present(*Locators.text_luck)
    page.is_element_present(*Locators.button_add)
    # text = "It's gone!"
    # assert text in page
    page.click_button(*Locators.button_enable)
    page.wait_element_to_be_active(*Locators.input_dis)
    page.fill_input(*Locators.input_dis, "привет")


@allure.testcase('Dynamic Loading')
def test_dynamic_loading(browser):
    link = 'http://the-internet.herokuapp.com/dynamic_loading/1'
    page = BasePage(browser, link)
    page.open()
    page.click_button(*Locators.button_start)
    page.wait_visible_element_is_located(*Locators.text_hello)


@allure.testcase('Entry Ad')
def test_enrtry_add(browser):
    link = 'http://the-internet.herokuapp.com/entry_ad'
    page = BasePage(browser, link)
    page.open()
    page.is_element_present(*Locators.modal_window)  


@allure.testcase('Exit Intent')
def test_exit_intent(browser):
    link = 'http://the-internet.herokuapp.com/exit_intent'
    page = BasePage(browser, link)
    page.open()
    page.go_to_outside()
    page.is_element_present(*Locators.modal_window)


@allure.testcase('File Upload')
def test_file_upload(browser):
    link = 'http://the-internet.herokuapp.com/upload'
    page = BasePage(browser, link)
    page.open()
    page.file_upload(*Locators.file_upload)
    page.click_button(*Locators.button_upload)
    page.is_element_present(*Locators.message_file_upload)


@allure.testcase('Floating Menu')
def test_floating_menu(browser):
    link = 'http://the-internet.herokuapp.com/floating_menu'
    page = BasePage(browser, link)
    page.open()
    page.scroll()
    # time.sleep(10)
    page.wait_visible_element_is_located(*Locators.part_menu)


@allure.testcase('Horizontal Slider')
def test_horizontal_slider(browser):
    link = 'http://the-internet.herokuapp.com/horizontal_slider'
    page = BasePage(browser, link)
    page.open()
    page.horizontal_slider(*Locators.slider, *Locators.number_slider)
    time.sleep(5)


@allure.testcase('Hovers')
def test_hover(browser):  # пофикcить локаторы
    link = 'http://the-internet.herokuapp.com/hovers'
    page = BasePage(browser, link)
    page.open()
    page.element_hover(*Locators.number_slider)
    page.wait_visible_element_is_located(*Locators.image_one)


@allure.testcase('Inputs')
def test_input(browser):
    link = 'http://the-internet.herokuapp.com/inputs'
    page = BasePage(browser, link)
    page.open()
    page.fill_input(*Locators.input_input, '5')


@allure.testcase('Key Presses')
def test_key_presses(browser):
    link = 'http://the-internet.herokuapp.com/key_presses'
    page = BasePage(browser, link)
    page.open()
    page.key_down(*Locators.key_main)


@allure.testcase('JavaScript Alerts')
def test_alert(browser):
    link = 'http://the-internet.herokuapp.com/javascript_alerts'
    page = BasePage(browser, link)
    page.open()
    page.click_button(*Locators.alert_js)
    page.simple_alert()
    page.click_button(*Locators.alert_confirm)
    page.simple_alert()
    page.click_button(*Locators.alert_prompt)
    page.alert_promt()
