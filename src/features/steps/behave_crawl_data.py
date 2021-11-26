from os.path import isfile

from behave import given, then
from hamcrest import assert_that, has_length, is_
from report.stackoverflow import StackOverflowReport


@given("I need a report with {num_of_page:d} pages and page size is {page_size:d}")
def step_init_the_report(context, num_of_page, page_size):
    context.report = StackOverflowReport(numOfPage=num_of_page, pageSize=page_size)


@then("I have a report which has {num_of_line:d} lines")
def step_assert_report_line(context, num_of_line):
    list_question = context.report.getListQuestions()
    assert_that(
        list_question, has_length(num_of_line), f"report has wrong line numbers"
    )


@then("I save the report at {report_path}")
def step_save_report(context, report_path):
    context.report_path = context.report.saveAsCsv(report_path)
    assert_that(isfile(report_path), is_(True), "file is not exists")
