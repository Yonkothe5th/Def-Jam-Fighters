import click
from models import Base, Fighter, Skill, Arena, engine
from sqlalchemy.orm import sessionmaker

# Create the database tables
Base.metadata.create_all(engine)

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def list_fighters():
    fighters = session.query(Fighter).all()
    for fighter in fighters:
        click.echo(fighter)
        
    main_menu()

@cli.command()
def list_skills():
    skills = session.query(Skill).all()
    for skill in skills:
        click.echo(skill)

    main_menu()
    
@cli.command()
def list_arenas():
    arenas = session.query(Arena).all()
    for arena in arenas:
        click.echo(arena)
        
    main_menu()

@cli.command()
@click.option('--name', prompt='Enter fighter name')
@click.option('--gender', prompt='Enter fighter gender')
@click.option('--bio', prompt='Enter fighter bio')
def add_fighter(name, gender, bio):
    new_fighter = Fighter(name=name, gender=gender, bio=bio)
    session.add(new_fighter)
    session.commit()
    click.echo('Fighter added successfully.')
    
    main_menu()

@cli.command()
@click.option('--name', prompt='Enter skill name')
@click.option('--description', prompt='Enter skill description')
def add_skill(name, description):
    new_skill = Skill(name=name, description=description)
    session.add(new_skill)
    session.commit()
    click.echo('Skill added successfully.')
    
    main_menu()

@cli.command()
@click.option('--name', prompt='Enter arena name')
@click.option('--skill_id', prompt='Enter skill ID')
def add_arena(name, skill_id):
    new_arena = Arena(name=name, skill_id=skill_id)
    session.add(new_arena)
    session.commit()
    click.echo('Arena added successfully.')
    
    main_menu()

@cli.command()
def display_fighters_skills():
    fighters = session.query(Fighter).all()
    for fighter in fighters:
        click.echo(f'{fighter.name} - Skills: {[skill.name for skill in fighter.skills]}')
        
    main_menu()

@cli.command()
@click.option('--fighter_name', prompt='Enter fighter name')
@click.option('--new_skill_name', prompt='Enter new skill name')
def change_fighter_skill(fighter_name, new_skill_name):
    fighter = session.query(Fighter).filter_by(name=fighter_name).first()
    new_skill = session.query(Skill).filter_by(name=new_skill_name).first()
    
    if fighter and new_skill:
        fighter.skills = [new_skill]
        session.commit()
        click.echo(f"{fighter_name}'s skill changed to {new_skill_name} successfully.")
    else:
        click.echo('Fighter or skill not found.')
        
    main_menu()

@cli.command()
@click.option('--skill_name', prompt='Enter skill name')
@click.option('--new_arena_name', prompt='Enter new arena name')
def change_skill_arena(skill_name, new_arena_name):
    skill = session.query(Skill).filter_by(name=skill_name).first()
    new_arena = session.query(Arena).filter_by(name=new_arena_name).first()

    if skill and new_arena:
        skill.arenas = [new_arena]
        session.commit()
        click.echo(f"{skill_name}'s arena changed to {new_arena_name} successfully.")
    else:
        click.echo('Skill or arena not found.')
        
    main_menu()
    
@cli.command()
@click.option('--fighter_name', prompt='Enter fighter name to delete')
def delete_fighter(fighter_name):
    fighter = session.query(Fighter).filter_by(name=fighter_name).first()

    if fighter:
        session.delete(fighter)
        session.commit()
        click.echo(f'Fighter "{fighter_name}" deleted successfully.')
    else:
        click.echo('Fighter not found.')

    main_menu()



def print_main_menu():
    click.echo("Main Menu:")
    click.echo("1. List of Fighters")
    click.echo("2. List of Skills")
    click.echo("3. List of Arenas")
    click.echo("4. Recruit a Fighter")
    click.echo("5. Train a Skill")
    click.echo("6. Add an Arena")
    click.echo("7. Show Fighters and Their Skills")
    click.echo("8. Change Fighter's Skill")
    click.echo("9. Change Skill's Arena")
    click.echo ("10. Eliminate a Fighter")
    click.echo("0. Exit")

@cli.command()
def main_menu():
    while True:
        print_main_menu()
        choice = click.prompt('Pick your Bane(0-10)', type=int)
        
        if choice == 0:
            click.echo('Game Over!')
            break
        elif choice == 1:
            list_fighters()
        elif choice == 2:
            list_skills()
        elif choice == 3:
            list_arenas()
        elif choice == 4:
            add_fighter()
        elif choice == 5:
            add_skill()
        elif choice == 6:
            add_arena()
        elif choice == 7:
            display_fighters_skills()
        elif choice == 8:
            change_fighter_skill()
        elif choice == 9:
            change_skill_arena()
        elif choice == 10:
            delete_fighter() 
        else:
            click.echo('Stay within Bounds')

if __name__ == '__main__':
    main_menu()
