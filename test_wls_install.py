import os
import subprocess
import sys
import shutil

def run_command(command, cwd=None, shell=True):
    print(f"➜ Running: {command}")
    process = subprocess.Popen(command, shell=shell, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    # Stream output as it runs
    for line in iter(process.stdout.readline, ""):
        print(line, end="")
        
    process.stdout.close()
    return_code = process.wait()
    
    if return_code != 0:
        print(f"❌ Command failed with return code {return_code}")
        sys.exit(return_code)
    else:
        print("✅ Command completed successfully.\n")

def main():
    print("==================================================")
    print(" WSL Debian Testing Script for n8n AI Stack")
    print("==================================================")
    print("This script simulates the deployment process in a clean WSL Debian environment.")
    
    # Check if running on Linux
    if sys.platform != "linux" and sys.platform != "linux2":
        print("⚠️ Warning: This script is intended to run inside WSL / Linux.")
    
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Working directory: {repo_dir}")
    
    # Pre-configure environment files to bypass manual interaction step
    services = ["n8n", "postgres-rag", "postgres-vector"]
    print("Setting up .env files automatically to bypass interactive prompts...")
    
    for service in services:
        env_example = os.path.join(repo_dir, "services", service, ".env.example")
        env_file = os.path.join(repo_dir, "services", service, ".env")
        if os.path.exists(env_example) and not os.path.exists(env_file):
            shutil.copy2(env_example, env_file)
            print(f"Created: {env_file}")
            
    # Normally, the user has to confirm they edited the .env file.
    # We will modify the install.sh temporarily or use expect, but it's simpler
    # to just feed 'y' into it.
    
    install_script = os.path.join(repo_dir, "install.sh")
    
    if not os.path.exists(install_script):
        print(f"❌ Error: {install_script} not found.")
        sys.exit(1)
        
    # Ensure it's executable
    run_command(f"chmod +x {install_script}", cwd=repo_dir)
    
    # Execute with auto-yes pipeline
    print("Executing install.sh (feeding 'y' to bypass .env check)...")
    run_command(f'echo "y" | sudo {install_script}', cwd=repo_dir)
    
    print("🚀 Test complete.")

if __name__ == "__main__":
    main()
