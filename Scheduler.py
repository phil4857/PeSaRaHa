from database import SessionLocal
import crud
from models import User

def daily_rewards():
    db = SessionLocal()
    users = db.query(User).filter(User.membership_active==True).all()
    for u in users:
        crud.add_reward(db, u.id, 50)  # daily 50 credits
    db.close()
    print("Daily rewards distributed")

if __name__ == "__main__":
    daily_rewards()
