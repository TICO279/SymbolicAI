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

### Notes and Limitations
- The game uses a **minimax algorithm** with a fixed depth of search (`profundidadMaxima`), which may limit the AI's capability for deeper strategies in complex situations.
- The current implementation assumes valid user inputs. Invalid moves will prompt error messages and require re-entry.
- The AI's performance is optimized for local execution but may slow down with higher search depths.
- The script is designed for terminal-based interaction. A graphical user interface (GUI) is not provided.
- The algorithm heavily relies on heuristics, and any changes to these weights may significantly alter the AI’s behavior.

## Project 2: Optimizing Exam Scheduling with Evolutionary Algorithms

This project implements a **nested evolutionary algorithm** for solving the exam scheduling problem. The first algorithm optimizes exam assignments (rooms, times, and conflict resolution), while the second algorithm evolves parameters of the first to improve overall performance and results.

### Features
- **Primary Evolutionary Algorithm**:
  - Assigns exams to rooms and time slots while minimizing scheduling conflicts and penalties.
  - Penalizes undesirable conditions such as:
    - Overlapping exams for the same students.
    - Room capacity violations.
    - Scheduling exams during undesirable time slots (e.g., early morning, lunch hours).
  - Balances constraints to generate feasible exam schedules.

- **Meta-Evolutionary Algorithm**:
  - Evolves the parameters of the primary algorithm to improve its efficiency and quality of results.
  - Parameters optimized include:
    - Population size, number of generations, and mutation probability.
    - Penalty weights for constraints like room capacity, undesirable times, and exam overlaps.

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/SymbolicAI.git
   cd SymbolicAI/ExamScheduling

2. **Prepare Data**:
   Ensure CSV files (`salones.csv`, `materias.csv`, `alumnos.csv`) are present in the repository. These files contain:
   - **Room Capacities**: Each room's ID and seating capacity.
   - **Exam Registrations**: Number of students registered for each course exam.
   - **Student Preferences**: Exam schedules required by students.

3. **Run the Scheduler**:
   Execute the evolutionary algorithm by running the main Python script:
   ```bash
   python exam_scheduler.py

4. **Adjust Algorithm Parameters** *(Optional)*:
   You can modify the algorithm parameters in the script to optimize the scheduling process:
   - **Population Size**: Determines the number of candidate solutions in each generation.
   - **Mutation Probability**: Sets the likelihood of introducing random variations to the solutions.
   - **Penalty Weights**:
     - `pesoH`: Penalty for scheduling exams at undesirable times.
     - `pesoC`: Penalty for assigning exams to rooms with insufficient capacity.
     - `pesoE`: Penalty for overlapping exams in the same room and time slot.
     - `pesoA`: Penalty for scheduling exams that cause conflicts for students.

5. **Export Results**:
   After running the script, the results are automatically exported as CSV files in the repository directory:
   - `ResultadosMejoresParams.csv`: Stores the best parameters found during optimization.
   - `Parametros_Resultados.csv`: Contains parameter configurations used in successful runs.
   - `Calificaciones_Resultados.csv`: Includes fitness scores and errors for the best solutions identified.

### Notes and Limitations
- Ensure the CSV files (`salones.csv`, `materias.csv`, `alumnos.csv`) are correctly formatted and available in the repository before running the script.
- The algorithm's performance is sensitive to the population size and mutation probability, so experimentation with these parameters may be necessary.
- The script assumes a fixed dataset structure. Modifying the CSV structure without updating the script may result in errors.
- Solutions are optimized for the dataset provided and may require adjustments when applied to different datasets or institutions.
- Results are approximate and rely on heuristics, meaning they may not always yield the absolute optimal schedule.



