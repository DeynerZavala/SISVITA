from utils.db import db


class Test_Templates(db.Model):
    __tablename__ = 'test_template'

    template_id = db.Column(db.Integer, primary_key=True)
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
    estado = db.Column(db.String(255))
    test_id = db.Column(db.Integer, db.ForeignKey('test.test_id'))
    ans_sem_id = db.Column(db.Integer)
    
    def __init__(self, template_id, min, max):
        self.template_id_id = template_id
        self.min = min
        self.max = max

