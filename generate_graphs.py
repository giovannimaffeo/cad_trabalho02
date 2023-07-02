import subprocess
import re
import time
import matplotlib.pyplot as plt

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate()
    return output

def run_jacobi(norder, iterations):
    command = f"./jacobi --norder {norder} --iterations {iterations} --convergence 0.0001"
    start_time = time.time()
    output = run_command(command)
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

def run_jacobi_optimized(norder, iterations):
    command = f"./jacobi_optimized --norder {norder} --iterations {iterations} --convergence 0.0001"
    start_time = time.time()
    output = run_command(command)
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

def run_jacobi_profiled(norder, iterations):
    command = f"./jacobi_profiled --norder {norder} --iterations {iterations} --convergence 0.0001"
    start_time = time.time()
    output = run_command(command)
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

norder = 2000
iterations = 20000

# Execute os programas e registre os tempos
jacobi_times = []
optimized_times = []
profiled_times = []

for attempt in range(1, 6):
    print(f"Executando tentativa {attempt}...")

    jacobi_time = run_jacobi(norder, iterations)
    optimized_time = run_jacobi_optimized(norder, iterations)
    profiled_time = run_jacobi_profiled(norder, iterations)

    jacobi_times.append(jacobi_time)
    optimized_times.append(optimized_time)
    profiled_times.append(profiled_time)

# Gere o gráfico
attempts = range(1, 6)

plt.plot(attempts, jacobi_times, color='red', label='jacobi')
plt.plot(attempts, optimized_times, color='yellow', label='jacobi_optimized')
plt.plot(attempts, profiled_times, color='green', label='jacobi_profiled')

plt.xlabel('Tentativa')
plt.ylabel('Tempo')
plt.title('Tempos de Execução')
plt.legend()

plt.show()
