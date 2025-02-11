# 🃏 Blackjack Game in Python

## 🎯 Overview
This is a **command-line Blackjack game** written in Python. The objective is to get as close to **21** as possible without going over, while playing against a dealer who follows standard house rules.

## 🚀 Features
- **Standard 52-card deck** (♠ ♥ ♣ ♦).
- **Betting system**: Start with **100 chips** and place bets before each round.
- **Game actions**:
  - `h` → Hit (Take another card)
  - `s` → Stand (Keep your current hand)
  - `d` → Deal (Start a new round)
  - `q` → Quit (Exit the game)
- **Dealer rules**:
  - Hits until reaching **17**.
  - **Busts if over 21**.
- **Game outcomes**:
  - Win if your hand is **closer to 21** than the dealer’s.
  - Lose if you **bust** or the dealer has a better hand.
  - Tie if you and the dealer have the **same value** (*push*).

## 🕹️ How to Play
1. **Run the game**:
   ```bash
   python blackjack.py
Place a bet.
Cards are dealt. Choose:
Hit (h) → Take another card.
Stand (s) → Keep your current hand.
Deal (d) → Start a new round.
Quit (q) → Exit the game.
Dealer plays automatically.
Win or lose, then repeat or quit.
🔧 Requirements
Python 3.x
No additional libraries needed (uses Python’s built-in random module).

## Welcome to BlackJack! 🎲
Get as close to 21 as possible without going over!

Enter your bet: 20

Player Hand: ♥A ♦9
Total: 20

Dealer Hand: ♠7 (with another card hidden)

Hit (h) or Stand (s)?
> s

## Dealer Hand: ♠7 ♣10  (Total: 17)
You win! Press d to deal again, or q to quit.
🛠️ Future Enhancements
✅ Add GUI support
✅ Implement split-hand feature
✅ Introduce doubling down

Enjoy the game! 🚀♠️♥️♣️♦️
