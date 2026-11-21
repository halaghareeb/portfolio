"""Hala Ghareeb — portfolio website (Flask).

Run locally:
    pip install -r requirements.txt
    python app.py            # then open http://127.0.0.1:5000

Export a static copy (for GitHub Pages, Netlify, ...):
    python app.py freeze     # writes plain HTML files to ./build
"""
import sys
from datetime import date
from pathlib import Path
import os

from flask import Flask, render_template, url_for

import data

app = Flask(__name__)


@app.template_filter("asset")
def asset(path):
    """Turn a "/static/..." path into a proper URL (adds the /portfolio prefix on GitHub Pages).
    Full web addresses (https://...) are returned unchanged."""
    if path and path.startswith("/static/"):
        return url_for("static", filename=path[len("/static/"):])
    return path


@app.context_processor
def inject_globals():
    """Values available in every template."""
    return {
        "nav": data.NAV,
        "social": data.SOCIAL,
        "email": data.EMAIL,
        "year": date.today().year,
    }


@app.route("/")
def home():
    return render_template("index.html", title="Hala Ghareeb | Geospatial Engineer",
                           profile=data.PROFILE, education=data.EDUCATION, experience=data.EXPERIENCE, explore=data.EXPLORE)


@app.route("/solutions")
def solutions():
    return render_template("solutions.html", title="Solutions | Hala Ghareeb", solutions=data.SOLUTIONS)


@app.route("/dashboards")
def dashboards():
    return render_template("dashboards.html", title="Dashboards | Hala Ghareeb", dashboards=data.DASHBOARDS)


@app.route("/educational-projects")
def educational_projects():
    return render_template("educational_projects.html", title="Educational Projects | Hala Ghareeb",
                           projects=data.EDUCATIONAL_PROJECTS)


@app.route("/achievements")
def achievements():
    return render_template("achievements.html", title="Achievements | Hala Ghareeb",
                           achievements=data.ACHIEVEMENTS)


@app.route("/training-and-skills")
def training_and_skills():
    return render_template("training_and_skills.html", title="Training and Skills | Hala Ghareeb",
                           lidar=data.LIDAR, projects=data.TRAINING_PROJECTS)


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html", title="Page not found | Hala Ghareeb"), 404


def freeze(out_dir="build"):
    """Render every page to static HTML so the site can be hosted without Python."""
    import shutil

    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(Path(app.root_path) / "static", out / "static")

    # On GitHub Pages a project site lives under /<repo-name>/, so links must carry that prefix.
    base = os.environ.get("BASE_PATH", "").rstrip("/")
    base_url = f"http://localhost{base}/"

    client = app.test_client()
    routes = [r.rule for r in app.url_map.iter_rules() if r.endpoint != "static"]
    for rule in routes:
        html = client.get(rule, base_url=base_url).get_data(as_text=True)
        target = out / "index.html" if rule == "/" else out / rule.strip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print("wrote", target)
    (out / "404.html").write_text(
        client.get("/__missing__", base_url=base_url).get_data(as_text=True), encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        freeze()
    else:
        app.run(debug=True)
