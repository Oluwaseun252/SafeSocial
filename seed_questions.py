from app import app
from extensions import db
from models import Question


questions = [
    # -------------------------------------------------
    # Cyberbullying
    # -------------------------------------------------
    {
        "category": "Cyberbullying",
        "question_text": (
            "You notice that several people are posting hurtful comments "
            "about a classmate. What is the safest response?"
        ),
        "option_a": "Join the conversation so you are not targeted",
        "option_b": "Ignore it because it does not involve you",
        "option_c": (
            "Save the evidence, report it and tell a trusted adult"
        ),
        "option_d": "Reply with an equally hurtful comment",
        "correct_option": "C",
    },
    {
        "category": "Cyberbullying",
        "question_text": (
            "Someone shares an embarrassing photo of your friend in a "
            "group chat and asks everyone to repost it."
        ),
        "option_a": "Share it so you are not left out.",
        "option_b": "Like the photo but do not repost it.",
        "option_c": "Refuse to share it and support your friend.",
        "option_d": "Edit the photo to make it funnier.",
        "correct_option": "C",
    },
    {
        "category": "Cyberbullying",
        "question_text": (
            "A friend tells you they are receiving threatening messages "
            "every day online."
        ),
        "option_a": "Tell them to delete the messages.",
        "option_b": "Tell them to fight back online.",
        "option_c": (
            "Encourage them to report the messages and speak to a "
            "trusted adult."
        ),
        "option_d": "Post the messages publicly.",
        "correct_option": "C",
    },
    {
        "category": "Cyberbullying",
        "question_text": (
            "You witness a livestream where viewers are encouraging "
            "others to insult another teenager."
        ),
        "option_a": "Join the comments.",
        "option_b": "Watch without doing anything.",
        "option_c": "Record the stream for entertainment.",
        "option_d": "Report the livestream and leave the stream.",
        "correct_option": "D",
    },
    {
        "category": "Cyberbullying",
        "question_text": (
            "Someone creates a fake account pretending to be one of your "
            "classmates and posts offensive messages."
        ),
        "option_a": "Share the account with friends.",
        "option_b": "Ignore the account.",
        "option_c": (
            "Report the fake account and inform your classmate."
        ),
        "option_d": "Create another fake account in response.",
        "correct_option": "C",
    },

    # -------------------------------------------------
    # Privacy and Oversharing
    # -------------------------------------------------
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "Someone you recently met online asks for your home address. "
            "What should you do?"
        ),
        "option_a": "Send it if they appear friendly",
        "option_b": "Refuse and tell a trusted adult",
        "option_c": "Send only part of the address",
        "option_d": "Ask for their address first",
        "correct_option": "B",
    },
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "You are about to post a photo showing your school badge and "
            "the street outside your home. What is the safest action?"
        ),
        "option_a": (
            "Post it because only your followers can see it."
        ),
        "option_b": (
            "Remove or hide details that reveal your school or location."
        ),
        "option_c": "Tag your school so friends can find the post.",
        "option_d": (
            "Add your live location to make the post more interesting."
        ),
        "correct_option": "B",
    },
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "A social media quiz asks for your full name, date of birth, "
            "school and first pet's name. What should you do?"
        ),
        "option_a": "Complete it because quizzes are harmless.",
        "option_b": "Give false answers but still submit it.",
        "option_c": "Share only your date of birth.",
        "option_d": (
            "Avoid submitting it because the information could be used "
            "to guess passwords or security answers."
        ),
        "correct_option": "D",
    },
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "Your friend tags you in a public post that reveals where you "
            "will be spending the weekend. What is the safest response?"
        ),
        "option_a": (
            "Leave it because the post was made by a friend."
        ),
        "option_b": "Share it again so more people can see it.",
        "option_c": (
            "Remove the tag or ask your friend to delete the location "
            "details."
        ),
        "option_d": "Add the exact time you will arrive.",
        "correct_option": "C",
    },
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "An app requests access to your contacts, camera, microphone "
            "and location even though these are not needed for its main "
            "purpose. What should you do?"
        ),
        "option_a": "Allow everything so the app works properly.",
        "option_b": (
            "Review the permissions and allow only those genuinely "
            "required."
        ),
        "option_c": (
            "Allow access temporarily and forget about it."
        ),
        "option_d": (
            "Share the app with friends before checking the permissions."
        ),
        "correct_option": "B",
    },

    # -------------------------------------------------
    # Online Grooming
    # -------------------------------------------------
    {
        "category": "Online Grooming",
        "question_text": (
            "An online friend asks you to keep your conversations secret "
            "from your parents or carers. What should you do?"
        ),
        "option_a": "Keep it secret to protect the friendship",
        "option_b": (
            "Continue chatting but avoid personal questions"
        ),
        "option_c": (
            "Tell a trusted adult and stop private contact"
        ),
        "option_d": "Ask them why before deciding",
        "correct_option": "C",
    },
    {
        "category": "Online Grooming",
        "question_text": (
            "An online gamer offers to buy you expensive gifts if you "
            "continue chatting privately. What is the safest response?"
        ),
        "option_a": (
            "Accept the gifts because they are being kind."
        ),
        "option_b": "Accept only if you never meet them.",
        "option_c": (
            "Stop communicating, block the person and tell a trusted "
            "adult."
        ),
        "option_d": (
            "Give them your address so they can send the gifts."
        ),
        "correct_option": "C",
    },
    {
        "category": "Online Grooming",
        "question_text": (
            "Someone you met on social media asks you to move your "
            "conversation to a private messaging app. What should you do?"
        ),
        "option_a": (
            "Move immediately because private chats are safer."
        ),
        "option_b": (
            "Move only after sharing your phone number."
        ),
        "option_c": (
            "Be cautious and tell a trusted adult if the person is making "
            "you uncomfortable or asking personal questions."
        ),
        "option_d": (
            "Delete all previous messages and continue chatting."
        ),
        "correct_option": "C",
    },
    {
        "category": "Online Grooming",
        "question_text": (
            "An online friend says they are the same age as you and wants "
            "to meet in person without telling anyone. What is the safest "
            "action?"
        ),
        "option_a": "Meet them because they seem friendly.",
        "option_b": (
            "Meet in a public place without telling your family."
        ),
        "option_c": (
            "Refuse the meeting and tell a trusted adult immediately."
        ),
        "option_d": "Ask them to bring another friend.",
        "correct_option": "C",
    },
    {
        "category": "Online Grooming",
        "question_text": (
            "Someone online asks you to send a personal photo and promises "
            "nobody else will ever see it. What should you do?"
        ),
        "option_a": (
            "Send one photo because they promised to keep it private."
        ),
        "option_b": "Edit the photo before sending it.",
        "option_c": (
            "Refuse, block the person if necessary and report the "
            "behaviour."
        ),
        "option_d": "Ask them to send their photo first.",
        "correct_option": "C",
    },

    # -------------------------------------------------
    # Scams and Phishing
    # -------------------------------------------------
    {
        "category": "Scams and Phishing",
        "question_text": (
            "You receive a message saying you have won a prize and must "
            "click a link immediately. What should you do?"
        ),
        "option_a": "Click quickly before the prize expires",
        "option_b": "Forward it to friends",
        "option_c": "Reply and ask whether it is genuine",
        "option_d": (
            "Do not click it; verify the sender through a trusted source"
        ),
        "correct_option": "D",
    },
    {
        "category": "Scams and Phishing",
        "question_text": (
            "A message that appears to be from your social media platform "
            "asks you to confirm your password because of suspicious "
            "activity. What is the safest response?"
        ),
        "option_a": (
            "Send the password so the account is not closed."
        ),
        "option_b": "Click the message link and log in.",
        "option_c": (
            "Open the official app or website directly and check your "
            "account security there."
        ),
        "option_d": (
            "Reply and ask whether the message is genuine."
        ),
        "correct_option": "C",
    },
    {
        "category": "Scams and Phishing",
        "question_text": (
            "A social media post promises free game credits if you enter "
            "your username, password and payment details. What is the "
            "safest action?"
        ),
        "option_a": (
            "Enter the details because the offer is free."
        ),
        "option_b": "Use a different password and continue.",
        "option_c": "Ask a friend to test the offer first.",
        "option_d": (
            "Do not provide any details and report the post as a "
            "possible scam."
        ),
        "correct_option": "D",
    },
    {
        "category": "Scams and Phishing",
        "question_text": (
            "An online seller offers a popular item at a very low price "
            "but asks you to pay outside the official marketplace. What "
            "should you do?"
        ),
        "option_a": "Pay quickly before someone else buys it.",
        "option_b": "Use the payment method they request.",
        "option_c": "Send half the money first.",
        "option_d": (
            "Avoid the payment and use the marketplace's protected "
            "payment system."
        ),
        "correct_option": "D",
    },
    {
        "category": "Scams and Phishing",
        "question_text": (
            "A friend's account sends you an unusual message asking for "
            "money because of an emergency. What should you do?"
        ),
        "option_a": "Send the money immediately.",
        "option_b": "Reply with your bank details.",
        "option_c": (
            "Contact your friend through another trusted method to "
            "confirm the request."
        ),
        "option_d": "Share the message publicly.",
        "correct_option": "C",
    },

    # -------------------------------------------------
    # Misinformation
    # -------------------------------------------------
    {
        "category": "Misinformation",
        "question_text": (
            "A dramatic social media post makes a serious claim but gives "
            "no reliable source. What should you do before sharing it?"
        ),
        "option_a": (
            "Share it because many people have liked it"
        ),
        "option_b": (
            "Check the claim using reliable and independent sources"
        ),
        "option_c": "Share it but add that it may be untrue",
        "option_d": (
            "Assume it is true because it looks professional"
        ),
        "correct_option": "B",
    },
    {
        "category": "Misinformation",
        "question_text": (
            "A short video makes a serious health claim but provides no "
            "evidence or expert source. What is the safest response?"
        ),
        "option_a": (
            "Follow the advice because the video looks professional."
        ),
        "option_b": (
            "Share it with friends to ask what they think."
        ),
        "option_c": (
            "Trust it if the creator has many followers."
        ),
        "option_d": (
            "Check the claim using reliable health organisations or "
            "qualified experts."
        ),
        "correct_option": "D",
    },
    {
        "category": "Misinformation",
        "question_text": (
            "You see a dramatic image being shared as proof of a recent "
            "event. What should you do before accepting it as genuine?"
        ),
        "option_a": (
            "Assume it is real because it looks convincing."
        ),
        "option_b": (
            "Check whether trusted news sources confirm it and whether "
            "the image has been used in a different context."
        ),
        "option_c": (
            "Share it and delete it later if it is false."
        ),
        "option_d": "Believe it if a friend posted it.",
        "correct_option": "B",
    },
    {
        "category": "Misinformation",
        "question_text": (
            "Two social media accounts give conflicting information about "
            "the same event. What is the best response?"
        ),
        "option_a": (
            "Believe the account with more followers."
        ),
        "option_b": (
            "Choose the version that agrees with your opinion."
        ),
        "option_c": "Ignore both without checking anything.",
        "option_d": (
            "Compare the claims with multiple reliable and independent "
            "sources."
        ),
        "correct_option": "D",
    },
    {
        "category": "Misinformation",
        "question_text": (
            "A post uses an alarming headline, but the article underneath "
            "says something less dramatic. What should you do?"
        ),
        "option_a": (
            "Share the headline because it attracts attention."
        ),
        "option_b": (
            "Comment on the headline without reading the article."
        ),
        "option_c": (
            "Read the full article and check the original source before "
            "deciding whether to share it."
        ),
        "option_d": (
            "Assume the headline accurately summarises everything."
        ),
        "correct_option": "C",
    },
]


def seed_questions():
    added_count = 0
    updated_count = 0

    with app.app_context():
        for question_data in questions:
            existing_question = Question.query.filter_by(
                question_text=question_data["question_text"]
            ).first()

            if existing_question is None:
                question = Question(**question_data)
                db.session.add(question)
                added_count += 1

            else:
                # Keep existing questions consistent with this script.
                changed = False

                for field, value in question_data.items():
                    if getattr(existing_question, field) != value:
                        setattr(existing_question, field, value)
                        changed = True

                if changed:
                    updated_count += 1

        try:
            db.session.commit()

            total_questions = Question.query.count()

            print(
                f"Question seeding completed: "
                f"{added_count} added, "
                f"{updated_count} updated, "
                f"{total_questions} total."
            )

        except Exception as error:
            db.session.rollback()
            print(f"Question seeding failed: {error}")
            raise


if __name__ == "__main__":
    seed_questions()