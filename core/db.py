from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(String(255), nullable=False)  # Restricted to 255 identifiers for indexing
    role = Column(String(255), nullable=False)  # e.g., "user" or "assistant"
    content = Column(String, nullable=False)  # Limitless text content
    timestamp = Column(DateTime, default=datetime.now)

class Database:
    def __init__(self):
        # Load database configuration from environment variables
        DB_USER = os.getenv("POSTGRES_USER")
        DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        DB_NAME = os.getenv("POSTGRES_DB")
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_PORT = int(os.getenv("DB_PORT", 5432))

        # Validate required environment variables
        missing_vars = []
        if not DB_USER:
            missing_vars.append("POSTGRES_USER")
        if not DB_PASSWORD:
            missing_vars.append("POSTGRES_PASSWORD")
        if not DB_NAME:
            missing_vars.append("POSTGRES_DB")
        if missing_vars:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        # Initialize database connection
        self.engine = create_engine(
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.SessionLocal()
        
        try:
            yield db
        finally:
            db.close()

    def save_message(self, conversation_id, role, content):
        db = self.SessionLocal()

        try:
            new_message = Message(
                conversation_id=conversation_id,
                role=role,
                content=content
            )

            db.add(new_message)
            db.commit()
            db.refresh(new_message)  # Refresh to get the new ID

            return new_message
        
        except Exception as e:
            # If an error occurs, rollback the transaction
            db.rollback()
            raise e

        finally:
            db.close()

    def get_message(self, conversation_id):
        """
        Retrieve all messages for a given conversation_id.
        Returns a list of Message objects.
        """
        db = self.SessionLocal()
        try:
            messages = db.query(Message).filter(Message.conversation_id == conversation_id).order_by(Message.timestamp).all()

            return messages
        except Exception as e:
            # If an error occurs, rollback the transaction
            db.rollback()
            raise e

        finally:
            db.close()