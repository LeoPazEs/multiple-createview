class MultipleCreateView(CreateView): 
    """ Talvez alterar o father para BaseCreateView e um template response mixin"""

    def get_context_data(self, **kwargs): 
        for key, value in self.form_class.items(): 
            if key not in kwargs: 
                kwargs[key] = value
        return super().get_context_data(**kwargs)  
    
    def post(self,  request, *args, **kwargs):
        self.object = None 
        forms = {}
        for key, value in self.form_class.items(): 
            forms[key] = value(**self.get_form_kwargs()) 

        for form in forms.values(): 
            if not form.is_valid():
                return self.form_invalid(**forms) 
        return self.form_valid(**forms) 

    def form_valid(self, **forms):
        for i, validForm in enumerate(forms.values()) : 
            if i == 0:
                self.object = validForm.save()
            validForm.save()  
  
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self,**forms):
        return self.render_to_response(self.get_context_data(**forms))


