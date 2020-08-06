from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from consultant.models import ( User,
                                PersonalDetails,
                                OfficialDetails,
                                ProjectDetails,
                                TrainingDetails,
                                FinancialDetails,
                                InvoicingDetails,
                                BenchDetails,
                                ProspectDetails,
                                )


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats=('%m/%d/%Y', )


class PersonalDetailsForm(forms.ModelForm):

    class Meta:
        model = PersonalDetails
        exclude = ('employee',)
        widgets = {
            'date_of_birth': DateInput(),
            'anniversary_date': DateInput(),
            'gc_priority_date': DateInput(),
            'zip_code': forms.TextInput(attrs={'placeholder':'XXXXX or XXXXX-XXXX'})
            }

    def clean(self):
        cleaned_data = super().clean()
        personal_email = cleaned_data.get("personal_email")
        marketing_email = cleaned_data.get("marketing_email")

        if personal_email == marketing_email:
            self.add_error("marketing_email","Should be different than Personal Email")


class OfficialDetailsForm(forms.ModelForm):

    class Meta:
        model = OfficialDetails
        exclude = ('employee',)
        widgets = {
            'date_of_joining': DateInput(),
            'date_of_termination': DateInput(),
            'ssn': forms.TextInput(attrs={'placeholder':'XXX-XX-XXXX'})
            }

    def clean_ssn(self):
        ssn = self.cleaned_data.get('ssn')
        mask = ssn.replace(ssn[0:7],'XXXXXXX')
        return mask

    def clean_official_phone_number(self):
        phone = self.cleaned_data.get('official_phone_number')
        res = str(phone)
        ext = res[-3:]
        first = res[:3]
        last = res[3:7]
        return ("({}) {}-{}".format(ext,first,last))



class ProjectDetailsForm(forms.ModelForm):

    class Meta:
        model = ProjectDetails
        exclude = ('employee',)
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            }


class TrainingDetailsForm(forms.ModelForm):

    class Meta:
        model = TrainingDetails
        exclude = ('employee',)
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'availability_date': DateInput(),
            }


class FinancialDetailsForm(forms.ModelForm):

    total_expense = forms.DecimalField(required=False, disabled=True)
    margin = forms.DecimalField(required=False, disabled=True)
    recruiter_margin = forms.DecimalField(required=False, disabled=True)

    class Meta:
        model = FinancialDetails
        exclude = ('employee',)

    def clean_total_expense(self):
        monthly_pay_rate = self.cleaned_data.get("monthly_pay_rate")
        perDm = self.cleaned_data.get("perDm")
        federal_tax = self.cleaned_data.get("federal_tax")
        state_tax = self.cleaned_data.get("state_tax")
        extra_expense = self.cleaned_data.get("extra_expense")
        immigration_cost = self.cleaned_data.get("immigration_cost")
        insurance = self.cleaned_data.get("insurance")
        four_o_one_k = self.cleaned_data.get("four_o_one_k")
        total_expense = self.cleaned_data.get("total_expense")
        total = sum([monthly_pay_rate,perDm,federal_tax,state_tax,extra_expense,immigration_cost,insurance,four_o_one_k])
        return total

    def clean_margin(self):
        monthly_bill_rate = self.cleaned_data.get("monthly_bill_rate")
        total_expense = self.cleaned_data.get("total_expense")
        margin = self.cleaned_data.get("margin")
        diff = (monthly_bill_rate - total_expense)
        return diff

    def clean_recruiter_margin(self):
        margin = self.cleaned_data.get("margin")
        recruiter_margin = self.cleaned_data.get("recruiter_margin")
        per = ((margin * 10)/100)
        return per


class InvoicingDetailsForm(forms.ModelForm):

    class Meta:
        model = InvoicingDetails
        exclude = ('employee',)


class BenchDetailsForm(forms.ModelForm):

    class Meta:
        model = BenchDetails
        exclude = ('employee',)
        widgets = {
            'availability_date': DateInput(),
            }


class ProspectDetailsForm(forms.ModelForm):

    class Meta:
        model = ProspectDetails
        exclude = ('employee',)
        widgets = {
            'availability_date': DateInput(),
            }
