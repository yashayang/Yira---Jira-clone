from app.models import db, Project, environment, SCHEMA
from datetime import datetime

def seed_projects():
  project1 = Project(
    name='RD Sprint 23',
    owner_id=1,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  db.session.add(project1)
  db.session.commit()

def undo_projects():
    db.session.execute('TRUNCATE projects RESTART IDENTITY CASCADE;')
    db.session.commit()
