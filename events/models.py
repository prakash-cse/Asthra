from django.db import models

# Choices for event categories
EVENT_CATEGORIES = [
    ('TECHNICAL', 'Technical Event'),
    ('NON_TECHNICAL', 'Non-Technical Event'),
]

class Event(models.Model):
    category = models.CharField(
        max_length=20,
        choices=EVENT_CATEGORIES,
        default='TECHNICAL',
    )
    name = models.CharField(max_length=100)  # e.g., "Paper Presentation", "Fireless Cooking"
    description = models.TextField(null=True,blank=True)  # Brief description of the event
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Rule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rules')
    rule_text = models.CharField(max_length=255)  # Individual rule (e.g., "Maximum of two members")

    def __str__(self):
        return f"Rule for {self.event.name}: {self.rule_text}"