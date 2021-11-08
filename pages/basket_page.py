from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .loginpage import LoginPage
import time
from .locators import BasePageLocators

class BasketPage(BasePage):
	def should_be_basket_empty(self):
		assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET_PAGE), 'Product in basket'
	def should_be_basket_empty_message(self):
		assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_PAGE), 'Product in basket'
