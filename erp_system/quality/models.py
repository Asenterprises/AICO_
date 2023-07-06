```python
from django.db import models
from erp_system.users.models import User

class QualityCheck(models.Model):
    CHECK_CHOICES = (
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_result = models.CharField(max_length=4, choices=CHECK_CHOICES)
    check_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.check_result} - {self.check_date}'

class QualityIssue(models.Model):
    ISSUE_STATUS = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_status = models.CharField(max_length=6, choices=ISSUE_STATUS, default='open')
    issue_date = models.DateTimeField(auto_now_add=True)
    issue_description = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.issue_status} - {self.issue_date}'
```