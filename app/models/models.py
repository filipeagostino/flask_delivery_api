from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class DelivererModel(db.Model):
    __tablename__ = 'deliverer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    phone = db.Column(db.String(14), nullable=False)