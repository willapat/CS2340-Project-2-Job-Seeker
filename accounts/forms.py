from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import inlineformset_factory

from .models import Education, Link, Profile, WorkExperience


class BootstrapMixin:
    """Adds Bootstrap classes to every field."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                css = "form-check-input"
            elif isinstance(widget, forms.Select):  # includes SelectMultiple
                css = "form-select"
            else:
                css = "form-control"
            widget.attrs["class"] = f"{widget.attrs.get('class', '')} {css}".strip()


class SignUpForm(BootstrapMixin, UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")


class LoginForm(BootstrapMixin, AuthenticationForm):
    pass


class ProfileForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["headline", "skills"]
        widgets = {
            "headline": forms.TextInput(
                attrs={"placeholder": "e.g. Recent CS grad seeking backend roles"}
            ),
        }


class EducationForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Education
        fields = ["school", "degree", "start_year", "end_year"]

    def clean(self):
        data = super().clean()
        start, end = data.get("start_year"), data.get("end_year")
        if start and end and end < start:
            raise forms.ValidationError("End year can't be before start year.")
        return data


class ExperienceForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ["company", "title", "start_date", "end_date", "description"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "end_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "description": forms.Textarea(attrs={"rows": 3}),
        }

    def clean(self):
        data = super().clean()
        start, end = data.get("start_date"), data.get("end_date")
        if start and end and end < start:
            raise forms.ValidationError("End date can't be before start date.")
        return data


class LinkForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Link
        fields = ["label", "url"]
        widgets = {"label": forms.TextInput(attrs={"placeholder": "e.g. GitHub"})}


EducationFormSet = inlineformset_factory(
    Profile, Education, form=EducationForm, extra=2, can_delete=True
)
ExperienceFormSet = inlineformset_factory(
    Profile, WorkExperience, form=ExperienceForm, extra=2, can_delete=True
)
LinkFormSet = inlineformset_factory(
    Profile, Link, form=LinkForm, extra=2, can_delete=True
)