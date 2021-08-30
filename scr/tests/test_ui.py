import pytest
import requests
from scr.pages.basePage import BasePage
from scr.pages.locators import Locators
import time


def page_open(browser, link):
    page = BasePage(browser, link)
    page.open()


def test_add_delete_element(browser):
    link = 'http://the-internet.herokuapp.com/add_remove_elements/'
    page = BasePage(browser, link)
    page.open()
    page.click_button(*Locators.buttonAddElement)
    page.is_element_present(*Locators.buttonDeleteElement)
    page.click_button(*Locators.buttonDeleteElement)
    page.is_not_element_present(*Locators.buttonDeleteElement)


def test_basic_auth(browser):
    link = 'http://the-internet.herokuapp.com/basic_auth'
    page = BasePage(browser, link)
    page.open()
    page.fill_alert_field()


@pytest.mark.parametrize('image', ["asdf.jpg", "hjkl.jpg", "img/avatar-blank.jpg"])
def test_broken_images(browser, image):
    link = f'http://the-internet.herokuapp.com/{image}'
    result = requests.get(link)
    assert 200 == result.status_code


def test_checkboxes(browser):
    link = 'http://the-internet.herokuapp.com/checkboxes'
    page = BasePage(browser, link)
    page.open()
    page.choose_checkbox(*Locators.checkbox)


def test_context_menu(browser):
    link = 'http://the-internet.herokuapp.com/context_menu'
    page = BasePage(browser, link)
    page.open()
    page.click_context_menu(*Locators.contextmenu)


def test_dropdown(browser):
    link = 'http://the-internet.herokuapp.com/dropdown'
    page = BasePage(browser, link)
    page.open()
    page.choose_dropdown(*Locators.dropdown, "Option 1")


def test_disappearing_elements(browser):  # спорный кейс
    link = 'http://the-internet.herokuapp.com/disappearing_elements'
    page = BasePage(browser, link)
    page.open()
    page.refresh_page(*Locators.gallery)


def test_drag_and_drop(browser):
    link = 'http://the-internet.herokuapp.com/drag_and_drop'
    page = BasePage(browser, link)
    page.open()
    page.drag_and_drop(*Locators.element, *Locators.destination)


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


def test_dynamic_loading(browser):
    link = 'http://the-internet.herokuapp.com/dynamic_loading/1'
    page = BasePage(browser, link)
    page.open()
    page.click_button(*Locators.button_start)
    page.wait_visible_element_is_located(*Locators.text_hello)


def test_enrtry_add(browser):
    link = 'http://the-internet.herokuapp.com/entry_ad'
    page = BasePage(browser, link)
    page.open()
    page.is_element_present(*Locators.modal_window)  # разобраться


def test_exit_intent(browser):
    link = 'http://the-internet.herokuapp.com/exit_intent'
    page = BasePage(browser, link)
    page.open()
    page.go_to_outside()
    page.is_element_present(*Locators.modal_window)


def test_file_upload(browser):
    link = 'http://the-internet.herokuapp.com/upload'
    page = BasePage(browser, link)
    page.open()
    page.file_upload(*Locators.file_upload)
    page.click_button(*Locators.button_upload)
    page.is_element_present(*Locators.message_file_upload)


def test_floating_menu(browser):
    link = 'http://the-internet.herokuapp.com/floating_menu'
    page = BasePage(browser, link)
    page.open()
    page.scroll()
    # time.sleep(10)
    page.wait_visible_element_is_located(*Locators.part_menu)


def test_horizontal_slider(browser):
    link = 'http://the-internet.herokuapp.com/horizontal_slider'
    page = BasePage(browser, link)
    page.open()
    page.horizontal_slider(*Locators.slider, *Locators.number_slider)
    time.sleep(5)


def test_hover(browser):  # пофикить локаторы
    link = 'http://the-internet.herokuapp.com/hovers'
    page = BasePage(browser, link)
    page.open()
    page.element_hover(*Locators.number_slider)
    page.wait_visible_element_is_located(*Locators.image_one)


def test_input(browser):
    link = 'http://the-internet.herokuapp.com/inputs'
    page = BasePage(browser, link)
    page.open()
    page.fill_input(*Locators.input_input, '5')


def test_key_presses(browser):
    link = 'http://the-internet.herokuapp.com/key_presses'
    page = BasePage(browser, link)
    page.open()
    page.key_down(*Locators.key_main)


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