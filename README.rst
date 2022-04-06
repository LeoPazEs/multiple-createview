==================
MultipleCreateView
================== 
View to use various unrelated or related forms of diferent objects. 
Some mixins don't work in with this view. 

Usage: 
    class ContactFormView(FormView):
        template_name = 'contact.html'
        form_class = {'form_contact' : ContactForm, 'form_client': ClientForm }
        success_url = '/thanks/'