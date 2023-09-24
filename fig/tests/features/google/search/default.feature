Feature: Google Search Default Results

    As a software engineer,
    I want to find information online,
    So I can improve myself.
    
    Scenario: Searching should return related results
        Given I am on the home page
        When I search Selenium
        Then I should see Selenium results