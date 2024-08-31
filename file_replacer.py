import os

# Function to replace strings in a file and save to the output folder
def replace_strings_in_file(input_file_path, output_folder, replacements):
    with open(input_file_path, 'r') as file:
        file_content = file.read()

    # Replace the specified strings
    for old_string, new_string in replacements.items():
        file_content = file_content.replace(old_string, new_string)

    # Prepare output file path
    output_file_name = os.path.basename(input_file_path)
    output_file_path = os.path.join(output_folder, output_file_name)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Write the modified content to a new file
    with open(output_file_path, 'w') as file:
        file.write(file_content)

    print(f"File saved to: {output_file_path}")

# Define the input folder and output folder
input_folder = os.getcwd()  # Present working directory
output_folder = os.path.join(input_folder, 'output')

# Collect input from the user
file_location = input("Enter the file location to replace 'xfilepathx': ")
domain_name = input("Enter the domain name to replace 'yourdomain': ")
ip_address = input("Enter the IP address to replace '192.168.1.25': ")
container_name = input("Enter the container name to replace 'uptime-kuma': ")

# Define the file paths and corresponding replacements
file_replacements = {
    'docker-compose.yml': {'xfilepathx': file_location},
    'configuration.yml': {'yourdomain': domain_name},
    'Authelia_CONF.txt': {'192.168.1.25': ip_address},
    'Protected_Domain_CONF.txt': {
        'uptime-kuma': container_name,
        '192.168.1.25': ip_address,
        'yourdomain': domain_name
    },
}

# Iterate over each file and apply the replacements
for file_name, replacements in file_replacements.items():
    input_file_path = os.path.join(input_folder, file_name)
    replace_strings_in_file(input_file_path, output_folder, replacements)
