from sqlalchemy import String, Integer, UUID, ForeignKey,Enum, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base 
from datetime import datetime, timezone
import enum
import uuid 

class ItemType(enum.Enum):
    File = "File"
    Folder = "Folder" 

class Items(Base):
    __tablename__ = "items"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    parent_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("items.id", ondelete="CASCADE"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[ItemType] = mapped_column(Enum(ItemType), nullable=False)
    mime_type: Mapped[str | None] = mapped_column(String, nullable=True)
    uri: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    size: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    parent: Mapped["Items"] = relationship(
        back_populates="children",
        remote_side=[id]
        ) 
    children: Mapped[list["Items"]] = relationship(
        back_populates="parent" , 
        uselist=True
        )
    
    def __repr__(self) -> str:
        return f"<Item:(id={self.id !r}) name={self.name !r} type={self.type.value !r}>"