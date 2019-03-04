from pyquil import Program
from pyquil.gates import *
program = Program(
    H(0),
    CNOT(0, 1),
)
print(program)