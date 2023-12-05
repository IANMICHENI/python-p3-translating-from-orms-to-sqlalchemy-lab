from models import Dog

def create_table(base ,engine):
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    try:
        return session.query(Dog).filter_by(name=name).one()
    except NoResultFound:
        return None

def find_by_id(session, dog_id):
    try:
        return session.query(Dog).filter_by(id=dog_id).one()
    except NoResultFound:
        return None

def find_by_name_and_breed(session, name, breed):
    try:
        return session.query(Dog).filter_by(name=name, breed=breed).one()
    except NoResultFound:
        return None

def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()

# ... (remaining code)
