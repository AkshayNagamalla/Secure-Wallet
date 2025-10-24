from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, UUID, DateTime
from database import Base 
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import JSONB
import uuid

class Users(Base):
    __tablename__ = "users" 

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100)) 
    email: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)
    password_hash: Mapped[str | None] = mapped_column(String(256), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), default=lambda: datetime.now(timezone.utc)) 
    metadata: Mapped[dict] = mapped_column(JSONB, default=dict)

    def __repr__(self) -> str:
        return f"<User:(id={self.id !r}, name={self.name !r}, email={self.email !r})>"
