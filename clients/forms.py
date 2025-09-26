from django.contrib.auth.forms import UserCreationForm
from .models import Client


class ClientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Client
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


