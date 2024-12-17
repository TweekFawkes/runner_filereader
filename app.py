import sys
from datetime import datetime
import os

def main():
    # Check if command line argument is provided
    if len(sys.argv) < 2:
        print("Error: Please provide a file name as an argument")
        sys.exit(1)
    
    file_name = sys.argv[1]
    file_path = os.path.join(os.getcwd(), "inputs", file_name)
    
    # Verify if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
        
    print(f"Reading the File: {file_path}")

if __name__ == "__main__":
    main()
