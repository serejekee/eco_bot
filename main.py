from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

app = FastAPI()
Base = declarative_base()

# SQLite БД
engine = create_engine("sqlite:///chat.db")
SessionLocal = sessionmaker(bind=engine)


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    text = Column(String)
    response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


class MessageIn(BaseModel):
    user_id: str
    text: str


class MessageOut(BaseModel):
    user_id: str
    text: str
    response: str
    timestamp: datetime


@app.post("/message", response_model=MessageOut)
def send_message(msg: MessageIn):
    db = SessionLocal()
    response_text = f"Вы сказали: {msg.text}"
    message = Message(
        user_id=msg.user_id,
        text=msg.text,
        response=response_text
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    db.close()
    return message


@app.get("/history/{user_id}", response_model=list[MessageOut])
def get_history(user_id: str):
    db = SessionLocal()
    history = db.query(Message).filter(Message.user_id == user_id).all()
    db.close()
    if not history:
        raise HTTPException(status_code=404, detail="История не найдена")
    return history
