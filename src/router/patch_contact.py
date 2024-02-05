from src.lib.managedb import ManageDb
from fastapi import HTTPException

def patch_contact(id_contact:str, new_contact):
    md = ManageDb()
    contacts = md.read_contacts()

    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.dict()

            md.write_contacts(contacts)
            return {
                "success":True, 
                "message": "Updated Contact"
            }
        raise HTTPException(status_code=404, detail= "Contact not found")