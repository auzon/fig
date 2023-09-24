import logging
import pytest
from selenium import webdriver
from fig.pages.google.home_page import HomePage
from fig.pages.google.search_page import SearchPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def search_page(driver):
    return SearchPage(driver)


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    logging.error(f"{step}")


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    logging.info(f"{step}")