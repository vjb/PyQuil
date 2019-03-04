from pyquil import Program
from pyquil.gates import *
from pyquil.api import WavefunctionSimulator

def ghz_state(qubits):
    """Create a GHZ state on the given list of qubits by applying
    a Hadamard gate to the first qubit followed by a chain of CNOTs
    """
    program = Program()
    program += H(qubits[0])
    for q1, q2 in zip(qubits, qubits[1:]):
        program += CNOT(q1, q2)
    return program

program = ghz_state(qubits=[0, 1, 2])
print(program)

wfn = WavefunctionSimulator().wavefunction(program)
print(wfn)