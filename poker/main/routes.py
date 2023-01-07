#!/usr/bin/python3

from flask import render_template, request, Blueprint
from poker.models import Post
from poker.models import Game

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    Display home page
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    pokers = Game.query.order_by(Game.date_played.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, pokers=pokers)


@main.route("/about")
def about():
    """
    Display about us page
    """
    return render_template('about.html', title='About')
