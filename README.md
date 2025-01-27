# SymbolicAI

This repository contains two projects focused on Symbolic AI concepts. Each project implements a different AI algorithm.

## Project 1: Ultimate Tic-Tac-Toe Minimax Algorithm

This project demonstrates a Minimax-based AI for playing **Ultimate Tic-Tac-Toe**. It uses heuristic evaluation and advanced game-tree searching to make decisions in the game.

### Features
- Implements the **Minimax algorithm** with heuristic functions for decision-making.
- Evaluates multiple layers of nested Tic-Tac-Toe boards using:
  - Positional advantage heuristics (corners, centers).
  - Blocking opponent moves.
  - Maximizing future potential moves.
- Dynamic depth adjustment to optimize computation time.
- Handles special game rules, including:
  - Board redirection based on previous moves.
  - Free choice of boards in certain scenarios.
- A fully playable AI opponent that interacts through a text-based interface.

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/SymbolicAI.git
   cd SymbolicAI/Project1

2. **Install Dependencies**:  
   Ensure Python 3.x is installed. If additional dependencies are required, you can install them with:  
   ```bash
   pip install numpy

3. **Run the Game**:  
   Start the AI by executing the script:  
   ```bash
   python ultimate_tic_tac_toe.py

4. **Interact with the AI**:  
   Follow the on-screen instructions to play the game:  
   - Use inputs like `Aa` (e.g., `A1`, `H3`) to make your moves.  
   - Respond with `y` if the AI should start the game, or any other key for the opponent to start.  
   - Use `Ctrl+C` to quit the game at any point.

5. **Modify Heuristics** *(Optional)*:  
   The AI uses predefined weights for decision-making, such as `pesoGanarJuego` and `pesoAUnoDeLinea`.  
   You can fine-tune these values in the script to test and improve the AI’s performance.

## Notes and Limitations
- The game uses a **minimax algorithm** with a fixed depth of search (`profundidadMaxima`), which may limit the AI's capability for deeper strategies in complex situations.
- The current implementation assumes valid user inputs. Invalid moves will prompt error messages and require re-entry.
- The AI's performance is optimized for local execution but may slow down with higher search depths.
- The script is designed for terminal-based interaction. A graphical user interface (GUI) is not provided.
- The algorithm heavily relies on heuristics, and any changes to these weights may significantly alter the AI’s behavior.

