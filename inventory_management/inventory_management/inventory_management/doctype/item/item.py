# Copyright (c) 2024, prerna and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class Item(Document):
    def after_insert(self):
        # Display a success message when an item is added
        frappe.msgprint(f"Item '{self.item_name}' has been added successfully!", alert=True)
