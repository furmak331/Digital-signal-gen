func handleAMI(data string) {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Do you want to apply scrambling? (yes/no)")
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(strings.ToLower(choice))

	if choice == "yes" {
		fmt.Println("Choose Scrambling Type: (1) B8ZS (2) HDB3")
		scramblingChoice, _ := reader.ReadString('\n')
		scramblingChoice = strings.TrimSpace(scramblingChoice)

		switch scramblingChoice {
		case "1":
			fmt.Println("Scrambled Signal (B8ZS):", scrambleB8ZS(data))
		case "2":
			fmt.Println("Scrambled Signal (HDB3):", scrambleHDB3(data))
		default:
			fmt.Println("Invalid scrambling type.")
		}
	} else {
		fmt.Println("Encoded Signal (AMI):", encodeAMI(data))
	}
}

func encodeAMI(data string) string {
	var result strings.Builder
	positive := true

	for _, bit := range data {
		if bit == '1' {
			if positive {
				result.WriteString("+ ")
			} else {
				result.WriteString("- ")
			}
			positive = !positive
		} else {
			result.WriteString("0 ")
		}
	}
	return result.String()
}
