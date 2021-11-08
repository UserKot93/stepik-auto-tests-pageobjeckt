from .base_page import BasePage
import time

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert "login" in self.browser.current_url, "'login' not in current url"
        

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "LOGIN FORM IS NOT CORRECT"
        

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.FORM_LINK), "REGISTER FORM IS NOT CORRECT"
		
	def register_new_user(self):
		email = str(time.time()) + '@fakemail.org'
		password = 'myStrongPassword№121'
		self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
		self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
		self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD).send_keys(password)
		self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
