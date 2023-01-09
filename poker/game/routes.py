#!/usr/bin/python3
"""Routes for player to play game"""
from poker.game.card import Card
from poker.game.deck import Deck
from poker.game.game_round import GameRound
from poker.game.hand import Hand
from poker.game.player import Player

from flask_login import current_user, login_required
from poker import db
from poker.models import Game
from poker.game.forms import GameForm
from flask import render_template, Blueprint, flash, url_for, redirect, abort, request

games = Blueprint('games', __name__)

@games.route("/game")
@login_required
def start_game():
    """
    Load start game page
    """
    deck = Deck()
    cards = Card.create_standard_52_cards()
    deck.add_cards(cards)
    card = [str(card) for card in cards]
    card_string = "and".join(card)
    cards_list = str(card_string).split("and")
    cards_list_a, cards_list_c = split_list(cards_list)
    cards_list_b, cards_list_d = split_list(cards_list_c)
    return render_template("start_game.html", cards_list_b=cards_list_b)

@games.route("/game/<string:username>", methods=['GET', 'POST'])
@login_required
def show_cards(username):
    """
    Play game page, show cards received, show winning cards,
    show winner.
    """
    deck = Deck()
    cards = Card.create_standard_52_cards()
    deck.add_cards(cards)
    hand1 = Hand()
    hand2 = Hand()
    current_user.username = username
    player1 = Player(name = "Bot", hand = hand1)
    player2 = Player(name = username, hand = hand2)
    players = [player1, player2]
    game_round = GameRound(deck = deck, players = players)
    game_round.play()

    form = GameForm()
    return render_template("create_game.html", form=form, players=players)

def split_list(a_list):
    """
    split a list into two lists
    """
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

@games.route("/game/history")
def game_history():
    """Show game history
    """
    return redirect(url_for('main.home'))
@games.route("/quit")
def quit():
    """
    Quit game nd return to start game page
    """
    return redirect(url_for('games.start_game'))

def hand_list(player_hand):
    """
    Jinja2 Custom filter to convert players' hand to a list of cards
    """
    return str(player_hand).split(", ")
games.add_app_template_filter(hand_list, name=None)

def best_hand_cards(hand_cards):
    """
    Jinja2 Custom filter to convert players' best hand to a list of cards
    """
    hand_cards_strings = [str(card) for card in hand_cards]
    hand_cards_string = "and".join(hand_cards_strings)
    return str(hand_cards_string).split("and")
games.add_app_template_filter(best_hand_cards, name=None)