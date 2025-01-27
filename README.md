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
   Execute the integrated evolutionary algorithm by running the main Python script:
   ```bash
   python exam_scheduler.py

4. **Adjust Algorithm Parameters** *(Optional)*:
   Modify parameters for both the scheduling and meta-evolutionary algorithms directly in the script to optimize the process:
   - **Meta-Evolutionary Parameters**:
     - `tamanoPoblacion`: Number of parameter sets in each generation.
     - `numeroGeneraciones`: Maximum number of iterations before convergence.
     - `varianzaLimite`: Convergence threshold for parameter optimization.
     - `probamutacion`: Probability of mutating parameter sets during evolution.
   - **Scheduling Algorithm Parameters**:
     - **Penalty Weights**:
       - `pesoH`: Penalizes scheduling exams at undesirable times (e.g., early morning or lunchtime).
       - `pesoC`: Penalizes assigning exams to undersized rooms.
       - `pesoE`: Penalizes overlapping exams in the same room and time slot.
       - `pesoA`: Penalizes scheduling conflicts that prevent students from attending their exams.
     - `Population Size`: Number of candidate schedules in each generation.
     - `Mutation Probability`: Likelihood of introducing random variations to candidate schedules.

5. **Export Results**:
   Once the script completes, it generates the following CSV files in the repository directory:
   - **`ResultadosMejoresParams.csv`**: Contains the best parameter sets identified during meta-evolutionary optimization.
   - **`Parametros_Resultados.csv`**: Logs all evaluated parameter configurations.
   - **`Calificaciones_Resultados.csv`**: Includes scores, execution times, and errors for the best solutions.
   - **Final Exam Schedules**: The most optimized exam schedules are saved for review and implementation.

6. **Review Results and Refer to the Manual** *(Optional)*:
   - Open the generated CSV files to review:
     - The optimized parameters and their performance metrics.
     - Final exam schedules produced by the algorithm.
     - Errors and areas for improvement.
   - For detailed guidance on the algorithms and their functions, consult the **Manual de Usuario** included in the project itself. It provides in-depth explanations of key functions, parameters, and use cases.

### Notes and Limitations
- The scheduling system employs **evolutionary algorithms** and a **meta-evolutionary approach** to optimize both schedules and parameter sets. Results are approximate and may not guarantee a globally optimal solution.
- The algorithms are designed for the provided dataset structure. Using different datasets or modifying the CSV file formats (`salones.csv`, `materias.csv`, `alumnos.csv`) without updating the script may result in errors.
- The **meta-evolutionary algorithm** can be computationally intensive, especially with large populations or datasets, and may require significant processing time.
- Parameter tuning, such as population size, mutation probability, and penalty weights, has a significant impact on performance. Experimentation is recommended to find the best configuration for specific datasets.
- The algorithms rely on heuristics for fitness evaluation, which means that minor adjustments to the weights can lead to different scheduling results or parameter optimizations.
- Convergence of the meta-evolutionary algorithm may vary depending on the `varianzaLimite`. Premature convergence or prolonged execution may occur if parameters are not balanced.
- Refer to the **Manual de Usuario** included in the python file for detailed explanations of the algorithms, parameters, and troubleshooting tips.
