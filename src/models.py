import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    email=Column(String(250))
    password=Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer, nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer)  
    characters = relationship('character', backref='planet', lazy=True)
    species = relationship('specie', backref='planet', lazy=True)
 

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(30), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'),nullable=False)
  

class Specie(Base):
    __tablename__='specie'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    designation = Column(String(250))
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    eye_colors = Column(String(250))
    language = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planet.id'),nullable=False)
    characters = relationship('character', secondary='specie_character', lazy='subquery',backref=('specie'))
   

class SpecieCharacter(Base):
    __tablename__='specie_character'
    id_character=Column(Integer, ForeignKey('character.id'),primary_key=True)
    id_specie=Column(Integer, ForeignKey('specie.id'),primary_key=True)
   

class Film(Base):
    __tablename__='film'
    id=Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    episode_id = Column(Integer, nullable=False)
    producer = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=False)
    opening = Column(String(8000))
    characters = relationship('character', secondary='film_character', lazy='subquery',backref=('film'))
    planets = relationship('planet', secondary='film_planet', lazy='subquery',backref=('film'))
    species = relationship('specie', secondary='film_specie', lazy='subquery',backref=('film'))

class FilmCharacter(Base):
    __tablename__='film_character'
    id_character=Column(Integer, ForeignKey('character.id'),primary_key=True)
    id_film=Column(Integer, ForeignKey('film.id'),primary_key=True)


class FilmPlanet(Base):
    __tablename__='film_planet'
    id_planet=Column(Integer, ForeignKey('planet.id'),primary_key=True)
    id_film=Column(Integer, ForeignKey('film.id'),primary_key=True)
  

class FilmSpecie(Base):
    __tablename__='film_specie'
    id_specie=Column(Integer, ForeignKey('specie.id'),primary_key=True)
    id_film=Column(Integer, ForeignKey('film.id'),primary_key=True)
  

class Favorite(Base):
    __tablename__='favorite'
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'), nullable=False)
    favorite_id=Column(Integer, nullable=False)
    favorite_name=Column(String(250),nullable=False)
    favorite_type = Column(String(1))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')