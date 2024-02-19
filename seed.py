import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base,Fighter,Arena,Skill


if __name__ == "__main__":
    
    engine = create_engine('sqlite:///fighters.db')
    Base.metadata.bind = engine
    Session = sessionmaker (bind=engine)
    session = Session()
    
    #fighters seed data
    sd = Fighter (name= 'Snoop Dogg', gender = 'M', bio = 'Known to put enemies in a spliff')
    dmx = Fighter (name= 'DMX', gender = 'M', bio = 'He secretly knows who let the dogs out')
    me = Fighter (name= 'Missy Eliot', gender = 'F', bio = 'The boots stay clean before and after the fight ')
    lk = Fighter (name= 'Lil Kim', gender = 'F', bio = 'SHe rarely has time in her schedule so wraps it up quickly')
    
    
    session.add_all([sd,dmx,me,lk])
    session.commit
    
    #skills data
    hp = Skill(name='Health Points', description= "reduces damage taken", fighter = dmx, arena=td)
    ds = Skill (name='Speed Points' ,description= "increases speed", fighter = sd, arena=dp)
    am = Skill (name = "Amnesia", description= "Confused enemy temporarily", fighter = lk, arena=ct) 
    mt = Skill(name = 'Midas Touch' ,description = "Turns enemy into gold temporarily", figther= me, arena=msg)
    inf = Skill (name = 'Infereno', description = 'boosts all abilities for 10s', fighter = sd, arena = rs)
    sm = Skill (name ='Slow-Motion', description = "slows down time temporarily", fighter= lk, arena = cw)
    session.add_all([hp,ds,am,mt,inf,sm])
    session.commit
    
    #Arena data 
    td = Arena (name='Thunder dome',skill =hp)
    dp = Arena (name='Dog Pound',skill =hp)
    ct = Arena (name='China Town',skill= am)
    msg = Arena (name='Maddison Square Garden',skill= mt)
    rs = Arena (name = 'Recording Studio', skill= inf )
    cw = Arena (name = 'Car Wash',skill = sm)
    
    session.add_all([td,dp,ct,msg,rs,cw])
    session.commit()
    