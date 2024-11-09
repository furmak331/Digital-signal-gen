# Digital Signal Generator

A Python-based tool to generate and visualize various digital and line encoding schemes. It supports binary and analog input, offering options for encoding, scrambling, and modulation.

## Features
- Supports **NRZ-L**, **NRZ-I**, **Manchester**, **Differential Manchester**, and **AMI** encoding.
- Scrambling techniques: **B8ZS** and **HDB3**.
- Analog to digital conversion via **PCM** and **Delta Modulation**.
- Visualizes the generated signals using Matplotlib.
- Includes functionality to find the longest palindrome in binary data.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/furmak331/Digital-signal-gen.git
   cd digital-signal-generator
   ```
2. Run the script:
   ```bash
   python3 signal_generator.py
   ```
3. Follow the prompts to input data and choose encoding schemes.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## License
This project is open-source. Feel free to use and modify it as needed!