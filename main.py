"""
AI Bootcamp - Starter Project
A simple test script checking the Python environment and simulating an AI pipeline.
"""
import sys
import platform

def main():
    print("=" * 50)
    print("  AI Bootcamp: Starter Project Environment Check")
    print("=" * 50)
    print(f"Python Version : {sys.version.split()[0]}")
    print(f"Platform       : {platform.system()} ({platform.machine()})")
    print("-" * 50)
    
    sample_text = "Natural Language Processing and Generative AI"
    tokens = sample_text.split()
    print(f"Sample Input   : '{sample_text}'")
    print(f"Token Count    : {len(tokens)}")
    print(f"Tokens         : {tokens}")
    print("=" * 50)
    print("Starter project environment is ready!")

if __name__ == "__main__":
    main()
