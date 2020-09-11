import datetime as dt

from django.db import models

from agents.models import Agent

ACTION_TYPE_CHOICES = [
    ("schedreboot", "Scheduled Reboot"),
    ("taskaction", "Scheduled Task Action"),
]

# taskaction details format
# {
#   "action": "taskcreate" | "taskdelete" | "tasktoggle",
#   "value": "Enable" | "Disable" # only needed for task toggle,
#   "task_id": 1
# }

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("completed", "Completed"),
]


class PendingAction(models.Model):

    agent = models.ForeignKey(
        Agent,
        related_name="pendingactions",
        on_delete=models.CASCADE,
    )
    entry_time = models.DateTimeField(auto_now_add=True)
    action_type = models.CharField(
        max_length=255, choices=ACTION_TYPE_CHOICES, null=True, blank=True
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default="pending",
    )
    celery_id = models.CharField(null=True, blank=True, max_length=255)
    details = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.agent.hostname} - {self.action_type}"

    @property
    def due(self):
        if self.action_type == "schedreboot":
            obj = dt.datetime.strptime(self.details["time"], "%Y-%m-%d %H:%M:%S")
            return dt.datetime.strftime(obj, "%B %d, %Y at %I:%M %p")

    @property
    def description(self):
        if self.action_type == "schedreboot":
            return "Device pending reboot"

        elif self.action_type == "taskaction":
            if self.details.action == "taskdelete":
                return "Device pending task deletion"
            elif self.details.action == "taskcreate":
                return "Device pending task creation"
            elif self.details.action == "tasktoggle":
                return f"Device pending task {self.details.value}"
