from src.lib.managedb import ManageDb
from fastapi import HTTPException

def put_contact(id_contact:str, new_contact):
    md = ManageDb()
    contacts = md.read_contacts()

    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.model_dump()
            if new_contact.name == "":
                contacts[index]["name"] = contact["name"]
            if new_contact.phone == "":
                contacts[index]["phone"] = contact["phone"]

            md.write_contacts(contacts)
            return {
                "success":True,
                "message": "Updated Contact"
            }
    raise HTTPException(status_code=404, detail="Contact not Found")