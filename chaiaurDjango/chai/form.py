from django import forms
from .models import ChaiVarity

class ChaiForm(forms.Form):
    chai_varity = forms.ModelChoiceField(
        queryset=ChaiVarity.objects.all(),
        label='Choose a Chai'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['chai_varity'].widget.attrs.update({
            'class': (
                'w-full px-4 py-2 bg-white text-gray-800 border border-amber-200 '
                'rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-amber-400 '
                'transition duration-300'
            )
        })
