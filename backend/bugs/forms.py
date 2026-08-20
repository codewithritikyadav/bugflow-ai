from django import forms

from .models import Bug
from django.contrib.auth.models import User


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = [
            "title",
            "description",
            "priority",
            "status",
            "assigned_to",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter bug title",
                    "class": "form-input",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe the bug...",
                    "class": "form-input form-textarea",
                    "rows": 7,
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),

            "assigned_to": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),
        }

        labels = {
            "title": "Bug Title",
            "description": "Description",
            "priority": "Priority",
            "status": "Status",
            "assigned_to": "Assign Developer",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["assigned_to"].queryset = User.objects.all()
        self.fields["assigned_to"].required = False
        self.fields["assigned_to"].empty_label = "Unassigned"