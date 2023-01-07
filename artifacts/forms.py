from django import forms
from artifacts.models import Artifact


class ArtifactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if "user" in kwargs:
            self.user = kwargs.pop("user")
        super(ArtifactForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ArtifactForm, self).save(commit=False)
        instance.created_by = self.user
        instance.modified_by = self.user
        instance.name = instance.uploaded_file.name
        instance.save()
        return instance

    class Meta:
        model = Artifact
        fields = ('uploaded_file', )
