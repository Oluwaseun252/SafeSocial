from flask import render_template
from flask_login import current_user, login_required

from models import AssessmentResult, UserEvaluation


def register_dashboard_routes(app):

    @app.route("/dashboard")
    @login_required
    def dashboard():
        all_results = (
            AssessmentResult.query
            .filter_by(user_id=current_user.id)
            .order_by(AssessmentResult.date_completed.asc())
            .all()
        )

        latest_results = all_results[-5:]

        recommended_category = None
        strongest_category = None
        highest_risk_score = 0
        strongest_score = 0
        overall_awareness_score = 0

        category_scores = {}
        recent_activity = []

        if all_results:
            # Keep only the latest result for each category.
            for result in all_results:
                category_scores[result.category] = result

            category_results = list(category_scores.values())

            recommended_result = min(
                category_results,
                key=lambda result: result.percentage,
            )

            strongest_result = max(
                category_results,
                key=lambda result: result.percentage,
            )

            recommended_category = recommended_result.category
            strongest_category = strongest_result.category

            highest_risk_score = round(
                100 - recommended_result.percentage
            )

            strongest_score = round(
                strongest_result.percentage
            )

            overall_awareness_score = round(
                sum(
                    result.percentage
                    for result in category_results
                )
                / len(category_results)
            )

            recent_activity = list(
                reversed(all_results[-3:])
            )

        evaluation = UserEvaluation.query.filter_by(
            user_id=current_user.id
        ).first()

        completed_modules = (
            current_user.completed_modules or 0
        )

        current_xp = current_user.xp or 0
        current_level = current_user.level or 1

        xp_per_level = 100
        xp_in_current_level = current_xp % xp_per_level

        xp_to_next_level = (
            xp_per_level - xp_in_current_level
        )

        xp_progress_percentage = round(
            (xp_in_current_level / xp_per_level) * 100
        )

        total_categories = len(category_scores)

        journey_steps_completed = 0

        if all_results:
            journey_steps_completed += 1

        if recommended_category:
            journey_steps_completed += 1

        if completed_modules > 0:
            journey_steps_completed += 1

        if evaluation:
            journey_steps_completed += 1

        journey_progress = round(
            (journey_steps_completed / 4) * 100
        )

        if not all_results:
            safety_status = "Assessment not started"

            safety_status_message = (
                "Complete the AI assessment to receive your "
                "personalised safety profile."
            )

        elif overall_awareness_score >= 80:
            safety_status = "Strong awareness"

            safety_status_message = (
                "You are demonstrating strong awareness of "
                "social media risks. Continue practising safe "
                "online decisions."
            )

        elif overall_awareness_score >= 60:
            safety_status = "Developing awareness"

            safety_status_message = (
                "Your awareness is improving. Complete the "
                "recommended challenge to strengthen your "
                "weaker areas."
            )

        else:
            safety_status = "Support recommended"

            safety_status_message = (
                "Your results show areas that need more support. "
                "Begin with your personalised learning "
                "recommendation."
            )

        # AI personalised recommendation

        if not category_scores:
            ai_recommendation = (
                "Complete your first assessment so SafeSocial "
                "can generate a personalised learning pathway."
            )

        else:
            weakest_category = min(
                category_scores,
                key=lambda category: (
                    category_scores[category].percentage
                ),
            )

            weakest_score = (
                category_scores[weakest_category].percentage
            )

            recommended_category = weakest_category

            if weakest_score < 40:
                ai_recommendation = (
                    f"You are currently at high risk in "
                    f"{weakest_category}. We strongly recommend "
                    f"completing this learning module before "
                    f"taking another assessment."
                )

            elif weakest_score < 70:
                ai_recommendation = (
                    f"You have a moderate understanding of "
                    f"{weakest_category}. Completing the "
                    f"recommended learning module will strengthen "
                    f"your online safety skills."
                )

            else:
                ai_recommendation = (
                    f"Your understanding of {weakest_category} "
                    f"is currently strong. Continue completing "
                    f"additional modules to maintain and improve "
                    f"your online safety awareness."
                )

        unlocked_achievements = 0

        if all_results:
            unlocked_achievements += 1

        if completed_modules >= 1:
            unlocked_achievements += 1

        if completed_modules >= 3:
            unlocked_achievements += 1

        if overall_awareness_score >= 80:
            unlocked_achievements += 1

        total_achievements = 4

        achievement_progress = round(
            (
                unlocked_achievements
                / total_achievements
            )
            * 100
        )

        return render_template(
            "dashboard.html",
            latest_results=latest_results,
            recent_activity=recent_activity,
            recommended_category=recommended_category,
            strongest_category=strongest_category,
            highest_risk_score=highest_risk_score,
            strongest_score=strongest_score,
            overall_awareness_score=(
                overall_awareness_score
            ),
            category_scores=category_scores,
            total_categories=total_categories,
            evaluation=evaluation,
            completed_modules=completed_modules,
            current_xp=current_xp,
            current_level=current_level,
            xp_in_current_level=xp_in_current_level,
            xp_to_next_level=xp_to_next_level,
            xp_progress_percentage=(
                xp_progress_percentage
            ),
            journey_steps_completed=(
                journey_steps_completed
            ),
            journey_progress=journey_progress,
            safety_status=safety_status,
            safety_status_message=(
                safety_status_message
            ),
            ai_recommendation=ai_recommendation,
            unlocked_achievements=(
                unlocked_achievements
            ),
            total_achievements=total_achievements,
            achievement_progress=(
                achievement_progress
            ),
        )