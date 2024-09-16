from .base import db, BaseModel
from datetime import date

class VMShelving(BaseModel):
    __tablename__ = 'vm_shelving'

    vm_id = db.Column(db.String(255), nullable=False, unique=True)
    vm_name = db.Column(db.String(255), nullable=False)
    unique_id = db.Column(db.String(255), nullable=False)
    owner_email = db.Column(db.String(255), nullable=False)
    auto_shelve_date = db.Column(db.Date, nullable=True)
    ticket_id = db.Column(db.String(255), nullable=True)
    deferred = db.Column(db.Boolean, default=False, nullable=False)
    canceled = db.Column(db.Boolean, default=False, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    error = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<VMShelving {self.vm_name} for User {self.user_id}>"
