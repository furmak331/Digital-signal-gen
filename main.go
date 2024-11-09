package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Entry point
func main() {
	fmt.Println("=== Digital Signal Generator ===")
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Choose Input Type: (1) Analog (2) Digital")
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	if choice == "1" {
		handleAnalogInput()
	} else if choice == "2" {
		handleDigitalInput()
	} else {
		fmt.Println("Invalid choice. Please restart.")
	}
}

// Handles analog input (PCM/DM)
func handleAnalogInput() {
	fmt.Println("Analog signal processing selected!")
	fmt.Println("Choose Modulation Type: (1) PCM (2) Delta Modulation")
	reader := bufio.NewReader(os.Stdin)
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	if choice == "1" {
		performPCM()
	} else if choice == "2" {
		performDeltaModulation()
	} else {
		fmt.Println("Invalid modulation type.")
	}
}

// Handles digital input (line coding)
func handleDigitalInput() {
	fmt.Println("Enter binary input (e.g., 101010):")
	reader := bufio.NewReader(os.Stdin)
	data, _ := reader.ReadString('\n')
	data = strings.TrimSpace(data)

	fmt.Println("Choose Encoding Type:")
	fmt.Println("1: NRZ-L")
	fmt.Println("2: NRZ-I")
	fmt.Println("3: Manchester")
	fmt.Println("4: Differential Manchester")
	fmt.Println("5: AMI")
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	switch choice {
	case "1":
		fmt.Println("Encoded Signal (NRZ-L):", encodeNRZL(data))
	case "2":
		fmt.Println("Encoded Signal (NRZ-I):", encodeNRZI(data))
	case "3":
		fmt.Println("Encoded Signal (Manchester):", encodeManchester(data))
	case "4":
		fmt.Println("Encoded Signal (Differential Manchester):", encodeDiffManchester(data))
	case "5":
		handleAMI(data)
	default:
		fmt.Println("Invalid encoding type.")
	}
}
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Entry point
func main() {
	fmt.Println("=== Digital Signal Generator ===")
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Choose Input Type: (1) Analog (2) Digital")
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	if choice == "1" {
		handleAnalogInput()
	} else if choice == "2" {
		handleDigitalInput()
	} else {
		fmt.Println("Invalid choice. Please restart.")
	}
}

// Handles analog input (PCM/DM)
func handleAnalogInput() {
	fmt.Println("Analog signal processing selected!")
	fmt.Println("Choose Modulation Type: (1) PCM (2) Delta Modulation")
	reader := bufio.NewReader(os.Stdin)
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	if choice == "1" {
		performPCM()
	} else if choice == "2" {
		performDeltaModulation()
	} else {
		fmt.Println("Invalid modulation type.")
	}
}

// Handles digital input (line coding)
func handleDigitalInput() {
	fmt.Println("Enter binary input (e.g., 101010):")
	reader := bufio.NewReader(os.Stdin)
	data, _ := reader.ReadString('\n')
	data = strings.TrimSpace(data)

	fmt.Println("Choose Encoding Type:")
	fmt.Println("1: NRZ-L")
	fmt.Println("2: NRZ-I")
	fmt.Println("3: Manchester")
	fmt.Println("4: Differential Manchester")
	fmt.Println("5: AMI")
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	switch choice {
	case "1":
		fmt.Println("Encoded Signal (NRZ-L):", encodeNRZL(data))
	case "2":
		fmt.Println("Encoded Signal (NRZ-I):", encodeNRZI(data))
	case "3":
		fmt.Println("Encoded Signal (Manchester):", encodeManchester(data))
	case "4":
		fmt.Println("Encoded Signal (Differential Manchester):", encodeDiffManchester(data))
	case "5":
		handleAMI(data)
	default:
		fmt.Println("Invalid encoding type.")
	}
}
