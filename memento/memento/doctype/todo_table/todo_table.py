# Copyright (c) 2026, Sagar Patil and contributors
# For license information, please see license.txt

from frappe.model.document import Document
from frappe.utils import now_datetime, get_datetime



class ToDoTable(Document):

    def before_insert(self):
        if not self.task_start_time:
            self.task_start_time = now_datetime()

    def validate(self):
        if self.task_start_time and self.task_end_time:

            start_on = get_datetime(self.task_start_time)
            end_on = get_datetime(self.task_end_time)

            duration = int((end_on - start_on).total_seconds())

            hours, remainder = divmod(duration, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.total_duration = (
                f"{hours} hours {minutes} minutes {seconds} seconds"
            )
        else:
            self.total_duration = ""