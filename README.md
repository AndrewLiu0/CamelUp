# 🐪 Camel Up Game

A Python implementation of the popular board game Camel Up, featuring AI-powered betting advice and a colorful terminal-based interface.

## 🎮 Game Overview

Camel Up is a betting and racing game where players try to earn coins by betting on camel races. The game consists of multiple legs, with five colored camels (green, yellow, red, blue, and purple) racing around a 16-space track.

### Key Features:
- Terminal-based colorful interface using `colorama`
- AI-powered betting advice with Expected Value (EV) calculations
- Support for 2 players
- Multiple betting strategies
- Stacking camels mechanics
- Persistent camel positions between race legs

## 🎲 Game Mechanics

### Camel Movement
- Camels move based on dice rolls (1-3 spaces)
- Camels can stack on top of each other
- When a camel moves, it carries all camels on top of it
- The game ends when a camel crosses the finish line (space 16)

### Betting Options

Players have three main actions on their turn:

1. **Roll (R)**
   - Roll a random available die
   - Move the corresponding camel
   - Earn 1 coin for rolling

2. **Ticket (T)**
   - Bet on a camel to win the current leg
   - Available tickets: 5, 3, 2, 2 (in descending order)
   - Points awarded based on final positions:
     - 1st place: Ticket value
     - 2nd place: 1 point
     - 3rd-5th place: -1 point

3. **Overall Bet (B)**
   - Bet on a camel to win or lose the entire race
   - Points awarded based on betting order:
     1. 8 points
     2. 5 points
     3. 3 points
     4. 2 points
     5. 1 point
   - Incorrect bets: -1 point

## 🤖 AI Advice System

The game includes an AI advisor that calculates:
- Probability of each camel finishing 1st or 2nd
- Expected Value (EV) for betting tickets
- Recommendations for optimal betting strategies

You can enable automatic AI advice or request it only when making ticket bets.

### AI Display Format
```
AI Advice-
   1st   2nd
g  0.25  0.30
y  0.15  0.25
r  0.20  0.15
b  0.30  0.20
p  0.10  0.10
```

## 🎨 Visual Interface

The game features a colorful terminal interface showing:
- Track with stacked camels
- Available betting tickets
- Dice roll history
- Player scores and bets
- Position numbers (1-16)

Example display:
```
🌴                 g     y r   b p           🏁
  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
```

## 🎯 Scoring

- Players earn/lose coins through betting tickets
- Rolling dice earns 1 coin
- Final scores combine:
  - Leg betting results
  - Overall race betting results
  - Coins from dice rolls

## 🚀 Installation

1. Clone the repository
2. Install required packages:
```bash
pip install colorama
```

## 🎮 How to Play

1. Run the game:
```bash
python main.py
```

2. Choose AI advice mode:
   - `y`: Automatic advice every turn
   - `n`: Advice only when betting tickets

3. Follow the prompts to:
   - Choose actions (R/T/B)
   - Place bets
   - Roll dice

## 📦 Project Structure

- `main.py`: Game loop and main logic
- `camel_up.py`: Game state management
- `display.py`: Terminal interface rendering
- `expected_value.py`: AI betting calculations
- `tent.py`: Dice rolling mechanics

## 🎪 Game End

The game ends when a camel crosses space 16. Final scores are calculated including:
- All leg results
- Overall winner/loser bets
- Total coins earned

The player with the most coins wins! 🏆
