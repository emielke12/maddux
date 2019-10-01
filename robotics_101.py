#!/usr/bin/env python

from maddux.environment import Environment
from maddux.robots.arm import Arm
from maddux.robots.link import Link
import numpy as np

L1 = Link(0, 3.4, 0, np.pi/2)
L2 = Link(0, 0, 0, -np.pi/2)
L3 = Link(0, 4, 0, -np.pi/2)
L4 = Link(0, 0, 0, np.pi/2)
L5 = Link(0, 4, 0, np.pi/2)
L6 = Link(0, 0, 0, -np.pi/2)
L7 = Link(0, 1.26, 0, 0)
links = np.array([L1, L2, L3, L4, L5, L6, L7])

q0 = np.array([0,0,0,0,0,0,0])
r = Arm(links, q0, 'iiwa')
env = Environment(robot = r)
# q = np.array([np.pi/4,-np.pi/2,0,np.pi/2,0,np.pi/2,0])
# r.update_angles(q)

qf = r.ikine([1, 6, 6])
# b = env.animate(None, '/home/emielke/output.mp4')
r.update_angles(qf)
env.plot()
