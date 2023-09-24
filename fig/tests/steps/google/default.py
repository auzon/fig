from pytest_bdd import scenarios, given, when, then
from fig.pages.google.home_page import HomePage
from fig.pages.google.search_page import SearchPage


scenarios("../../features/google/search/default.feature")

@given("I am on the home page")
def open_google_home_page(home_page: "HomePage"):
    home_page.visit()


@when("I search Selenium")
def search(home_page: "HomePage"):
    home_page.search("Selenium")


@then("I should see Selenium results")
def check_results(search_page: "SearchPage"):
    assert search_page.calculate_relatedness_ratio("Selenium") >= 0.9, f"There are some unrelated info in {search_page.result_description_list}"