# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

from ..base_optimizer import BaseOptimizer
from ..base_positioner import BasePositioner


class HillClimbingOptimizer(BaseOptimizer):
    def __init__(self, init_positions, space_dim, opt_para):
        super().__init__(init_positions, space_dim, opt_para)

    def init_pos(self, nth_init):
        pos_new = self._base_init_pos(
            nth_init, HillClimbingPositioner(self.space_dim, self._opt_args_)
        )

        return pos_new

    def iterate(self, nth_iter):
        self._base_iterate(nth_iter)
        pos = self.p_current.move_climb(self.p_current.pos_current)

        return pos

    def evaluate(self, score_new):
        self._evaluate_new2best(score_new)

        if self.nth_iter % self._opt_args_.n_neighbours == 0:
            self.p_current.score_current = self.p_current.score_best
            self.p_current.pos_current = self.p_current.pos_best


class HillClimbingPositioner(BasePositioner):
    def __init__(self, space_dim, _opt_args_):
        super().__init__(space_dim, _opt_args_)

        self.epsilon = _opt_args_.epsilon
        self.distribution = _opt_args_.distribution
