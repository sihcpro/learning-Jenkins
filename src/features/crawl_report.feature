Feature: Download StackOverflow report

    I want to download a report from StackOverflow
    @download_report
    Scenario Outline: I want to download a report from StackOverflow with custom page size
        Given I need a report with <num_of_page> pages and page size is <page_size>
        Then I have a report which has <num_of_line> lines
        Examples:
            | num_of_page | page_size | num_of_line |
            | 3           | 15        | 45          |
            | 5           | 20        | 100         |

    @download_report
    @save_report
    Scenario: I want to save a report from StackOverflow
        Given I need a report with 3 pages and page size is 15
        Then I have a report which has 45 lines
        And I save the report at ./output/scenario_crawl_report.csv
