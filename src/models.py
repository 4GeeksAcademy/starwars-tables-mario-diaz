from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="user")

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[str] = mapped_column(nullable=False)

    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="characters")

class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    characters: Mapped["Characters"] = relationship(back_populates="favorite_characters")
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="favorite_characters")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
