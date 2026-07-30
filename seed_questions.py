from app import app
from extensions import db
from models import Question


questions = [
    Question(
        category="Cyberbullying",
        question_text=(
            "You notice that several people are posting hurtful comments "
            "about a classmate. What is the safest response?"
        ),
        option_a="Join the conversation so you are not targeted",
        option_b="Ignore it because it does not involve you",
        option_c="Save the evidence, report it and tell a trusted adult",
        option_d="Reply with an equally hurtful comment",
        correct_option="C",
    ),
    Question(
        category="Privacy",
        question_text=(
            "Someone you recently met online asks for your home address. "
            "What should you do?"
        ),
        option_a="Send it if they appear friendly",
        option_b="Refuse and tell a trusted adult",
        option_c="Send only part of the address",
        option_d="Ask for their address first",
        correct_option="B",
    ),
    Question(
        category="Online Grooming",
        question_text=(
            "An online friend asks you to keep your conversations secret "
            "from your parents or carers. What should you do?"
        ),
        option_a="Keep it secret to protect the friendship",
        option_b="Continue chatting but avoid personal questions",
        option_c="Tell a trusted adult and stop private contact",
        option_d="Ask them why before deciding",
        correct_option="C",
    ),
    Question(
        category="Scams and Phishing",
        question_text=(
            "You receive a message saying you have won a prize and must "
            "click a link immediately. What should you do?"
        ),
        option_a="Click quickly before the prize expires",
        option_b="Forward it to friends",
        option_c="Reply and ask whether it is genuine",
        option_d="Do not click it; verify the sender through a trusted source",
        correct_option="D",
    ),
    Question(
        category="Misinformation",
        question_text=(
            "A dramatic social media post makes a serious claim but gives "
            "no reliable source. What should you do before sharing it?"
        ),
        option_a="Share it because many people have liked it",
        option_b="Check the claim using reliable and independent sources",
        option_c="Share it but add that it may be untrue",
        option_d="Assume it is true because it looks professional",
        correct_option="B",
    ),
]


with app.app_context():
    if Question.query.count() == 0:
        db.session.add_all(questions)
        db.session.commit()
        print("Five assessment questions were added successfully.")
    else:
        print("Questions already exist. No new questions were added.")