from app import app
from extensions import db
from models import Question


SOCIAL_MEDIA_QUESTIONS = [
    # =========================================================
    # 1. PRIVACY AND OVERSHARING
    # =========================================================
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "You take a photo for Instagram, but your school badge "
            "and house number are visible in the background. "
            "What is the safest action?"
        ),
        "option_a": "Post it because only friends follow you",
        "option_b": "Remove or hide the identifying details before posting",
        "option_c": "Post it and delete it later",
        "option_d": "Add your location so friends know where you are",
        "correct_option": "B",
    },
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "A new social-media app asks for access to your contacts, "
            "camera, microphone and location before you can use it. "
            "What should you do?"
        ),
        "option_a": "Accept every permission immediately",
        "option_b": "Allow access because popular apps are always safe",
        "option_c": "Review the permissions and allow only those required",
        "option_d": "Ask a friend to accept the permissions for you",
        "correct_option": "C",
    },
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "You want to share a photograph from a family holiday on "
            "Instagram while you are still away from home. "
            "What is the safest choice?"
        ),
        "option_a": "Share your live location publicly",
        "option_b": "Post that nobody is currently at your house",
        "option_c": "Tag your home address",
        "option_d": "Wait until you return or restrict who can view it",
        "correct_option": "D",
    },
    {
        "category": "Privacy and Oversharing",
        "question_text": (
            "Someone you recently followed asks for your full name, "
            "school and date of birth. What should you do?"
        ),
        "option_a": "Do not share the information and review the account",
        "option_b": "Share it because the person seems friendly",
        "option_c": "Send only your school and date of birth",
        "option_d": "Ask them to share theirs first, then send yours",
        "correct_option": "A",
    },

    # =========================================================
    # 2. CYBERBULLYING
    # =========================================================
    {
        "category": "Cyberbullying",
        "question_text": (
            "Someone repeatedly posts insulting comments under your "
            "TikTok videos. What is the safest response?"
        ),
        "option_a": "Reply with stronger insults",
        "option_b": "Encourage friends to attack the person",
        "option_c": "Save evidence, block or report them and tell a trusted adult",
        "option_d": "Share the comments publicly to embarrass them",
        "correct_option": "C",
    },
    {
        "category": "Cyberbullying",
        "question_text": (
            "A private group chat is sharing an embarrassing photograph "
            "of a classmate without permission. What should you do?"
        ),
        "option_a": "Forward it to another group",
        "option_b": "Do not share it, support the classmate and report it",
        "option_c": "React with a laughing emoji but do not forward it",
        "option_d": "Save it for later",
        "correct_option": "B",
    },
    {
        "category": "Cyberbullying",
        "question_text": (
            "A friend says they are afraid to attend school because of "
            "abusive messages they receive on social media. "
            "What is the most helpful response?"
        ),
        "option_a": "Tell them to ignore it completely",
        "option_b": "Tell them to delete all evidence",
        "option_c": "Post the messages publicly without asking them",
        "option_d": "Listen, help preserve evidence and involve a trusted adult",
        "correct_option": "D",
    },
    {
        "category": "Cyberbullying",
        "question_text": (
            "Someone creates a fake Instagram account using your friend's "
            "photo and posts offensive content. What should you do?"
        ),
        "option_a": "Report the account and tell your friend",
        "option_b": "Follow the account to see what happens",
        "option_c": "Send the account abusive messages",
        "option_d": "Create another fake account in response",
        "correct_option": "A",
    },

    # =========================================================
    # 3. ONLINE GROOMING
    # =========================================================
    {
        "category": "Online Grooming",
        "question_text": (
            "Someone you met on Snapchat asks you to keep your conversations "
            "secret from your parents or carers. What is the safest response?"
        ),
        "option_a": "Agree because private friendships are normal",
        "option_b": "Stop the conversation and tell a trusted adult",
        "option_c": "Continue talking but delete the messages",
        "option_d": "Move the conversation to another app",
        "correct_option": "B",
    },
    {
        "category": "Online Grooming",
        "question_text": (
            "An online contact says they are your age but refuses to video "
            "call and asks to meet you alone. What should you do?"
        ),
        "option_a": "Meet them in a public place without telling anyone",
        "option_b": "Give them your address instead",
        "option_c": "Do not meet them and tell a trusted adult",
        "option_d": "Ask a friend to meet them for you",
        "correct_option": "C",
    },
    {
        "category": "Online Grooming",
        "question_text": (
            "A social-media contact gives you gifts and later pressures you "
            "to send a private photograph. What should you do?"
        ),
        "option_a": "Refuse, save evidence, block or report them and seek help",
        "option_b": "Send one photograph because they bought you gifts",
        "option_c": "Send a photograph that disappears",
        "option_d": "Ask them to send one first",
        "correct_option": "A",
    },
    {
        "category": "Online Grooming",
        "question_text": (
            "An older person online tells you that you are mature for your "
            "age and tries to separate you from your friends. "
            "What could this indicate?"
        ),
        "option_a": "A harmless compliment",
        "option_b": "A normal social-media friendship",
        "option_c": "A marketing technique",
        "option_d": "Possible grooming or manipulation",
        "correct_option": "D",
    },

    # =========================================================
    # 4. PHISHING AND SCAMS
    # =========================================================
    {
        "category": "Phishing and Scams",
        "question_text": (
            "You receive an Instagram message saying your account will be "
            "deleted unless you click a link immediately. What should you do?"
        ),
        "option_a": "Click quickly before the deadline",
        "option_b": "Reply with your password",
        "option_c": "Avoid the link and verify through the official app",
        "option_d": "Forward the link to friends",
        "correct_option": "C",
    },
    {
        "category": "Phishing and Scams",
        "question_text": (
            "A TikTok account says you have won a new phone but must pay a "
            "small delivery charge. What is the safest response?"
        ),
        "option_a": "Pay because the charge is small",
        "option_b": "Treat it as suspicious and do not provide payment details",
        "option_c": "Send your address before paying",
        "option_d": "Ask a friend to pay it",
        "correct_option": "B",
    },
    {
        "category": "Phishing and Scams",
        "question_text": (
            "A WhatsApp message appears to come from a friend asking urgently "
            "for money from a new number. What should you do?"
        ),
        "option_a": "Send the money immediately",
        "option_b": "Send half the amount first",
        "option_c": "Ask for their bank details",
        "option_d": "Verify their identity using another trusted method",
        "correct_option": "D",
    },
    {
        "category": "Phishing and Scams",
        "question_text": (
            "A direct message offers free game currency in exchange for your "
            "social-media password. What should you do?"
        ),
        "option_a": "Never share the password and report the message",
        "option_b": "Share it and change the password afterwards",
        "option_c": "Use a friend's password instead",
        "option_d": "Send only part of the password",
        "correct_option": "A",
    },

    # =========================================================
    # 5. FAKE PROFILES AND IMPERSONATION
    # =========================================================
    {
        "category": "Fake Profiles and Impersonation",
        "question_text": (
            "A celebrity account follows you, has very few posts and asks "
            "you to pay for access to a private fan group. What should you do?"
        ),
        "option_a": "Pay before the opportunity disappears",
        "option_b": "Check verification and report the account if suspicious",
        "option_c": "Send your personal information first",
        "option_d": "Invite friends to join",
        "correct_option": "B",
    },
    {
        "category": "Fake Profiles and Impersonation",
        "question_text": (
            "You receive a friend request from an account using your "
            "classmate's name and photograph, although you already follow "
            "your classmate. What is the safest action?"
        ),
        "option_a": "Accept because you recognise the photograph",
        "option_b": "Send the account your phone number",
        "option_c": "Verify with your classmate through another method",
        "option_d": "Share the profile publicly immediately",
        "correct_option": "C",
    },
    {
        "category": "Fake Profiles and Impersonation",
        "question_text": (
            "An account has stolen your photographs and is pretending to be "
            "you. What should you do?"
        ),
        "option_a": "Report the account, preserve evidence and tell a trusted adult",
        "option_b": "Give the account more photographs",
        "option_c": "Create another fake account",
        "option_d": "Ignore it even if it contacts your friends",
        "correct_option": "A",
    },
    {
        "category": "Fake Profiles and Impersonation",
        "question_text": (
            "Which sign most strongly suggests that a social-media profile "
            "may be fake?"
        ),
        "option_a": "It uses a profile photograph",
        "option_b": "It follows several people",
        "option_c": "It posts frequently",
        "option_d": "Its details conflict and its images appear copied",
        "correct_option": "D",
    },

    # =========================================================
    # 6. MISINFORMATION
    # =========================================================
    {
        "category": "Misinformation",
        "question_text": (
            "A TikTok video claims that a household product can cure a "
            "serious illness but provides no reliable source. "
            "What should you do before sharing it?"
        ),
        "option_a": "Share it because many people liked it",
        "option_b": "Check reliable health and evidence-based sources",
        "option_c": "Trust it because the creator sounds confident",
        "option_d": "Share it with a warning but do not check it",
        "correct_option": "B",
    },
    {
        "category": "Misinformation",
        "question_text": (
            "A dramatic social-media post includes an old photograph and "
            "claims it shows an event happening today. What should you do?"
        ),
        "option_a": "Share it before other people do",
        "option_b": "Assume photographs cannot be misleading",
        "option_c": "Check the original source, date and context",
        "option_d": "Believe it if a friend shared it",
        "correct_option": "C",
    },
    {
        "category": "Misinformation",
        "question_text": (
            "An influencer promotes a financial opportunity without stating "
            "that the post is sponsored. What should you consider?"
        ),
        "option_a": "The recommendation may be influenced by payment",
        "option_b": "Influencers are required to give perfect advice",
        "option_c": "A large follower count guarantees accuracy",
        "option_d": "Sponsored content carries no financial risk",
        "correct_option": "A",
    },
    {
        "category": "Misinformation",
        "question_text": (
            "Several accounts repeat the same claim, but none provides "
            "evidence. Does repetition make the claim reliable?"
        ),
        "option_a": "Yes, because many accounts cannot be wrong",
        "option_b": "Yes, if the posts have many comments",
        "option_c": "Yes, if the claim is trending",
        "option_d": "No, the original evidence and source still need checking",
        "correct_option": "D",
    },

    # =========================================================
    # 7. SOCIAL ENGINEERING
    # =========================================================
    {
        "category": "Social Engineering",
        "question_text": (
            "Someone claiming to be platform support asks for the security "
            "code sent to your phone. What should you do?"
        ),
        "option_a": "Send the code so they can protect the account",
        "option_b": "Do not share it and contact official support directly",
        "option_c": "Post the code publicly to check whether it is genuine",
        "option_d": "Send only the first few digits",
        "correct_option": "B",
    },
    {
        "category": "Social Engineering",
        "question_text": (
            "A person in a gaming group builds your trust and then asks for "
            "answers to your security questions. What should you do?"
        ),
        "option_a": "Answer because you have known them online for weeks",
        "option_b": "Give one answer only",
        "option_c": "Refuse and avoid sharing account-recovery information",
        "option_d": "Ask them for their answers first",
        "correct_option": "C",
    },
    {
        "category": "Social Engineering",
        "question_text": (
            "A message creates panic by saying your private photographs will "
            "be published unless you act immediately. What is the safest step?"
        ),
        "option_a": "Pause, preserve evidence and seek help from a trusted adult",
        "option_b": "Pay immediately",
        "option_c": "Delete your account without saving evidence",
        "option_d": "Send more information to negotiate",
        "correct_option": "A",
    },
    {
        "category": "Social Engineering",
        "question_text": (
            "Why do scammers often create urgency in social-media messages?"
        ),
        "option_a": "To make the message easier to read",
        "option_b": "To improve social-media security",
        "option_c": "To give users more time to investigate",
        "option_d": "To pressure users into acting without checking",
        "correct_option": "D",
    },

    # =========================================================
    # 8. DIGITAL FOOTPRINT AND REPUTATION
    # =========================================================
    {
        "category": "Digital Footprint and Reputation",
        "question_text": (
            "Before posting an embarrassing photograph of a friend on "
            "Instagram, what should you do?"
        ),
        "option_a": "Post it if you think it is funny",
        "option_b": "Ask for their permission and consider the consequences",
        "option_c": "Post it only at night",
        "option_d": "Tag as many people as possible",
        "correct_option": "B",
    },
    {
        "category": "Digital Footprint and Reputation",
        "question_text": (
            "You delete an offensive social-media post shortly after "
            "publishing it. Which statement is most accurate?"
        ),
        "option_a": "The post may still exist in screenshots or shared copies",
        "option_b": "Deleting it guarantees nobody saw it",
        "option_c": "Deleted posts can never affect your reputation",
        "option_d": "Only the platform can remember it",
        "correct_option": "A",
    },
    {
        "category": "Digital Footprint and Reputation",
        "question_text": (
            "A social-media trend encourages users to reveal personal secrets. "
            "What should you consider before participating?"
        ),
        "option_a": "Whether the trend has entertaining music",
        "option_b": "Whether your friends have participated",
        "option_c": "How the information could affect you now and in future",
        "option_d": "How quickly you can post it",
        "correct_option": "C",
    },
    {
        "category": "Digital Footprint and Reputation",
        "question_text": (
            "A future employer or university may be able to find some of your "
            "public social-media activity. What does this demonstrate?"
        ),
        "option_a": "Private messages are always public",
        "option_b": "Every social-media account must be deleted",
        "option_c": "Employers control all social-media platforms",
        "option_d": "Online posts can contribute to a lasting digital footprint",
        "correct_option": "D",
    },
]


def seed_questions():
    with app.app_context():
        # Remove the previous assessment questions.
        Question.query.delete()
        db.session.commit()

        for question_data in SOCIAL_MEDIA_QUESTIONS:
            question = Question(**question_data)
            db.session.add(question)

        db.session.commit()

        total_questions = Question.query.count()

        print(
            f"Successfully added {total_questions} "
            "social-media awareness questions."
        )


if __name__ == "__main__":
    seed_questions()