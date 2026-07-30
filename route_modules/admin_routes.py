from flask import render_template
from flask_login import login_required

from extensions import db
from models import (
    AssessmentResult,
    ModuleProgress,
    User,
    UserEvaluation,
)
from route_modules.decorators import admin_required


def register_admin_routes(app):

    @app.route("/admin")
    @login_required
    @admin_required
    def admin_dashboard():
        # ----------------------------------
        # Main dashboard statistics
        # ----------------------------------

        total_users = User.query.count()

        total_assessments = AssessmentResult.query.count()

        total_modules_completed = (
            ModuleProgress.query
            .filter_by(completed=True)
            .count()
        )

        total_evaluations = UserEvaluation.query.count()

        # ----------------------------------
        # Average statistics
        # ----------------------------------

        average_xp = (
            db.session.query(
                db.func.avg(User.xp)
            ).scalar()
            or 0
        )

        average_score = (
            db.session.query(
                db.func.avg(
                    AssessmentResult.percentage
                )
            ).scalar()
            or 0
        )

        highest_score = (
            db.session.query(
                db.func.max(
                    AssessmentResult.percentage
                )
            ).scalar()
            or 0
        )

        lowest_score = (
            db.session.query(
                db.func.min(
                    AssessmentResult.percentage
                )
            ).scalar()
            or 0
        )

        average_rating = (
            db.session.query(
                db.func.avg(
                    UserEvaluation.overall_satisfaction
                )
            ).scalar()
            or 0
        )

        # ----------------------------------
        # Category performance
        # ----------------------------------

        category_results = (
            db.session.query(
                AssessmentResult.category,
                db.func.avg(
                    AssessmentResult.percentage
                ).label("average_percentage"),
                db.func.count(
                    AssessmentResult.id
                ).label("assessment_count"),
            )
            .group_by(
                AssessmentResult.category
            )
            .order_by(
                db.func.avg(
                    AssessmentResult.percentage
                ).asc()
            )
            .all()
        )

        category_labels = [
            result.category
            for result in category_results
        ]

        category_scores = [
            round(
                float(result.average_percentage),
                1,
            )
            for result in category_results
        ]

        category_counts = [
            result.assessment_count
            for result in category_results
        ]

        # The category with the lowest average score
        # is treated as the most difficult category.

        most_difficult_category = None
        most_difficult_category_score = 0

        if category_results:
            most_difficult_result = category_results[0]

            most_difficult_category = (
                most_difficult_result.category
            )

            most_difficult_category_score = round(
                float(
                    most_difficult_result.average_percentage
                ),
                1,
            )

        # ----------------------------------
        # Module completion analytics
        # ----------------------------------

        module_results = (
            db.session.query(
                ModuleProgress.module_name,
                db.func.count(
                    ModuleProgress.id
                ).label("completion_count"),
            )
            .filter(
                ModuleProgress.completed.is_(True)
            )
            .group_by(
                ModuleProgress.module_name
            )
            .order_by(
                db.func.count(
                    ModuleProgress.id
                ).desc()
            )
            .all()
        )

        module_labels = [
            result.module_name
            for result in module_results
        ]

        module_counts = [
            result.completion_count
            for result in module_results
        ]

        most_completed_module = None
        most_completed_module_count = 0

        if module_results:
            most_completed_result = module_results[0]

            most_completed_module = (
                most_completed_result.module_name
            )

            most_completed_module_count = (
                most_completed_result.completion_count
            )

        # ----------------------------------
        # Evaluation analytics
        # ----------------------------------

        evaluation_completion_rate = 0

        if total_users > 0:
            evaluation_completion_rate = round(
                (
                    total_evaluations
                    / total_users
                )
                * 100,
                1,
            )

        # ----------------------------------
        # Recent users
        # ----------------------------------

        recent_users = (
            User.query
            .order_by(User.id.desc())
            .limit(5)
            .all()
        )

        # ----------------------------------
        # Recent assessments
        # ----------------------------------

        recent_assessments = (
            AssessmentResult.query
            .order_by(
                AssessmentResult.date_completed.desc()
            )
            .limit(5)
            .all()
        )

        # ----------------------------------
        # Awareness distribution
        # ----------------------------------

        strong_awareness_count = (
            AssessmentResult.query
            .filter(
                AssessmentResult.percentage >= 80
            )
            .count()
        )

        developing_awareness_count = (
            AssessmentResult.query
            .filter(
                AssessmentResult.percentage >= 60,
                AssessmentResult.percentage < 80,
            )
            .count()
        )

        support_recommended_count = (
            AssessmentResult.query
            .filter(
                AssessmentResult.percentage < 60
            )
            .count()
        )

        awareness_distribution_labels = [
            "Strong awareness",
            "Developing awareness",
            "Support recommended",
        ]

        awareness_distribution_values = [
            strong_awareness_count,
            developing_awareness_count,
            support_recommended_count,
        ]

        # ----------------------------------
        # Render dashboard
        # ----------------------------------

        return render_template(
            "admin_dashboard.html",

            total_users=total_users,
            total_assessments=total_assessments,
            total_modules=total_modules_completed,
            total_evaluations=total_evaluations,

            average_xp=round(
                float(average_xp)
            ),

            average_score=round(
                float(average_score),
                1,
            ),

            highest_score=round(
                float(highest_score),
                1,
            ),

            lowest_score=round(
                float(lowest_score),
                1,
            ),

            average_rating=round(
                float(average_rating),
                1,
            ),

            category_labels=category_labels,
            category_scores=category_scores,
            category_counts=category_counts,

            most_difficult_category=(
                most_difficult_category
            ),

            most_difficult_category_score=(
                most_difficult_category_score
            ),

            module_labels=module_labels,
            module_counts=module_counts,

            most_completed_module=(
                most_completed_module
            ),

            most_completed_module_count=(
                most_completed_module_count
            ),

            evaluation_completion_rate=(
                evaluation_completion_rate
            ),

            recent_users=recent_users,
            recent_assessments=recent_assessments,

            awareness_distribution_labels=(
                awareness_distribution_labels
            ),

            awareness_distribution_values=(
                awareness_distribution_values
            ),
        )