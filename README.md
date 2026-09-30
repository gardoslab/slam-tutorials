# slam-tutorials

Hands-on tutorials for 2D LiDAR SLAM, built up from first principles: converting
raw LiDAR readings to points, transforming and matching scans, optimization, and
Iterative Closest Point (ICP). Everything runs on synthetic data in plain NumPy
and matplotlib, so each algorithm can be checked against a known answer.

## Where to start

1. Read [docs/slam_tutorials_readme.md](docs/slam_tutorials_readme.md) for the
   background concepts: polar data, coordinate transforms, occupancy grids, and
   why scan matching is needed.
2. Follow [docs/icp_curriculum.md](docs/icp_curriculum.md) for the module-by-module
   plan. Each module links the notebooks and scripts that go with it.
3. Work through the notebooks in order:

   | Notebook | Topic |
   |---|---|
   | [1a_polar_to_cartesian](notebooks/1a_polar_to_cartesian.ipynb) | Turning LiDAR rays into `(x, y)` points |
   | [1b_matrix_transforms](notebooks/1b_matrix_transforms.ipynb) | Translating and rotating scans with homogeneous transforms |
   | [2b_cost_function_surface](notebooks/2b_cost_function_surface.ipynb) | Visualizing the alignment error as a surface |
   | [3a_gradient_descent_toy](notebooks/3a_gradient_descent_toy.ipynb) | Gradient descent, from toy problems to scan matching |
   | [4a_nearest_neighbors_kdtree](notebooks/4a_nearest_neighbors_kdtree.ipynb) | Finding point correspondences with a KD-tree |
   | [5a_the_corridor_problem](notebooks/5a_the_corridor_problem.ipynb) | Why point-to-point ICP fails in a corridor |

## Repository layout

```
docs/        Background reading and the curriculum
notebooks/   Interactive tutorial notebooks (Jupyter)
src/         Standalone tutorial scripts
AGENTS.md    Conventions for contributors and AI coding agents
```

## Setup

You need Python 3.12 or newer. Create a virtual environment in `.venv/` (it is
gitignored) and install the dependencies into it:

```sh
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run `source .venv/bin/activate` again in each new terminal before working in the repo.
To leave the environment, run `deactivate`.

## Running the tutorials

Open the notebooks in JupyterLab:

```sh
jupyter lab notebooks/
```

If you use VS Code, open a notebook and pick the `.venv` interpreter as its kernel.

Run a script directly:

```sh
python src/synthetic_scan_matching_step_1.py
```

## Contributing

See [AGENTS.md](AGENTS.md) for naming and structure conventions, and for how
to add dependencies.

## License

[MIT](LICENSE)
