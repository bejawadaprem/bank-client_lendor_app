from ._anvil_designer import Lender_reg_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_1(Lender_reg_form_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    #name = self.text_box_1.text
    #gender = self.drop_down_1_copy_1
    #city = self.text_box_2.text
    #user_id = self.user_id
    
    #if not name or not city or not gender:
      #Notification("Please fill all the fields").show()
   #else:
      #nvil.server.call('add_lendor_frist_form',name,gender,city,user_id)
      
    open_form('lendor_registration_form.Lender_reg_form_2')
    """This method is called when the button is clicked"""
  
