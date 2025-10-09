from django import forms
from django.forms import Textarea
from django.core.exceptions import ValidationError

from .models import Product, Category

EXCLUDE_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]

    def clean(self):
        cleaned_data = super().clean()
        name, description = cleaned_data.get("name"), cleaned_data.get("description")

        if any(word.lower() in name.lower() for word in EXCLUDE_WORDS):
            self.add_error("name", "В имени присутствует недопустимое слово")
        if any(word.lower() in description.lower() for word in EXCLUDE_WORDS):
            self.add_error("description", "В описании присутствует недопустимое слово")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть меньше нуля")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            if image.size > 5 * 1024 * 1024:  # 5 МБ
                raise forms.ValidationError("Файл не должен превышать 5 MB.")
            if not (image.name.endswith(".jpg") or image.name.endswith(".jpeg") or image.name.endswith(".png")):
                raise forms.ValidationError("Допустимые форматы: JPEG, PNG.")
        return image

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["category"].widget.attrs.update({"class": "form-select"})


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    message = forms.CharField(widget=Textarea)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get("name")
    #     phone = cleaned_data.get("phone")
    #     message = cleaned_data.get("message")
