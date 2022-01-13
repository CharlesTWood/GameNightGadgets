from website import db

def write_to_db(item):
    db.session.add(item)
    db.session.commit()