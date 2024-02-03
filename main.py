from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid
from src.lib.managedb import ManageDb
from pydantic import BaseModel
from src.router.get_contacts import get_contacts
from src.router.get_contact import get_contact
from src.router.post_contact import post_contacts
from src.router.put_contact import put_contact
from src.router.delete_contact import delete_contact

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