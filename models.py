from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///fighters.db')

Base = declarative_base()


class Fighter(Base):
    
    __tablename__ = "fighters"
    
    id= Column(Integer(),primary_key= True)
    name = Column (String())
    gender = Column (String())
    bio = Column (String())
    skills= relationship('Skill',backref='fighter')
    
    
    def __repr__(self):
        return f'Fighter(id={self.id})' + \
            f'name= {self.name}'+ \
            f'gender= {self.gender})' + \
            f'bio={self.bio}'

class Skill(Base):
    __tablename__ = "skills"
    
    id= Column(Integer(),primary_key = True)
    name = Column(String())
    description = Column(String())
    fighter_id= Column(Integer(),ForeignKey('fighters.id'))
    arenas = relationship ('Arena',backref='skill')

    
    def __repr__(self):
        return f'Skill(id={self.id})' + \
            f'name= {self.name}'+ \
            f'description = {self.description})' + \
            f'fighter_id={self.fighter_id}'
            
class Arena (Base):
    
    __tablename__ = "arenas"
    
    id = Column(Integer(),primary_key=True)
    name = Column(Integer())
    skill_id = Column(Integer(), ForeignKey("skills.id"))

    order = relationship('Skill',
        backref=backref('skill', uselist=False))
        
    def __repr__(self):
        return f'Arena(id={self.id})' + \
            f'name= {self.name}'+ \
            f'skill_id={self.skill_id}'