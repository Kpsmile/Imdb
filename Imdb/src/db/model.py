from sqlalchemy import Integer, String, Float
from sqlalchemy import MetaData, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

metadata = MetaData()

Base = declarative_base(metadata=metadata)

class Genre(Base):
    __tablename__ = 'genre'
    genre_id = Column(Integer, autoincrement=True, primary_key=True)
    genre_name = Column(String(45), nullable=False)
    # genre_map = relationship("MovieGenreMap", cascade="delete")

class Movie(Base):
    __tablename__ = 'movie'
    movie_id = Column(Integer, autoincrement=True, primary_key=True)
    # genre_id = Column(Integer, ForeignKey('genre.genre_id'), nullable=False)
    popularity = Column(Float, nullable=True)
    director = Column(String(45), nullable=False)
    imdb_score =  Column(Float, nullable=True)
    movie_name = Column(String(505), nullable=False)
    # movie_map = relationship("MovieGenreMap", cascade="delete")


class Role(Base):
    __tablename__ = 'role'
    role_id = Column(Integer, autoincrement=True, primary_key=True)
    role_type = Column(String(45), nullable=False)


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.role_id'), nullable=False)
    user_name = Column(String(45), nullable=False)
    # user_role = relationship("Role", back_populates="user")

class MovieGenreMap(Base):
    __tablename__ = 'movie_genre_map'
    movie_genre_map_id = Column(Integer, autoincrement=True, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.movie_id'), nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.genre_id'), nullable=False)
    # movie = relationship("Movie", cascade="delete")
    # genre = relationship("Genre", cascade="delete")
    parent = relationship(Movie, backref=backref("MovieGenreMap", cascade="all,delete"))