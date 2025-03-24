import os
import subprocess
import uuid

# Define input and output directories
input_root = r"C:\Users\subha\Box\Input"
output_root = r"C:\Users\subha\Box\Output_Deidentified_Notes"

# Path to the NLM Scrubber executable
scrubber_exe = r"C:\Users\subha\Downloads\scrubber\scrubber.19.0411W\scrubber.19.0411W.exe"

# Function to create a config file dynamically
def create_config(input_folder, output_folder, config_path):
    with open(config_path, 'w') as config_file:
        config_file.write(f"ROOT1 = {input_folder}\n")
        config_file.write(f"ClinicalReports_dir = ROOT1\n")
        config_file.write(f"ClinicalReports_files = .*\\.txt\n")
        config_file.write(f"nPHI_outdir = {output_folder}\n")

# Function to process directories recursively
def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        # Process directories that contain text files
        if any(file.endswith('.txt') for file in files):
            relative_path = os.path.relpath(root, input_root)
            output_folder = os.path.join(output_root, relative_path)
            os.makedirs(output_folder, exist_ok=True)

            # Generate a unique config file
            config_filename = f"scrubber_config_{uuid.uuid4().hex}.cfg"
            config_path = os.path.join(output_folder, config_filename)

            # Create config file for processing
            create_config(root, output_folder, config_path)

            # Run the scrubber with the generated config
            command = [scrubber_exe, config_path]
            process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Logging output and errors
            with open(os.path.join(output_folder, "scrubber_log.txt"), "w") as log_file:
                log_file.write(f"STDOUT:\n{process.stdout}\n")
                log_file.write(f"STDERR:\n{process.stderr}\n")

            if process.returncode == 0:
                print(f"Successfully processed: {root}")
            else:
                print(f"Error processing {root}: {process.stderr}")

# Start processing both 'aria' and 'cerner' folders
process_directory(os.path.join(input_root, "aria"), os.path.join(output_root, "aria"))
process_directory(os.path.join(input_root, "cerner"), os.path.join(output_root, "cerner"))

print("\n Processing complete!")
