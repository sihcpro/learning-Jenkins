import os


def after_scenario(context, scenario):
    if "save_report" in scenario.tags:
        # print("Deleting report file")
        os.remove(context.report_path)
