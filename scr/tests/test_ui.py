import pytest
import requests
from scr.pages.basePage import BasePage
from scr.pages.locators import Locators
import time
import allure


@allure.testcase('Add and remove element')
@allure.description('Check add and remove element')
def test_add_and_remove_element(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/add_remove_elements/'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Check add button"):
        with allure.step("Click add button"):
            page.click_button(*Locators.button_add_element)

        with allure.step("Check button appeared"):
            page.is_element_present(*Locators.button_delete_element)

    with allure.step("Check delete button"):
        with allure.step("Click delete button"):
            page.click_button(*Locators.button_delete_element)

        with allure.step("Check delete button"):
            page.is_not_element_present(*Locators.button_add_element)


@allure.testcase('Basic Auth')
@allure.description('Check basic auth')
def test_basic_auth(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/basic_auth'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Fill login form"):
        page.fill_login_form()

    with allure.step("Check auth passed"):
        expected_text = "Congratulation"
        actual_text = browser.find_element(*Locators.text_from_basic_auth).text
        assert expected_text in actual_text


@allure.testcase('Broken Images')
@allure.description('Find broken images')
@pytest.mark.parametrize('image', ["asdf.jpg", "hjkl.jpg", "img/avatar-blank.jpg"])
def test_broken_images(browser, image):
    with allure.step("Check links"):
        link = f'http://the-internet.herokuapp.com/{image}'
        result = requests.get(link)

    with allure.step("Check image is right"):
        assert 200 == result.status_code


@allure.testcase('Checkboxes')
@allure.description('Check checkboxes')
def test_checkboxes(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/checkboxes'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Choose checkbox"):
        page.choose_checkbox(*Locators.checkbox)

    with allure.step("Check checkbox is checked"):
        element = browser.find_element(*Locators.checkbox)
        condition_checkbox = element.get_attribute('checked')
        assert condition_checkbox == 'true', f"Checkbox is not checked"


@allure.testcase('Context Menu')
@allure.description('Check context menu')
def test_context_menu(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/context_menu'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Click context menu"):
        page.click_context_menu(*Locators.context_menu)

    with allure.step("Check context menu appeared"):
        alert = browser.switch_to.alert
        assert "You selected a context menu" in alert.text, f'{alert.text} is wrong'
        alert.accept()


@allure.testcase('Dropdown')
@allure.description('Check dropdown')
def test_dropdown(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/dropdown'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Choose dropdown option 1"):
        page.choose_dropdown(*Locators.dropdown, "Option 1")

    with allure.step("Check choosen dropdown option 1"):
        element = browser.find_element(*Locators.dropdown_option_1)
        condition_checkbox = element.get_attribute('selected')
        assert condition_checkbox == 'true', f"Option 1 is not selected"


@allure.testcase('Disappearing Elements')
@allure.description('Check disappearing element')
def test_disappearing_elements(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/disappearing_elements'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Check count of elements"):
        count_before_refresh = browser.find_elements(*Locators.disappearing_elements)

    with allure.step("Refresh page"):
        page.refresh_page(*Locators.gallery)

    with allure.step("Check count of elements after refresh"):
        count_after_refresh = browser.find_elements(*Locators.disappearing_elements)
        assert count_before_refresh != count_after_refresh, "Page is not refresh"

@allure.testcase('Drag and Drop')
@allure.description('Check drag and drop')
def test_drag_and_drop(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/drag_and_drop'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Check first header"):
        header_before = browser.execute_script(f"return arguments[0].textContent", *Locators.first_block)

    with allure.step("Check drag and drop"):
        page.drag_and_drop(*Locators.element, *Locators.destination)

    with allure.step("Check header after drag and drop"):
        header_after = browser.execute_script(f"return arguments[0].textContent", *Locators.first_block)
        header_before != header_after, "Drag and Drop is not work"


@allure.testcase('Dynamic Controls')
def test_dinamic_control(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/dynamic_controls'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Сheck checkbox"):
        page.choose_checkbox(*Locators.checkbox_dinamic)
        page.click_button(*Locators.button_remove)

    with allure.step("Сheck text appeared after choose checkbox"):
        page.wait_text_to_be_present(*Locators.text_luck)
        page.is_element_present(*Locators.button_add)

    with allure.step("Click button enable"):
        page.click_button(*Locators.button_enable)

    with allure.step("Check that input is enable after clicking button"):
        page.wait_element_to_be_active(*Locators.input_dis)
        page.fill_input(*Locators.input_dis, "привет")


@allure.testcase('Dynamic Loading')
def test_dynamic_loading(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/dynamic_loading/1'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Click button start"):
        page.click_button(*Locators.button_start)

    with allure.step("Check text is appeared"):
        page.wait_visible_element_is_located(*Locators.text_hello)


@allure.testcase('Entry Ad')
def test_enrtry_add(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/entry_ad'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Check ad is appeared"):
        page.is_element_present(*Locators.modal_window)


@allure.testcase('Exit Intent')
def test_exit_intent(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/exit_intent'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Click outside"):
        page.go_to_outside()

    with allure.step("Modal window is appeared"):
        page.is_element_present(*Locators.modal_window)


@allure.testcase('File Upload')
def test_file_upload(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/upload'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Upload file"):
        page.file_upload(*Locators.file_upload)
        page.click_button(*Locators.button_upload)

    with allure.step("Check that file is uploaded"):
        page.is_element_present(*Locators.message_file_upload)


@allure.testcase('Floating Menu')
def test_floating_menu(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/floating_menu'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Scroll page"):
        page.scroll()

    with allure.step("Check that element is appeared"):
        page.wait_visible_element_is_located(*Locators.part_menu)


@allure.testcase('Horizontal Slider')
def test_horizontal_slider(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/horizontal_slider'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Slide to 5"):
        page.horizontal_slider(*Locators.slider)

    with allure.step("Check slider"):
        number_slider = browser.find_element(*Locators.number_slider)
        number = '5'
        assert number in number_slider.text


@allure.testcase('Hovers')
def test_hover(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/hovers'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Hower to element"):
        page.element_hover(*Locators.number_slider)

    with allure.step("Check that element is appeared after hover"):
        page.wait_visible_element_is_located(*Locators.image_one)


@allure.testcase('Key Presses')
def test_key_presses(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/key_presses'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Press key ENTER"):
        page.key_down()

    with allure.step("Check that ENTER is pressed"):
        element = browser.find_element(*Locators.key_main)
        button = 'ENTER'
        assert button in element.text


@allure.testcase('JavaScript Alerts')
def test_alert(browser):
    with allure.step("Open page"):
        link = 'http://the-internet.herokuapp.com/javascript_alerts'
        page = BasePage(browser, link)
        page.open()

    with allure.step("Click JS Alert"):
        page.click_button(*Locators.alert_js)
        page.simple_alert()

    with allure.step("Check that JS Alert is clicked"):
        message_alert = browser.execute_script(f"return arguments[0].textContent", *Locators.alert_message)
        assert 'You successfully clicked an alert' in message_alert, "Alert is not clicked"

    with allure.step("Click JS Confirm"):
        page.click_button(*Locators.alert_confirm)
        page.simple_alert()

    with allure.step("Check that JS Confirm is clicked"):
        message_alert = browser.execute_script(f"return arguments[0].textContent", *Locators.alert_message)
        assert 'You clicked: Ok' in message_alert, "Alert is not clicked"

    with allure.step("Click JS Prompt"):
        page.click_button(*Locators.alert_prompt)
        page.alert_promt()

    with allure.step("Check that JS Prompt is clicked"):
        message_alert = browser.execute_script(f"return arguments[0].textContent", *Locators.alert_message)
        assert 'You entered: admin' in message_alert, "Alert is not clicked"
