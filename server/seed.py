"""
Database seed script.

Drops all tables, recreates them, and inserts representative demo data for
every model (User, Tag, Note).  Intended for development and grading only.

Usage:
    python seed.py
"""
from dotenv import load_dotenv

load_dotenv()

from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.note import Note, Tag
from app.config import DevelopmentConfig


def seed():
    app = create_app(DevelopmentConfig)

    with app.app_context():
        print("🗑  Dropping all tables …")
        db.drop_all()

        print("🏗  Creating all tables …")
        db.create_all()

        # ------------------------------------------------------------------ #
        # Users                                                                #
        # ------------------------------------------------------------------ #
        print("\n👤 Creating users …")

        alice = User(username="alice")
        alice.set_password("password123")

        bob = User(username="bob")
        bob.set_password("password123")

        carol = User(username="carol")
        carol.set_password("password123")

        db.session.add_all([alice, bob, carol])
        db.session.commit()
        print(f"   ✅ alice (id={alice.id}), bob (id={bob.id}), carol (id={carol.id})")

        # ------------------------------------------------------------------ #
        # Tags                                                                 #
        # ------------------------------------------------------------------ #
        print("\n🏷  Creating tags …")

        alice_tags = [
            Tag(user_id=alice.id, name="Work",     color="#3B82F6"),
            Tag(user_id=alice.id, name="Personal", color="#10B981"),
            Tag(user_id=alice.id, name="Ideas",    color="#F59E0B"),
        ]
        bob_tags = [
            Tag(user_id=bob.id, name="Dev",     color="#8B5CF6"),
            Tag(user_id=bob.id, name="Reading", color="#EC4899"),
        ]
        carol_tags = [
            Tag(user_id=carol.id, name="Health",  color="#EF4444"),
            Tag(user_id=carol.id, name="Finance", color="#14B8A6"),
        ]

        db.session.add_all(alice_tags + bob_tags + carol_tags)
        db.session.commit()
        print(f"   ✅ {len(alice_tags + bob_tags + carol_tags)} tags created")

        # ------------------------------------------------------------------ #
        # Notes                                                                #
        # ------------------------------------------------------------------ #
        print("\n📝 Creating notes …")

        alice_notes = [
            Note(
                user_id=alice.id,
                tag_id=alice_tags[0].id,
                title="Q2 Roadmap",
                content="Outline the key features and milestones for Q2.",
                pinned=True,
            ),
            Note(
                user_id=alice.id,
                tag_id=alice_tags[0].id,
                title="Sprint Planning Notes",
                content="Team capacity: 42 story points. Focus on auth and dashboard.",
                pinned=False,
            ),
            Note(
                user_id=alice.id,
                tag_id=alice_tags[1].id,
                title="Grocery List",
                content="Milk, eggs, bread, avocados, coffee beans.",
                pinned=False,
            ),
            Note(
                user_id=alice.id,
                tag_id=alice_tags[2].id,
                title="Side Project Ideas",
                content="1. Recipe tracker  2. Habit journal  3. Budget visualiser",
                pinned=True,
            ),
            Note(
                user_id=alice.id,
                tag_id=None,
                title="Book Recommendations",
                content="Clean Code, The Pragmatic Programmer, Designing Data-Intensive Applications.",
                pinned=False,
            ),
        ]

        bob_notes = [
            Note(
                user_id=bob.id,
                tag_id=bob_tags[0].id,
                title="Database Schema v2",
                content="Add indexes on user_id columns.  Consider partitioning notes table.",
                pinned=True,
            ),
            Note(
                user_id=bob.id,
                tag_id=bob_tags[0].id,
                title="API Docs Checklist",
                content="Document /notes, /tags, /signup, /login, /me endpoints.",
                pinned=False,
            ),
            Note(
                user_id=bob.id,
                tag_id=bob_tags[1].id,
                title="Currently Reading",
                content="Atomic Habits — chapter 12.  Fluent Python — chapter 5.",
                pinned=False,
            ),
        ]

        carol_notes = [
            Note(
                user_id=carol.id,
                tag_id=carol_tags[0].id,
                title="Weekly Workout Plan",
                content="Mon: run 5k  Wed: yoga  Fri: strength training",
                pinned=True,
            ),
            Note(
                user_id=carol.id,
                tag_id=carol_tags[1].id,
                title="Monthly Budget",
                content="Income: 4500  Rent: 1200  Food: 400  Savings: 900",
                pinned=False,
            ),
        ]

        all_notes = alice_notes + bob_notes + carol_notes
        db.session.add_all(all_notes)
        db.session.commit()
        print(f"   ✅ {len(all_notes)} notes created")

        # ------------------------------------------------------------------ #
        # Summary                                                              #
        # ------------------------------------------------------------------ #
        print("\n✨ Seeding complete!")
        print("\n📋 Demo credentials:")
        print("   alice   / password123")
        print("   bob     / password123")
        print("   carol   / password123")


if __name__ == "__main__":
    seed()
