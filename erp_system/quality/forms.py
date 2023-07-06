from django import forms
from .models import QualityCheck

class QualityCheckForm(forms.ModelForm):
    class Meta:
        model = QualityCheck
        fields = ['product', 'quality_score', 'checked_by', 'check_date']

    def clean_quality_score(self):
        quality_score = self.cleaned_data.get('quality_score')
        if quality_score < 0 or quality_score > 100:
            raise forms.ValidationError('Quality score must be between 0 and 100.')
        return quality_score