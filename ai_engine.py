CATEGORY_EXPLANATIONS = {
    "Privacy and Oversharing": {
        "analysis": (
            "Your responses suggest that you may unintentionally share personal "
            "information on social media. Oversharing can expose your identity, "
            "location and personal details to strangers."
        ),
        "recommendation": (
            "Complete the Privacy and Oversharing Awareness Challenge."
        ),
    },
    "Cyberbullying": {
        "analysis": (
            "Your assessment indicates that you may find it difficult to recognise "
            "or respond appropriately to cyberbullying situations on social media."
        ),
        "recommendation": (
            "Complete the Cyberbullying Awareness Challenge."
        ),
    },
    "Online Grooming": {
        "analysis": (
            "Your responses indicate that you may not always recognise warning "
            "signs associated with online grooming and manipulative relationships."
        ),
        "recommendation": (
            "Complete the Online Grooming Awareness Challenge."
        ),
    },
    "Phishing and Scams": {
        "analysis": (
            "Your answers suggest that fraudulent messages and phishing attempts "
            "may be difficult for you to identify quickly."
        ),
        "recommendation": (
            "Complete the Phishing and Scams Awareness Challenge."
        ),
    },
    "Fake Profiles and Impersonation": {
        "analysis": (
            "Your assessment shows that fake accounts and impersonation attempts "
            "could be difficult for you to recognise."
        ),
        "recommendation": (
            "Complete the Fake Profiles and Impersonation Awareness Challenge."
        ),
    },
    "Misinformation": {
        "analysis": (
            "Your responses indicate that misleading information shared on social "
            "media could influence your decisions if it is not verified."
        ),
        "recommendation": (
            "Complete the Misinformation Awareness Challenge."
        ),
    },
    "Social Engineering": {
        "analysis": (
            "Your assessment suggests that you may be vulnerable to manipulation "
            "techniques used to obtain personal or account information."
        ),
        "recommendation": (
            "Complete the Social Engineering Awareness Challenge."
        ),
    },
    "Digital Footprint and Reputation": {
        "analysis": (
            "Your responses suggest that you may underestimate how social media "
            "posts can affect your long-term digital reputation."
        ),
        "recommendation": (
            "Complete the Digital Footprint and Reputation Awareness Challenge."
        ),
    },
}


def classify_risk(score):
    if score >= 90:
        return "Very Low Risk"
    elif score >= 75:
        return "Low Risk"
    elif score >= 60:
        return "Moderate Risk"
    elif score >= 40:
        return "High Risk"
    else:
        return "Very High Risk"


def generate_ai_report(category_scores, overall_score):
    if not category_scores:
        return {
            "overall_score": overall_score,
            "risk_level": classify_risk(overall_score),
            "highest_risk": "Not available",
            "strongest_area": "Not available",
            "analysis": "Complete the assessment to receive personalised analysis.",
            "recommendation": "Complete the social media awareness assessment.",
        }

    weakest_category = min(
        category_scores,
        key=category_scores.get,
    )

    strongest_category = max(
        category_scores,
        key=category_scores.get,
    )

    explanation = CATEGORY_EXPLANATIONS.get(
        weakest_category,
        {},
    )

    return {
        "overall_score": overall_score,
        "risk_level": classify_risk(overall_score),
        "highest_risk": weakest_category,
        "strongest_area": strongest_category,
        "analysis": explanation.get(
            "analysis",
            "Your responses have been analysed to identify areas requiring improvement.",
        ),
        "recommendation": explanation.get(
            "recommendation",
            "Continue completing social media awareness challenges.",
        ),
    }