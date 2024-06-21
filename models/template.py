from utils.db import db


class Template(db.Model):
    __tablename__ = 'template'

    template_id = db.Column(db.Integer, primary_key=True)
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
    
    def __init__(self, template_id, min, max):
        self.template_id_id = template_id
        self.min = min
        self.max = max
