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
    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="user")
    favorite_vehicles: Mapped[List["FavoriteVehicle"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "is_active": self.is_active
    }


class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[str] = mapped_column(nullable=False)

    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="characters")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year
    }

class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    characters: Mapped["Characters"] = relationship(back_populates="favorite_characters")
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="favorite_characters")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
    }


class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)

    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planets")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain
    }

class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    planets: Mapped["Planets"] = relationship(back_populates="favorite_planets")
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="favorite_planets")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
    }


class Vehicles(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)   
    vehicle_class: Mapped[str] = mapped_column(nullable=False)

    favorite_vehicles: Mapped[List["FavoriteVehicle"]] = relationship(back_populates="Vehicles")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class
    }

class FavoriteVehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    vehicle: Mapped["Vehicles"] = relationship(back_populates="favorite_vehicles")
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="favorite_vehicles")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,             
            "user_id": self.user_id,      
            "vehicle_id": self.vehicle_id   
        }


    
