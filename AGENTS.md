# AGENTS.md

Guidance for AI coding agents working in this repository. `CLAUDE.md` only imports
this file; put all agent instructions here, not in `CLAUDE.md`.

## Project

Educational 2D LiDAR SLAM tutorials, built up step by step. The curriculum and
background concepts live in [docs/slam_tutorials_readme.md](docs/slam_tutorials_readme.md):

1. Scan-to-scan matching (brute force / correlation)
2. Scan-to-map integration against an occupancy grid
3. Optimization (non-linear least squares, e.g. Gauss-Newton)
4. ICP (point-to-point and point-to-line)

New tutorial steps should follow this order and build on earlier steps.

## Environment

- Python 3.12 in a local virtualenv at `.venv/` (gitignored).
- Dependencies are listed in `requirements.txt` (`numpy`, `matplotlib`,
  `scipy`, `jupyter`, `ipywidgets`). Keep the list minimal. When a change
  needs a new package, add it to `requirements.txt` **and** install it into
  the venv with `.venv/bin/pip install -r requirements.txt`.

```sh
source .venv/bin/activate
pip install -r requirements.txt
python src/synthetic_scan_matching_step_1.py   # run a script
jupyter lab notebooks/                         # open the notebooks
```

There is no test suite, linter, or build step yet. Before committing a
notebook, run it top to bottom (e.g. `jupyter execute notebooks/<name>.ipynb`)
to make sure every cell executes.

## Code layout and conventions

- The curriculum in [docs/icp_curriculum.md](docs/icp_curriculum.md) is the
  plan; each module lists the notebooks and scripts that belong to it.
- Tutorial notebooks live in `notebooks/`, named `<module><letter>_<topic>.ipynb`
  (e.g. `1a_polar_to_cartesian.ipynb`). Each notebook opens with a title,
  a short motivation, and a "Learning goals" list, alternates markdown
  explanation with short code cells, and ends with a "Summary" and a
  pointer to the next step. Commit notebooks with outputs cleared.
- Tutorial scripts live in `src/` as standalone, runnable files named
  `<topic>_step_<n>.py` (e.g. `synthetic_scan_matching_step_1.py`).
- Each script and notebook is self-contained (helpers such as the synthetic
  LiDAR simulator are copied in rather than imported): small functions with
  docstrings, then a main block that generates synthetic data, runs the
  algorithm, prints true vs. estimated values, and visualizes with matplotlib.
- Scans are `numpy` arrays of shape `(N, 2)` holding Cartesian `(x, y)` points
  in meters, in the robot frame.
- Frame convention: robot motion `(+dx, +dy)` shifts observed points by
  `(-dx, -dy)`; a scan match returns the translation that maps the new scan
  back onto the reference.
- Favor clarity over performance — these are teaching materials. Explicit loops
  and plain numpy are preferred over opaque vectorization or library calls when
  they make the algorithm easier to follow.
