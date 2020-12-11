from django.forms import DateInput

class BootstrapDateTimePickerInput(DateInput):
    template_name = 'contact/bootstrap_datetimepicker.html'

    
class FengyuanChenDatePickerInput(DateInput):
    template_name = 'contact/fengyuanchen_datepicker.html'