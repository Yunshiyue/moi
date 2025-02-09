import taichi as ti
ti.init(arch=ti.cuda)

from algorithm.LBM import LBMSolver

solver = LBMSolver(tau=0.57, res=(64, 64, 64), gravity=(0.0, 0.0, -0.0007), smag_constant=0.04)
solver.init_scene()
solver.simulate(2000.0)
