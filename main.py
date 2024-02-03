from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid
from src.lib.managedb import ManageDb
from pydantic import BaseModel

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
    return md.read_contacts()

@app.post("/")
def post():
    return {"message":"I am post"}

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    contacts = md.read_contacts()
    for contact in contacts:
        if contact["id"] ==id_contact:
            return contact
    raise HTTPException(status_code=404, detail="contact not found")

@app.post("/api/contacts")
def add_contact(new_contact:ContactModel):
    contacts = md.read_contacts()
    new_contact = new_contact.model_dump()

    contacts.append(new_contact)
    md.write_contacts(contacts)

    return{
        "success": True,
        "message": "Added new contact"
    }

@app.put("/api/contacts/{idcontact}")
def update_contact(id_contact: str, new_contact:ContactModel):
    contacts = md.read_contacts()

    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.model_dump()

            md.write_contacts(contacts)
            return {
                "success":True,
                "message": "Updated Contact"
            }
    raise HTTPException(status_code=404, detail="Contact not Found")