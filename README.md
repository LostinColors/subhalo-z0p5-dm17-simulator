# Subhalo DM-17 Matter Simulation

This repository contains a numerical simulation of particle evolution inside the dark-matter subhalo **DM-17 at redshift z = 0.5**. The project includes both Python and Julia implementations of the same physical model, using a shared text file for initial particle data.

## Description

The simulation loads particle positions and velocities from `initial_data.txt`.
Two implementations are provided:

* **Python (`simulate.py`)** — uses NumPy and Matplotlib
* **Julia (`simulate.jl`)** — uses DelimitedFiles and Plots

Both versions follow equivalent logic, allowing easy comparison of performance and numerical behavior.

## Running the Simulation

### Python Version

```
python simulate.py
```

### Julia Version

```
julia simulate.jl
```

Both scripts automatically read `initial_data.txt` from the repository directory.

## Initial Data Format

The expected structure of `initial_data.txt` depends on the code, but a typical format is:

```
x   y   z   vx   vy   vz
...
```

Each row represents a particle with initial phase-space coordinates.

## Requirements

### Python

Required packages:

```
numpy
matplotlib
```

Install them via:

```
conda install numpy matplotlib
```

### Julia

Required packages:

```
DelimitedFiles   # standard library
Plots            # external package
```

Install Plots with:

```julia
add Plots
```
