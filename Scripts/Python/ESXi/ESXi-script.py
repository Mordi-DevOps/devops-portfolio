import sys
import yaml
import paramiko

def main(machine_id):
    # Load configuration from YAML file
    try:
        with open('config.yaml', 'r') as f:
            # Using .get() ensures the script doesn't crash if keys are missing
            config = yaml.safe_load(f).get('esxi', {})
    except FileNotFoundError:
        print("Error: config.yaml file not found.")
        return
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
        return

    # Define ESXi vim-cmd commands
    get_state = f'vim-cmd vmsvc/power.getstate {machine_id}'
    power_on = f'vim-cmd vmsvc/power.on {machine_id}'
    
    # Initialize SSH Client
    client = paramiko.SSHClient()
    # Automatically add the server's host key (appropriate for lab environments)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Establish connection to the ESXi host
        print(f"Connecting to host: {config.get('hostname')}...")
        client.connect(
            config.get('hostname'), 
            port=22, 
            username=config.get('username'), 
            password=config.get('password'),
            timeout=10
        )
        
        # Check current VM power status
        _, stdout, _ = client.exec_command(get_state)
        output = stdout.read().decode()
        
        if 'Powered off' in output:
            print(f"VM {machine_id} is currently POWERED OFF. Initiating power on...")
            client.exec_command(power_on)
            print('Power-on command sent successfully.')
        else:
            print(f"VM {machine_id} is already running or status is unknown.")

    except paramiko.AuthenticationException:
        print("Authentication failed, please check your credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the connection is always closed
        client.close()
        print("SSH connection closed.")

if __name__ == '__main__':
    # Ensure machine_id is provided as a command-line argument
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python esxi_control.py <machine_id>")
