import subprocess

# Path to the file containing Nmap scripts
nmap_scripts_path = '/mnt/data/nmap_scripts.txt'

# Read the Nmap scripts from the file
with open(nmap_scripts_path, 'r') as file:
    nmap_scripts = [line.strip() for line in file if line.strip()]

# Function to execute Nmap commands and capture the output
def execute_nmap_script(script):
    try:
        result = subprocess.run(script.split(), capture_output=True, text=True, timeout=300)
        output = result.stdout if result.stdout else result.stderr
        return output
    except subprocess.TimeoutExpired:
        return f"Command timed out: {script}"
    except Exception as e:
        return f"An error occurred: {e}"

# Execute each Nmap script and capture the output
script_outputs = {}
for script in nmap_scripts:
    if script:  # Ensure the script is not empty
        output = execute_nmap_script(script)
        script_outputs[script] = output

# Save the filtered outputs to a file
output_file_path = '/mnt/data/nmap_script_outputs.txt'
with open(output_file_path, 'w') as file:
    for script, output in script_outputs.items():
        file.write(f"Script: {script}\n")
        file.write(f"Output:\n{output}\n")
        file.write("\n" + "="*80 + "\n")

print(f"Outputs have been saved to {output_file_path}")
