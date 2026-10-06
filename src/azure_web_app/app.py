from datetime import datetime

from flask import Flask, render_template

FAVORITES = [
    {"id": 1, "title": "Lionel Messi", "why": "His dribbling and playmaking."},
    {"id": 2, "title": "Cristiano Ronaldo", "why": "His goal-scoring ability."},
    {"id": 3, "title": "Neymar", "why": "His creativity and skill."},
]

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app


def index():
    current_hour = datetime.now().hour  # noqa: DTZ005
    return render_template(
        "index.html",
        name="CFERG",
        hobby="Soccer",
        hours_per_week=3,
        hour=current_hour,
        show_counter=True,
        fun_fact="I have played soccer for 14 years",
        favorites=FAVORITES,
    )


def setup_routes(app):
    app.route("/")(index)


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
