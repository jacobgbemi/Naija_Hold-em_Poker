from poker.game.card import Card
from poker.game.deck import Deck
from poker.game.game_round import GameRound
from poker.game.hand import Hand
from poker.game.player import Player

from flask_login import current_user, login_required
from poker import db
from poker.game.forms import GameForm
from flask import render_template, Blueprint, flash, url_for
from poker.models import Game

games = Blueprint('games', __name__)

@games.route("/game", methods=['GET', 'POST'])
@login_required
def show_cards():
    deck = Deck()
    cards = Card.create_standard_52_cards()
    deck.add_cards(cards)

    hand1 = Hand()
    hand2 = Hand()

    player1 = Player(name = "Bot", hand = hand1)
    player2 = Player(name = current_user.username, hand = hand2)
    players = [player1, player2]

    game_round = GameRound(deck = deck, players = players)
    game_round.play()
    
    
    for player in players:
        hand_list = str(player.hand).split(",")
        index, hand_name, hand_cards = player.best_hand()
        hand_cards_strings = [str(card) for card in hand_cards]
        hand_cards_string = " and ".join(hand_cards_strings)
        hand_cards_str = str(hand_cards_string).split("and")

    winning_player = max(players)
    winner = winning_player.name

    # form = GameForm()
    # if form.validate_on_submit():
    #     game = Game(winner=winning_player.name, author=current_user)
    #     db.session.add(game)
    #     db.session.commit()
    #     flash(f'{winner} has won', 'success')
    return render_template("create_game.html", players=players, hand_name=hand_name, hand_cards=hand_cards,
                            winner=winner, hand_list=hand_list, hand_cards_str=hand_cards_str, hand_cards_string= hand_cards_string)