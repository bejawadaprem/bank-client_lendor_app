from ._anvil_designer import Lender_reg_form_6Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_6(Lender_reg_form_6Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    address_type = self.drop_down_1.selected_value
    house_no = self.text_box_1.text
    building_name = self.text_box_2.text
    street = self.text_box_3.text
    user_id = self.userId
    if not address_type or not house_no or not building_name or not street:
      Notification("Please all the fields")
    else:
     anvil.server.call('add_lendor_six_form',address_type,house_no,building_name,street,user_id)
     open_form('lendor_registration_form.Lender_reg_form_7',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_5',user_id=user_id)
    """This method is called when the button is clicked"""
    
