from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a single-qubit quantum circuit with one classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Apply Pauli-X gate
qc.x(0)

# Measure the qubit
qc.measure(0, 0)

# Display the quantum circuit
print("Quantum Circuit:")
print(qc)

# Create simulator
simulator = AerSimulator()

# Execute the circuit for 1000 shots
job = simulator.run(qc, shots=1000)

# Get measurement results
result = job.result()
counts = result.get_counts()

# Display measurement counts
print("\nMeasurement Counts:")
print(counts)