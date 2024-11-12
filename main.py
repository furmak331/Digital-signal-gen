import numpy as np
import matplotlib.pyplot as plt
import time
from typing import Tuple




def print_fancy_header():
    header = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║           Digital Signal Processing Workbench v1.0           ║
    ║            By Furqan Makhdoomi & Mohammad Oyaiss             ║
    ║                                                              ║
    ║           Department of Information Technology               ║
    ║                        ©  5th Sem                            ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(header)
def loading_animation():
    print("\nInitializing system ", end="")
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")    

class SignalGenerator:
    def __init__(self):
        self.sampling_rate = 1000
        self.bit_duration = 0.1
        self.amplitude = 1
        
    def _create_time_base(self, data_length: int) -> np.ndarray:
        """Create time base for plotting signals"""
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        t = np.linspace(0, data_length * self.bit_duration, 
                       data_length * samples_per_bit)
        return t
    
    def find_longest_palindrome(self, data: str) -> str:
        """Find longest palindrome in binary data using dynamic programming"""
        n = len(data)
        # Create a table to store palindrome info
        table = [[False] * n for _ in range(n)]
        
        # All single chars are palindromes
        max_length = 1
        for i in range(n):
            table[i][i] = True
            
        # Check for substrings of length 2
        start = 0
        for i in range(n - 1):
            if data[i] == data[i + 1]:
                table[i][i + 1] = True
                start = i
                max_length = 2
                
        # Check for lengths greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if data[i] == data[j] and table[i + 1][j - 1]:
                    table[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
                        
        return data[start:start + max_length]
    
    def nrz_l(self, data: str) -> Tuple[np.ndarray, np.ndarray]:
        """Generate NRZ-L signal"""
        t = self._create_time_base(len(data))
        signal = np.zeros_like(t)
        
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        for i, bit in enumerate(data):
            if bit == '1':
                signal[i * samples_per_bit:(i + 1) * samples_per_bit] = self.amplitude
            else:
                signal[i * samples_per_bit:(i + 1) * samples_per_bit] = -self.amplitude
                
        return t, signal
    
    def nrz_i(self, data: str) -> Tuple[np.ndarray, np.ndarray]:
        """Generate NRZ-I signal"""
        t = self._create_time_base(len(data))
        signal = np.zeros_like(t)
        
        current_level = self.amplitude
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        
        for i, bit in enumerate(data):
            if bit == '1':
                current_level = -current_level
            signal[i * samples_per_bit:(i + 1) * samples_per_bit] = current_level
                
        return t, signal
    
    def manchester(self, data: str) -> Tuple[np.ndarray, np.ndarray]:
        """Generate Manchester signal"""
        t = self._create_time_base(len(data))
        signal = np.zeros_like(t)
        
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        half_samples = samples_per_bit // 2
        
        for i, bit in enumerate(data):
            if bit == '1':
                signal[i * samples_per_bit:i * samples_per_bit + half_samples] = self.amplitude
                signal[i * samples_per_bit + half_samples:(i + 1) * samples_per_bit] = -self.amplitude
            else:
                signal[i * samples_per_bit:i * samples_per_bit + half_samples] = -self.amplitude
                signal[i * samples_per_bit + half_samples:(i + 1) * samples_per_bit] = self.amplitude
                
        return t, signal
    
    def differential_manchester(self, data: str) -> Tuple[np.ndarray, np.ndarray]:
        """Generate Differential Manchester signal"""
        t = self._create_time_base(len(data))
        signal = np.zeros_like(t)
        
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        half_samples = samples_per_bit // 2
        last_level = self.amplitude
        
        for i, bit in enumerate(data):
            if bit == '0':
                # Transition at start of bit
                last_level = -last_level
            
            signal[i * samples_per_bit:i * samples_per_bit + half_samples] = last_level
            signal[i * samples_per_bit + half_samples:(i + 1) * samples_per_bit] = -last_level
            
        return t, signal
    
    def ami(self, data: str) -> Tuple[np.ndarray, np.ndarray]:
        """Generate AMI signal"""
        t = self._create_time_base(len(data))
        signal = np.zeros_like(t)
        
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        last_one_level = self.amplitude
        
        for i, bit in enumerate(data):
            if bit == '1':
                signal[i * samples_per_bit:(i + 1) * samples_per_bit] = last_one_level
                last_one_level = -last_one_level
                
        return t, signal
    
    def b8zs(self, data: str) -> Tuple[np.ndarray, np.ndarray]:
        """Generate B8ZS scrambled signal"""
        # Replace sequences of 8 zeros with special violation sequence
        i = 0
        scrambled_data = ""
        last_one_level = self.amplitude
        
        while i < len(data):
            if i <= len(data) - 8 and data[i:i+8] == "00000000":
                # B8ZS violation sequence: 000VB0VB
                # where V = violation (same polarity as previous), B = bipolar
                violation_sequence = f"000{'+' if last_one_level > 0 else '-'}-0{'+' if last_one_level > 0 else '-'}-"
                scrambled_data += violation_sequence
                i += 8
            else:
                if data[i] == '1':
                    scrambled_data += '+' if last_one_level > 0 else '-'
                    last_one_level = -last_one_level
                else:
                    scrambled_data += '0'
                i += 1
        
        # Convert scrambled data to signal
        t = self._create_time_base(len(data))
        signal = np.zeros_like(t)
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        
        for i, symbol in enumerate(scrambled_data):
            if symbol == '+':
                signal[i * samples_per_bit:(i + 1) * samples_per_bit] = self.amplitude
            elif symbol == '-':
                signal[i * samples_per_bit:(i + 1) * samples_per_bit] = -self.amplitude
                
        return t, signal
    
    def hdb3(self, data: str) -> Tuple[np.ndarray, np.ndarray]:
        """Generate HDB3 scrambled signal"""
        i = 0
        scrambled_data = ""
        last_one_level = self.amplitude
        violation_count = 0
        
        while i < len(data):
            if i <= len(data) - 4 and data[i:i+4] == "0000":
                # HDB3 violation sequence depends on number of preceding non-zero pulses
                if violation_count % 2 == 0:
                    violation_sequence = f"000{'+' if last_one_level > 0 else '-'}"
                else:
                    violation_sequence = f"{'+' if last_one_level > 0 else '-'}00{'+' if last_one_level > 0 else '-'}"
                scrambled_data += violation_sequence
                violation_count += 1
                i += 4
            else:
                if data[i] == '1':
                    scrambled_data += '+' if last_one_level > 0 else '-'
                    last_one_level = -last_one_level
                    violation_count += 1
                else:
                    scrambled_data += '0'
                i += 1
        
        # Convert scrambled data to signal
        t = self._create_time_base(len(data))
        signal = np.zeros_like(t)
        samples_per_bit = int(self.sampling_rate * self.bit_duration)
        
        for i, symbol in enumerate(scrambled_data):
            if symbol == '+':
                signal[i * samples_per_bit:(i + 1) * samples_per_bit] = self.amplitude
            elif symbol == '-':
                signal[i * samples_per_bit:(i + 1) * samples_per_bit] = -self.amplitude
                
        return t, signal
    
    def pcm(self, analog_signal: np.ndarray, bits: int = 8) -> str:
        """Convert analog signal to PCM digital signal"""
        # Quantization levels
        levels = 2 ** bits
        
        # Normalize signal to [-1, 1]
        normalized = analog_signal / np.max(np.abs(analog_signal))
        
        # Quantize
        quantized = np.round((normalized + 1) * (levels - 1) / 2)
        
        # Convert to binary
        digital = ''.join([format(int(x), f'0{bits}b') for x in quantized])
        
        return digital
    
    def delta_modulation(self, analog_signal: np.ndarray, step_size: float = 0.1) -> str:
        """Convert analog signal to digital using Delta Modulation"""
        digital = ""
        prev_value = 0
        
        for sample in analog_signal:
            if sample > prev_value:
                digital += "1"
                prev_value += step_size
            else:
                digital += "0"
                prev_value -= step_size
                
        return digital
    
    def plot_signal(self, t: np.ndarray, signal: np.ndarray, title: str):
        """Plot the generated signal"""
        plt.figure(figsize=(12, 4))
        plt.plot(t, signal, 'b-', linewidth=2)
        plt.grid(True)
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.ylim([-1.5 * self.amplitude, 1.5 * self.amplitude])
        plt.show()

def main():
    print_fancy_header()
    loading_animation()
    generator = SignalGenerator()
    
    print("Digital Signal Generator")
    print("1. Digital Input")
    print("2. Analog Input")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        data = input("Enter binary data stream: ")
        
        print("\nAvailable encoding schemes:")
        print("1. NRZ-L")
        print("2. NRZ-I")
        print("3. Manchester")
        print("4. Differential Manchester")
        print("5. AMI")
        
        scheme = input("Choose encoding scheme (1-5): ")
        
        # Find longest palindrome
        palindrome = generator.find_longest_palindrome(data)
        print(f"\nLongest palindrome in data: {palindrome}")
        
        if scheme == "5":  # AMI
            scramble = input("Do you want to use scrambling? (y/n): ")
            if scramble.lower() == 'y':
                scramble_type = input("Choose scrambling type (1: B8ZS, 2: HDB3): ")
                if scramble_type == "1":
                    t, signal = generator.b8zs(data)
                    generator.plot_signal(t, signal, "B8ZS Scrambled Signal")
                else:
                    t, signal = generator.hdb3(data)
                    generator.plot_signal(t, signal, "HDB3 Scrambled Signal")
            else:
                t, signal = generator.ami(data)
                generator.plot_signal(t, signal, "AMI Signal")
        else:
            if scheme == "1":
                t, signal = generator.nrz_l(data)
                generator.plot_signal(t, signal, "NRZ-L Signal")
            elif scheme == "2":
                t, signal = generator.nrz_i(data)
                generator.plot_signal(t, signal, "NRZ-I Signal")
            elif scheme == "3":
                t, signal = generator.manchester(data)
                generator.plot_signal(t, signal, "Manchester Signal")
            elif scheme == "4":
                t, signal = generator.differential_manchester(data)
                generator.plot_signal(t, signal, "Differential Manchester Signal")
    
    else:  # Analog input
        print("\nGenerating sample analog signal...")
        t = np.linspace(0, 1, 1000)
        analog_signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)
        
        print("\nChoose conversion method:")
        print("1. PCM")
        print("2. Delta Modulation")
        method = input("Enter choice (1/2): ")
        
        if method == "1":
            digital_data = generator.pcm(analog_signal)
        else:
            digital_data = generator.delta_modulation(analog_signal)
            
        print(f"\nGenerated digital data: {digital_data[:50]}...")
        
        # Proceed with line encoding
        print("\nChoose line encoding scheme for the digital data:")
        print("1. NRZ-L")
        print("2. NRZ-I")
        print("3. Manchester")
        print("4. Differential Manchester")
        print("5. AMI")
        
        scheme = input("Enter choice (1-5): ")
        
        if scheme == "5":
            t, signal = generator.ami(digital_data)
            generator.plot_signal(t, signal, "AMI Signal")
        elif scheme == "1":
            t, signal = generator.nrz_l(digital_data)
            generator.plot_signal(t, signal, "NRZ-L Signal")
        elif scheme == "2":
            t, signal = generator.nrz_i(digital_data)
            generator.plot_signal(t, signal, "NRZ-I Signal")
        elif scheme == "3":
            t, signal = generator.manchester(digital_data)
            generator.plot_signal(t, signal, "Manchester Signal")
        elif scheme == "4":
            t, signal = generator.differential_manchester(digital_data)
            generator.plot_signal(t, signal, "Differential Manchester Signal")

if __name__ == "__main__":
    main()
