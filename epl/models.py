from epl import db
from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import List

class Club(db.Model):
    __tablename__ = 'clubs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    stadium: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[str] = mapped_column(String(255), nullable=False)

    Players: Mapped[List["Player"]] = relationship(back_populates="club")

    def __repr__(self):
        return f'<Club:{self.name}>'
    


class Player(db.Model):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    position: Mapped[str] = mapped_column(String(50), nullable=False)
    nationality: Mapped[str] = mapped_column(String(50), nullable=False)
    goal: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    squad_no: Mapped[int] = mapped_column(Integer, nullable=True)
    img: Mapped[str] = mapped_column(String(255), nullable=False)
    clean_sheets: Mapped[int] = mapped_column(Integer, nullable=True)
    club_id: Mapped[int] = mapped_column(Integer, ForeignKey(Club.id))

    club: Mapped["Club"] = relationship("Club", back_populates="Players")

    def __repr__(self):
        return f'<Player:{self.name}>'