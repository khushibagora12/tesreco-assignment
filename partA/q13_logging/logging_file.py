## q13 logging
from reportGeneration import report_generation

admin_report = report_generation("admin")

admin_report.login()
admin_report.start_report_generation()
admin_report.report_generation_completed()
