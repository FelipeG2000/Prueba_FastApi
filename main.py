from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid
from src.lib.managedb import ManageDb
from pydantic import BaseModel
from src.router.get_contacts import get_contacts
from src.router.get_contact import get_contact
from src.router.post_contact import post_contacts
from src.router.put_contact import put_contact
from src.router.delete_contact import delete_contact
from src.router.patch_contact import patch_contact

class ContactModel(BaseModel):
    id: str = str(uuid())
    name: str
    phone: str


app = FastAPI()
md = ManageDb()

@app.get("/")
def root():
    return {"message":"contacts messages"}

@app.get("/api/contacts")
def get_all_contacts():
    return get_contacts()

@app.post("/")
def post():
    return {"message":"I am post"}

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    return get_contact(id_contact)

@app.post("/api/contacts")
def add_contact(new_contact:ContactModel):
    return post_contacts(new_contact)

@app.put("/api/contacts/{idcontact}")
def update_contact(id_contact: str, new_contact:ContactModel):
    return put_contact(id_contact, new_contact)

@app.delete("/api/contacts/{id_contact}")
def remove_contact(id_contact:str):
    return delete_contact(id_contact)

@app.patch("/api/contacts/{id_contact}")
def updated_by_patch(id_contact:str,field_to_update:str,  new_value:str):
    md = ManageDb()
    contacts = md.read_contacts()

    for index, contact in enumerate(contacts):
        if contact.get("id") == id_contact:
            setattr(contacts[index], field_to_update, new_value)

            md.write_contacts(contacts)
            return {
                "success":True, 
                "message": "Updated Contact"
            }
    raise HTTPException(status_code=404, detail= "Contact not found")