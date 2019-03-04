from pyquil import Program
from pyquil.gates import *
from pyquil.api import WavefunctionSimulator
from pyquil import get_qc
import numpy as np
from pyquil import list_quantum_computers


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

qc = get_qc('3q-qvm')
print(qc)

print(qc.qubits())


bitstrings = qc.run_and_measure(program, trials=10)

print(bitstrings)

bitstring_array = np.vstack(bitstrings[q] for q in qc.qubits()).T
sums = np.sum(bitstring_array, axis=1)

print(sums)

print(list_quantum_computers())


import networkx as nx
nx.draw(qc.qubit_topology())

from matplotlib import pyplot as plt
_ = plt.title('3q-qvm', fontsize=18)

plt.show()