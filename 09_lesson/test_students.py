import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models import Base, Student


@pytest.fixture(scope="session")
def engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture(scope="function")
def db_session(engine):
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def test_create_student(db_session: Session):
    student = Student(
        first_name="Иван",
        last_name="Петров",
        email="ivan@example.com",
    )
    db_session.add(student)
    db_session.flush()
    db_session.refresh(student)
    db_session.commit()

    assert student.id is not None
    assert student.is_deleted is False

    in_db = db_session.query(Student).filter_by(id=student.id).first()
    assert in_db is not None
    assert in_db.email == "ivan@example.com"
    assert in_db.is_deleted is False


def test_update_student(db_session: Session):
    student = Student(
        first_name="Анна",
        last_name="Иванова",
        email="anna@example.com",
    )
    db_session.add(student)
    db_session.flush()
    db_session.refresh(student)
    db_session.commit()

    student_id = student.id

    student.first_name = "Анна-обновлённая"
    db_session.flush()
    db_session.commit()

    updated = db_session.query(Student).filter_by(id=student_id).first()
    assert updated is not None
    assert updated.first_name == "Анна-обновлённая"
    assert updated.is_deleted is False


def test_soft_delete_student(db_session: Session):
    student = Student(
        first_name="Пётр",
        last_name="Смирнов",
        email="petr@example.com",
    )
    db_session.add(student)
    db_session.flush()
    db_session.refresh(student)
    db_session.commit()

    student_id = student.id

    student.soft_delete()
    db_session.flush()
    db_session.commit()

    in_db = db_session.query(Student).filter_by(id=student_id).first()
    assert in_db is not None
    assert in_db.is_deleted is True

    active = db_session.query(Student).filter(
        Student.id == student_id,
        Student.is_deleted.is_(False),
    ).first()
    assert active is None
