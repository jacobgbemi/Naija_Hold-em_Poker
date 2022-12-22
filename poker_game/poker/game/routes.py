from poker.game.card import Card
from poker.game.deck import Deck
from poker.game.game_round import GameRound
from poker.game.hand import Hand
from poker.game.player import Player

from flask_login import current_user, login_required
from poker import db
from flask import render_template, Blueprint, flash, url_for, redirect
from poker.models import Game


games = Blueprint('games', __name__)

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

@games.route("/game")
def start_game():
    card = [str(card) for card in cards]
    card_string = "and".join(card)
    cards_list = str(card_string).split("and")
    cards_list_a, cards_list_b = split_list(cards_list)
    return render_template("start_game.html", cards_list_b=cards_list_b)

@games.route("/game/<string:username>", methods=['GET', 'POST'])
@login_required
def show_cards(username):
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
    
    # for player in players:
    #     hand_list = list(str(player.hand).split(", "))
        
        
        # index, hand_name, hand_cards = player.best_hand()
        # hand_cards_strings = [str(card) for card in hand_cards]
        # hand_cards_string = "and".join(hand_cards_strings)
        # hand_cards_list = str(hand_cards_string).split("and")
        # # # f"{player.name} has {hand_cards_list}"
        # for cardl_image in hand_list:
        #     cardl_image = url_for('static', filename='images/cards/' + cardl_image)
        
        # for handl_image in hand_cards_list:
        #         handl_image = url_for('static', filename='images/cards/' + handl_image)
    
    # winning_player = max(players)
    # winner = winning_player.name
    return render_template("create_game.html", players=players)

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

@games.route("/quit")
def quit():
    return redirect(url_for('games.start_game'))