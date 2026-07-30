from typing import Optional


def get_safebot_response(
    user_message: str,
    weakest_category: Optional[str] = None,
) -> dict:
    """
    Analyse a user's message and return a controlled online-safety response.

    The function uses keyword matching rather than a generative AI model.
    This keeps SafeBot focused, predictable and suitable for teenage users.
    """

    message = user_message.strip().lower()

    if not message:
        return {
            "reply": (
                "Please type a question about online safety, social media, "
                "privacy, scams or cyberbullying."
            ),
            "module": None,
            "category": "general",
        }

    safety_topics = [
        {
            "category": "privacy",
            "keywords": [
                "address",
                "phone number",
                "location",
                "personal information",
                "private information",
                "oversharing",
                "share my number",
                "where i live",
                "school name",
            ],
            "reply": (
                "Be careful about sharing personal information online. "
                "Do not give your address, phone number, school, live "
                "location or other private details to someone you do not "
                "know and trust. Stop replying if you feel pressured and "
                "speak to a trusted adult."
            ),
            "module": "Privacy and Oversharing",
        },
        {
            "category": "phishing",
            "keywords": [
                "phishing",
                "suspicious link",
                "strange link",
                "click this link",
                "free prize",
                "won a prize",
                "verify account",
                "bank details",
                "login details",
                "scam message",
            ],
            "reply": (
                "Do not click the link or provide any personal or login "
                "details. Check who sent the message and visit the official "
                "website directly instead of using the link. Delete or "
                "report the message if it appears suspicious."
            ),
            "module": "Phishing and Scams",
        },
        {
            "category": "passwords",
            "keywords": [
                "password",
                "hacked",
                "hack",
                "account stolen",
                "cannot log in",
                "someone logged in",
                "two factor",
                "2fa",
                "security code",
            ],
            "reply": (
                "Change your password immediately and use a strong, unique "
                "password that you do not use on another account. Turn on "
                "two-factor authentication, sign out of unfamiliar devices "
                "and report the problem to the platform."
            ),
            "module": "Passwords and Account Security",
        },
        {
            "category": "cyberbullying",
            "keywords": [
                "cyberbullying",
                "bullying",
                "mean messages",
                "insulting me",
                "threatening me",
                "harassing me",
                "spreading rumours",
                "making fun of me",
                "hate comments",
            ],
            "reply": (
                "You do not have to deal with online bullying alone. Avoid "
                "arguing with the person, save screenshots as evidence, "
                "block and report the account, and tell a trusted adult, "
                "teacher or safeguarding professional."
            ),
            "module": "Cyberbullying",
        },
        {
            "category": "fake_profiles",
            "keywords": [
                "fake account",
                "fake profile",
                "pretending to be",
                "catfish",
                "catfishing",
                "impersonating",
                "not who they say",
                "online friend",
            ],
            "reply": (
                "People online may not always be who they claim to be. "
                "Do not share personal information, money or private images. "
                "Avoid meeting them in person, block suspicious accounts and "
                "tell a trusted adult if you feel uncomfortable."
            ),
            "module": "Fake Profiles and Online Identity",
        },
        {
            "category": "grooming",
            "keywords": [
                "meet in person",
                "keep it secret",
                "secret from parents",
                "older person",
                "send a photo",
                "send pictures",
                "private photo",
                "inappropriate photo",
                "sexual message",
                "grooming",
            ],
            "reply": (
                "Do not send private or intimate images and do not agree to "
                "meet the person. Stop communicating, keep evidence, block "
                "and report the account, and tell a trusted adult immediately. "
                "It is not your fault if someone is pressuring you."
            ),
            "module": "Online Grooming and Unsafe Contact",
        },
        {
            "category": "scams",
            "keywords": [
                "scam",
                "money",
                "gift card",
                "investment",
                "giveaway",
                "buy something",
                "send payment",
                "free money",
                "urgent payment",
            ],
            "reply": (
                "Do not send money, gift-card codes or payment information. "
                "Scammers often create urgency or promise rewards that seem "
                "too good to be true. Check with a trusted adult and report "
                "the account or message."
            ),
            "module": "Phishing and Scams",
        },
        {
            "category": "harmful_content",
            "keywords": [
                "disturbing content",
                "violent video",
                "harmful content",
                "inappropriate content",
                "upsetting video",
                "graphic content",
                "dangerous challenge",
            ],
            "reply": (
                "Leave the page and do not share the content with others. "
                "Use the platform's report and block tools, adjust your "
                "content settings and speak to a trusted adult if the content "
                "has upset or frightened you."
            ),
            "module": "Harmful Content and Reporting",
        },
    ]

    for topic in safety_topics:
        if any(keyword in message for keyword in topic["keywords"]):
            return {
                "reply": topic["reply"],
                "module": topic["module"],
                "category": topic["category"],
            }

    if any(
        greeting in message
        for greeting in ["hello", "hi", "hey", "good morning", "good afternoon"]
    ):
        personalisation = ""

        if weakest_category:
            personalisation = (
                f" Your assessment suggests that {weakest_category} may be "
                "a useful area to review."
            )

        return {
            "reply": (
                "Hello! I am SafeBot, your online-safety coach. "
                "You can ask me about privacy, scams, passwords, "
                f"cyberbullying, fake profiles or unsafe contact.{personalisation}"
            ),
            "module": weakest_category,
            "category": "greeting",
        }

    return {
        "reply": (
            "I am designed to help with online safety and social media risks. "
            "Try asking me about privacy, phishing, scams, passwords, "
            "cyberbullying, fake profiles or someone making you feel "
            "uncomfortable online."
        ),
        "module": weakest_category,
        "category": "general",
    }