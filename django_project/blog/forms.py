from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Item, Post, XYZ_TestData


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'content']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'price','content','image','category','author']

class DateRangeForm(forms.Form):
  def __init__(self, *args, **kwargs):
    initial_start_date = kwargs.pop('initial_start_date')
    initial_end_date = kwargs.pop('initial_end_date')
    required_val = kwargs.pop('required')

    super(DateRangeForm,self).__init__(*args,**kwargs)
    self.fields['start_date'].initial = initial_start_date
    self.fields['start_date'].required = required_val
    self.fields['end_date'].initial = initial_end_date
    self.fields['end_date'].required = required_val

  start_date = forms.DateField()
  end_date = forms.DateField()

  def table_search(request):
      initial_start = "2015/2"
      initial_end = "2015/222"
      message = {'last_url': 'table_search'}

      if request.method == "POST":
          daterange_form = DateRangeForm(request.POST, required=True, initial_start_date=initial_start,
                                         initial_end_date=initial_end)

      else:
          daterange_form = DateRangeForm(required=True, initial_start_date=initial_start, initial_end_date=initial_end)
          search_dict.update({'daterange_form': daterange_form})

      return render(request, 'InterfaceApp/table_search.html', search_dict)



class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)

class XYZ_DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"
    #input_type = "datetime"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

class XYZ_TestDataForm(forms.ModelForm):
    class Meta:
        model =XYZ_TestData
        fields = '__all__'
        widgets = {
            'my_date':XYZ_DateInput(format=["%Y-%m-%d"],),
            # 'my_date': XYZ_DateInput(format=["%d-%m-%Y"], ),
            'my_date_time': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),
            'my_des': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),

        }


"""
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image")
"""
"""
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []
"""