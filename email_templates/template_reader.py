class TemplateReader:
    def __init__(self):
        pass

    def select_info(self,options_name):
        try:
            email_file = open("email_templates/preventive_Template.html", "r")
            email_message = email_file.read()

            return email_message
        except Exception as e:
            print('The exception is '+str(e))
