# 🐍 TurboSnake

**TurboSnake** is a modern take on the classic Snake game, built entirely with Python using the `turtle` graphics module. It’s a simple yet engaging project showcasing real-time input handling, object-oriented programming, and game loop mechanics.


## 🎮 Features

- Modular codebase using OOP principles (`Snake`, `Food`, and `Scoreboard` classes)
- Smooth and responsive movement with arrow key controls
- Random food generation and snake body growth
- Dynamic difficulty — the snake speeds up every 10 points
- Collision detection with wall and self for game over condition

---

## 📦 Requirements

This game uses only built-in Python libraries, so no external packages are needed.

- Python 3.x
- turtle (comes pre-installed with Python)

---
## 🎮 Controls

| Key     | Action      |
|---------|-------------|
| `↑`     | Move Up     |
| `↓`     | Move Down   |
| `←`     | Move Left   |
| `→`     | Move Right  |

Use the arrow keys on your keyboard to control the snake's direction. Eat food to grow longer and earn points. Avoid the walls and your own body — or it's game over!

---

## 🧠 How It Works

### 🗂 Code Structure

- **`main.py`**  
  Initializes the game window, runs the main game loop, and handles input and collision logic.

- **`snake.py`**  
  Defines the `Snake` class:
  - Handles snake segment creation
  - Controls movement and direction
  - Adds new segments when food is eaten

- **`food.py`**  
  Defines the `Food` class:
  - Randomly places the food on screen
  - Inherits from `turtle.Turtle`

- **`scoreboard.py`**  
  Defines the `Scoreboard` class:
  - Displays the current score
  - Shows "Game Over" when the snake crashes

### ⏱ Dynamic Difficulty

As your score increases, the game gets harder:
- The snake moves faster every 10 points


## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/Ewwftyy/TurboSnake.git
cd TurboSnake
python main.py


