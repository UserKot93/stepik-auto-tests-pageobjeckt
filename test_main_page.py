from .pages.main_page import MainPage
from .pages.loginpage import LoginPage
from .pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                      # открываем страницу
	page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
	
def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()
	
def test_guest_should_see_URL(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_login_url()
	
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket_page()
	page.should_be_basket_empty()
	page.should_be_basket_empty_message()
