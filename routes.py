from functools import wraps
from flask import (
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from ai_engine import generate_ai_report
from route_modules.dashboard_routes import (
    register_dashboard_routes,
)
from chatbot import get_safebot_response
from extensions import db
from learning_content import LEARNING_CONTENT
from models import (
    AssessmentResult,
    BehaviourReflection,
    ModuleProgress,
    Question,
    User,
    UserEvaluation,
)
from route_modules.admin_routes import register_admin_routes

def admin_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))

        if not current_user.is_admin:
            flash("You do not have permission to access that page.", "danger")
            return redirect(url_for("dashboard"))

        return function(*args, **kwargs)

    return decorated_function

def register_routes(app):
    register_dashboard_routes(app)
    register_admin_routes(app)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/chatbot", methods=["GET", "POST"])
    @login_required
    def chatbot():
        response = None
        user_message = ""
        weakest_category = None

        if request.method == "POST":
            user_message = request.form.get(
                "message",
                "",
            ).strip()

            response = get_safebot_response(
                user_message=user_message,
                weakest_category=weakest_category,
            )

        return render_template(
            "chatbot.html",
            response=response,
            user_message=user_message,
        )

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            if not username or not email or not password:
                flash("Please complete all fields.", "error")
                return redirect(url_for("register"))

            existing_user = User.query.filter(
                (User.username == username)
                | (User.email == email)
            ).first()

            if existing_user:
                flash(
                    "That username or email is already registered.",
                    "error",
                )
                return redirect(url_for("register"))

            user = User(
                username=username,
                email=email,
            )

            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            flash(
                "Registration successful. You can now log in.",
                "success",
            )

            return redirect(url_for("login"))

        return render_template("register.html")


    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            if not email or not password:
                flash(
                    "Please enter your email and password.",
                    "error",
                )
                return redirect(url_for("login"))

            user = User.query.filter_by(email=email).first()

            if user is None or not user.check_password(password):
                flash("Invalid email or password.", "error")
                return redirect(url_for("login"))

            login_user(user)

            flash("Login successful.", "success")
            return redirect(url_for("dashboard"))

        return render_template("login.html")



    @app.route("/modules")
    @login_required
    def learning_modules():
        completed_progress = ModuleProgress.query.filter_by(
            user_id=current_user.id,
            completed=True,
        ).all()

        completed_names = {
            progress.module_name
            for progress in completed_progress
        }

        return render_template(
            "learning_modules.html",
            learning_modules=LEARNING_CONTENT,
            completed_names=completed_names,
        )


    @app.route(
        "/module/<category>",
        methods=["GET", "POST"],
    )
    @login_required
    def learning_module(category):
        module = LEARNING_CONTENT.get(category)

        if module is None:
            flash(
                "That learning module could not be found.",
                "error",
            )
            return redirect(url_for("dashboard"))

        feedback = None
        answer_correct = None
        selected_option = None

        if request.method == "POST":
            selected_option = request.form.get("answer")

            if selected_option is None:
                flash("Please select an answer.", "error")
                return redirect(
                    url_for(
                        "learning_module",
                        category=category,
                    )
                )

            try:
                selected_option = int(selected_option)

            except (TypeError, ValueError):
                flash(
                    "Please select a valid answer.",
                    "error",
                )
                return redirect(
                    url_for(
                        "learning_module",
                        category=category,
                    )
                )

            correct_option = module["scenario"]["correct"]

            answer_correct = (
                selected_option == correct_option
            )

            feedback = module["scenario"]["feedback"]

            if answer_correct:
                existing_progress = (
                    ModuleProgress.query.filter_by(
                        user_id=current_user.id,
                        module_name=category,
                    ).first()
                )

                if existing_progress is None:
                    xp_reward = module["xp_reward"]

                    progress = ModuleProgress(
                        user_id=current_user.id,
                        module_name=category,
                        xp_awarded=xp_reward,
                        completed=True,
                    )

                    db.session.add(progress)

                    current_user.xp += xp_reward
                    current_user.completed_modules += 1

                    if current_user.xp >= 200:
                        current_user.level = 4

                    elif current_user.xp >= 100:
                        current_user.level = 3

                    elif current_user.xp >= 50:
                        current_user.level = 2

                    else:
                        current_user.level = 1

                    db.session.commit()

                    flash(
                        (
                            "Module completed! You earned "
                            f"{xp_reward} XP."
                        ),
                        "success",
                    )

                else:
                    flash(
                        (
                            "You have already completed this "
                            "module. No additional XP was awarded."
                        ),
                        "success",
                    )

        return render_template(
            "learning_module.html",
            module=module,
            category=category,
            feedback=feedback,
            answer_correct=answer_correct,
            selected_option=selected_option,
        )


    @app.route(
        "/reflection/<category>",
        methods=["GET", "POST"],
    )
    @login_required
    def behaviour_reflection(category):
        module = LEARNING_CONTENT.get(category)

        if module is None:
            flash(
                "That learning module could not be found.",
                "error",
            )
            return redirect(url_for("dashboard"))

        progress = ModuleProgress.query.filter_by(
            user_id=current_user.id,
            module_name=category,
            completed=True,
        ).first()

        if progress is None:
            flash(
                (
                    "Please complete the learning module "
                    "before reflecting."
                ),
                "error",
            )
            return redirect(
                url_for(
                    "learning_module",
                    category=category,
                )
            )

        existing_reflection = (
            BehaviourReflection.query.filter_by(
                user_id=current_user.id,
                module_name=category,
            ).first()
        )

        if request.method == "POST":
            confidence = request.form.get("confidence")

            safer_decision = request.form.get(
                "safer_decision"
            )

            key_learning = request.form.get(
                "key_learning",
                "",
            ).strip()

            if (
                not confidence
                or not safer_decision
                or not key_learning
            ):
                flash(
                    (
                        "Please complete all reflection "
                        "questions."
                    ),
                    "error",
                )
                return redirect(
                    url_for(
                        "behaviour_reflection",
                        category=category,
                    )
                )

            if existing_reflection:
                existing_reflection.confidence = confidence

                existing_reflection.safer_decision = (
                    safer_decision
                )

                existing_reflection.key_learning = (
                    key_learning
                )

            else:
                reflection = BehaviourReflection(
                    user_id=current_user.id,
                    module_name=category,
                    confidence=confidence,
                    safer_decision=safer_decision,
                    key_learning=key_learning,
                )

                db.session.add(reflection)

            db.session.commit()

            flash(
                "Thank you. Your reflection has been saved.",
                "success",
            )

            return redirect(url_for("dashboard"))

        return render_template(
            "behaviour_reflection.html",
            category=category,
            module=module,
            existing_reflection=existing_reflection,
        )


    @app.route(
        "/evaluation",
        methods=["GET", "POST"],
    )
    @login_required
    def user_evaluation():
        existing_evaluation = (
            UserEvaluation.query.filter_by(
                user_id=current_user.id
            ).first()
        )

        if request.method == "POST":
            try:
                learning_clarity = int(
                    request.form.get(
                        "learning_clarity",
                        0,
                    )
                )

                recommendation_usefulness = int(
                    request.form.get(
                        "recommendation_usefulness",
                        0,
                    )
                )

                scenario_engagement = int(
                    request.form.get(
                        "scenario_engagement",
                        0,
                    )
                )

                confidence_improvement = int(
                    request.form.get(
                        "confidence_improvement",
                        0,
                    )
                )

                overall_satisfaction = int(
                    request.form.get(
                        "overall_satisfaction",
                        0,
                    )
                )

            except (TypeError, ValueError):
                flash(
                    (
                        "Please provide a valid response "
                        "for every question."
                    ),
                    "error",
                )
                return redirect(
                    url_for("user_evaluation")
                )

            ratings = [
                learning_clarity,
                recommendation_usefulness,
                scenario_engagement,
                confidence_improvement,
                overall_satisfaction,
            ]

            if any(
                rating not in range(1, 6)
                for rating in ratings
            ):
                flash(
                    (
                        "Please answer every evaluation "
                        "question."
                    ),
                    "error",
                )
                return redirect(
                    url_for("user_evaluation")
                )

            suggestions = request.form.get(
                "suggestions",
                "",
            ).strip()

            if existing_evaluation:
                existing_evaluation.learning_clarity = (
                    learning_clarity
                )

                existing_evaluation.recommendation_usefulness = (
                    recommendation_usefulness
                )

                existing_evaluation.scenario_engagement = (
                    scenario_engagement
                )

                existing_evaluation.confidence_improvement = (
                    confidence_improvement
                )

                existing_evaluation.overall_satisfaction = (
                    overall_satisfaction
                )

                existing_evaluation.suggestions = suggestions

            else:
                evaluation = UserEvaluation(
                    user_id=current_user.id,
                    learning_clarity=learning_clarity,
                    recommendation_usefulness=(
                        recommendation_usefulness
                    ),
                    scenario_engagement=scenario_engagement,
                    confidence_improvement=(
                        confidence_improvement
                    ),
                    overall_satisfaction=(
                        overall_satisfaction
                    ),
                    suggestions=suggestions,
                )

                db.session.add(evaluation)

            db.session.commit()

            flash(
                (
                    "Thank you. Your evaluation has been "
                    "submitted."
                ),
                "success",
            )

            return redirect(url_for("dashboard"))

        return render_template(
            "user_evaluation.html",
            evaluation=existing_evaluation,
        )


    @app.route("/assessment",
        methods=["GET", "POST"],
    )
    @login_required
    def assessment():
        questions = Question.query.order_by(
            Question.id
        ).all()

        if not questions:
            flash(
                "No assessment questions are available.",
                "error",
            )
            return redirect(url_for("dashboard"))

        if request.method == "GET":
            session["assessment_index"] = 0
            session["assessment_answers"] = {}
            session["assessment_scores"] = {}
            session["assessment_saved"] = False

        question_index = session.get(
            "assessment_index",
            0,
        )

        if request.method == "POST":
            selected_answer = request.form.get("answer")
            question_id = request.form.get("question_id")

            if not selected_answer or not question_id:
                flash(
                    (
                        "Please select an answer before "
                        "continuing."
                    ),
                    "error",
                )
                return redirect(url_for("assessment"))

            try:
                question_id = int(question_id)

            except (TypeError, ValueError):
                flash(
                    "The selected question is invalid.",
                    "error",
                )
                return redirect(url_for("assessment"))

            current_question = db.session.get(
                Question,
                question_id,
            )

            if current_question is None:
                flash(
                    (
                        "The selected question could not "
                        "be found."
                    ),
                    "error",
                )
                return redirect(url_for("dashboard"))

            answers = session.get(
                "assessment_answers",
                {},
            )

            scores = session.get(
                "assessment_scores",
                {},
            )

            answers[str(current_question.id)] = (
                selected_answer
            )

            category = current_question.category

            if category not in scores:
                scores[category] = {
                    "correct": 0,
                    "total": 0,
                }

            scores[category]["total"] += 1

            if (
                selected_answer
                == current_question.correct_option
            ):
                scores[category]["correct"] += 1

            session["assessment_answers"] = answers
            session["assessment_scores"] = scores

            question_index += 1
            session["assessment_index"] = question_index

            if question_index >= len(questions):
                assessment_saved = session.get(
                    "assessment_saved",
                    False,
                )

                if not assessment_saved:
                    for category, result in scores.items():
                        percentage = round(
                            (
                                result["correct"]
                                / result["total"]
                            )
                            * 100,
                            1,
                        )

                        saved_result = AssessmentResult(
                            user_id=current_user.id,
                            category=category,
                            correct_answers=result["correct"],
                            total_questions=result["total"],
                            percentage=percentage,
                        )

                        db.session.add(saved_result)

                    db.session.commit()
                    session["assessment_saved"] = True

                return redirect(
                    url_for("assessment_results")
                )

        if question_index >= len(questions):
            return redirect(
                url_for("assessment_results")
            )

        current_question = questions[question_index]

        # Preserve the order in which categories first appear.
        category_order = list(
            dict.fromkeys(
                question.category
                for question in questions
            )
        )

        # Retrieve all questions in the current category.
        category_questions = [
            question
            for question in questions
            if question.category == current_question.category
        ]

        # Determine the question's position in its category.
        category_question_number = next(
            (
                index + 1
                for index, question in enumerate(
                    category_questions
                )
                if question.id == current_question.id
            ),
            1,
        )

        category_total_questions = len(
            category_questions
        )

        # Determine the category's position in the assessment.
        category_number = (
            category_order.index(
                current_question.category
            )
            + 1
        )

        total_categories = len(category_order)

        # Show the percentage of questions already completed.
        progress_percentage = int(
            (
                question_index
                / len(questions)
            )
            * 100
        )

        return render_template(
            "assessment.html",
            question=current_question,
            question_number=question_index + 1,
            total_questions=len(questions),
            progress_percentage=progress_percentage,
            category_question_number=(
                category_question_number
            ),
            category_total_questions=(
                category_total_questions
            ),
            category_number=category_number,
            total_categories=total_categories,
        )


    @app.route("/assessment/results")
    @login_required
    def assessment_results():
        scores = session.get(
            "assessment_scores",
            {},
        )

        if not scores:
            flash(
                "Please complete the assessment first.",
                "error",
            )
            return redirect(url_for("assessment"))

        results = []
        category_scores = {}

        total_correct = 0
        total_questions = 0

        for category, score in scores.items():
            correct = score["correct"]
            total = score["total"]

            percentage = round(
                (
                    correct
                    / total
                )
                * 100,
                1,
            )

            results.append(
                {
                    "category": category,
                    "correct": correct,
                    "total": total,
                    "percentage": percentage,
                }
            )

            category_scores[category] = percentage

            total_correct += correct
            total_questions += total

        overall_score = round(
            (
                total_correct
                / total_questions
            )
            * 100,
            1,
        )

        ai_report = generate_ai_report(
            category_scores=category_scores,
            overall_score=overall_score,
        )

        return render_template(
            "assessment_results.html",
            results=results,
            ai_report=ai_report,
        )


    @app.route("/logout")
    @login_required
    def logout():
        logout_user()

        flash(
            "You have been logged out.",
            "success",
        )

        return redirect(url_for("home"))

    