import numpy as np
from gradient_free_optimizers import RandomSearchOptimizer


def objective_function(pos_new):
    score = -pos_new[0] * pos_new[0]
    return score


search_space = [np.arange(-100, 101, 1)]


def test_initialize_warm_start():
    initialize = {"warm_start": [np.array([0])]}

    opt = RandomSearchOptimizer(search_space)
    opt.search(
        objective_function, n_iter=0, initialize=initialize,
    )

    assert abs(opt.best_score) < 0.001


def test_initialize_vertices():
    initialize = {"vertices": 2}

    opt = RandomSearchOptimizer(search_space)
    opt.search(
        objective_function, n_iter=0, initialize=initialize,
    )

    assert abs(opt.best_score) - 10000 < 0.001


def test_initialize_grid_0():
    search_space = [np.arange(-1, 2, 1)]
    initialize = {"grid": 1}

    opt = RandomSearchOptimizer(search_space)
    opt.search(
        objective_function, n_iter=0, initialize=initialize,
    )

    assert abs(opt.best_score) < 0.001


def test_initialize_grid_1():
    search_space = [np.arange(-2, 3, 1)]
    initialize = {"grid": 1}

    opt = RandomSearchOptimizer(search_space)
    opt.search(
        objective_function, n_iter=0, initialize=initialize,
    )

    assert abs(opt.best_score) - 1 < 0.001
