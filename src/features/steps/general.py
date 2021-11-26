from time import sleep

from behave import then


@then("Waiting for {waiting} second")
def step_waiting(context, waiting):
    sleep(waiting)
