# src/poker_now_log_converter/__main__.py

import logging
from poker_now_log_converter.hand import Hand

def main():
    # Set up logging, parse command line arguments, etc.
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Assuming you have parsed the hand history and created a Hand object named `hand`
    hand = Hand()  # Replace this with your actual Hand object initialization

    # Format the hand as a PokerStars hand history with USD currency
    formatted_hand = hand.format_as_pokerstars_hand(currency="USD", currency_symbol="$", timezone="GMT")

    # Print or save the formatted hand history
    for line in formatted_hand:
        print(line)

if __name__ == "__main__":
    main()