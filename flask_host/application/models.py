from application import db

class Sequences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.String(128), unique=True, nullable=False)
    submitted = db.Column(db.Integer(), nullable=False)


    def __repf__(self):
        return "".join([
                "sequence: ", self.sequence,
                "submitted: ", self.submitted
            ])
