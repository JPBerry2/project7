# CST-305 Project 7 — Code Errors and the Butterfly Effect

## Overview
This project implements the Lorenz System to model the butterfly effect in chaotic
dynamical systems, and applies M/M/1 queueing theory to analyze network gateway
and server performance.

## Requirements
- Python 3.8 or higher
- numpy
- matplotlib

## Installation
```bash
git clone https://github.com/[your-repo]/cst305-project7
cd cst305-project7
pip install -r requirements.txt
```

## Running the Program
```bash
python Project7.py
```

### Part 1 — Lorenz Attractor (interactive)
- At the prompt, enter a numeric value for rho (e.g. 10, 15, 28).
- Four plot windows open in sequence: 3D attractor, X, Y, Z time-series.
- Close each window to advance to the next plot.
- Enter as many rho values as desired.
- Type 'n' and press Enter to proceed to Part 2.

### Part 2 — Queueing Theory (automatic)
- Runs automatically after exiting Part 1.
- Prints M/M/1 gateway analysis to the console.
- Displays four sequential plots (a–d) for the scaling analysis.

## File Structure
```
├── Project7.py      # Main program (Part 1 + Part 2)
├── requirements.txt # Python dependencies
└── README.md
```
