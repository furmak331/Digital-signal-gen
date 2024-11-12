Here’s the enhanced and detailed README with well-explained definitions, improved explanations for scrambling techniques, properly referenced content, and included images.

---

# **Digital Signal Processing Workbench**

A Python-based tool for generating and visualizing various **digital line coding schemes** and **analog-to-digital conversion methods**.

---

## **Features**

### **Line Coding Schemes**

#### **1. NRZ-L (Non-Return-to-Zero Level)**  
- **Description**:  
  Binary `1` is represented by **positive voltage**, and binary `0` by **negative voltage**.  
  - Does not require a clock signal and uses signal level to encode binary data.  

#### **2. NRZ-I (Non-Return-to-Zero Inverted)**  
- **Description**:  
  A transition occurs at the **start of the bit period** for binary `1`, while no transition occurs for binary `0`.  
  - Ensures synchronization between sender and receiver.  

#### **3. Manchester Encoding**  
- **Description**:  
  This encoding ensures a **transition in the middle of each bit period**.  
  - Low-to-high transition represents binary `1`.  
  - High-to-low transition represents binary `0`.  

#### **4. Differential Manchester**  
- **Description**:  
  - Always has a **transition in the middle of the bit period** to provide synchronization.  
  - A **transition at the start of the bit period** represents binary `0`.  
  - **No transition at the start** represents binary `1`.  

**Visual Comparison:**  
![Encoding Comparison](https://img.electronicdesign.com/files/base/ebm/electronicdesign/image/2021/04/WtD_Manchester_NRZ_NRZI_promo.6080cd13035b8.png?auto=format,compress&fit=crop&q=45&h=528&height=528&w=950&width=950)

*Image Credit: [Electronic Design](https://www.electronicdesign.com/technologies/communications/article/21802271/electronic-design-whats-the-difference-between-nrz-nrzi-and-manchester-encoding)*

**Differential Manchester Vs Manchester Encoding**





![Differential Manchester Encoding](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilPxZy1U3XpkJ4h6tG5Phk_WWJ-kFuPgp_00YRvaGdzfAF1ry_y-RkTVMk0-bPHxx-A24lHf7eJfWYIIJgg9mMSPuRdchz-zGH6f1LMGMuUBXvVpnoAybOTBF5jYpdWJdq3zb_TFfRrpM-/w400-h210/DME-Manchester.PNG)  
*Image Credit: [Teledyne lecroy](https://blog.teledynelecroy.com/2021/11/what-is-differential-manchester-encoding.html)*

---

### **Scrambling Techniques**

Scrambling is used to enhance signal synchronization without increasing the bit rate. It works as a solution for synchronization problems caused by prolonged sequences of zeros in bipolar schemes like **AMI (Alternate Mark Inversion)**.  

#### **1. B8ZS (Bipolar with 8-Zero Substitution)**  
- **How It Works**:  
  - Replaces **8 consecutive zeros** with a special sequence: `000VB0VB`.  
  - **V (Violation)**: Non-zero voltage with the **same polarity** as the previous non-zero voltage, violating AMI rules.  
  - **B (Bipolar)**: Non-zero voltage with **opposite polarity** from the previous non-zero voltage, adhering to AMI rules.  

- **Example**:  
  For data `100000000`, it replaces 8 zeros with the pattern `000VB0VB`, ensuring synchronization.

---

#### **2. HDB3 (High-Density Bipolar 3-Zero Substitution)**  
- **How It Works**:  
  Replaces **4 consecutive zeros** with either:  
  - `000V` or `B00V`, depending on the number of previous non-zero pulses.  

- **Rules**:  
  - If the number of non-zero pulses since the last substitution is **odd**, the substitution pattern is `000V`.  
  - If the number of non-zero pulses is **even**, the substitution pattern is `B00V`.  

---

### **Comparative Visualization**
Below is an illustration of **B8ZS** and **HDB3** scrambling:  

![Scrambling Techniques](https://media.geeksforgeeks.org/wp-content/uploads/Digital_Electronics_Scrambling_1.jpg)  

*Image Source: [GeeksforGeeks](https://www.geeksforgeeks.org/what-is-scrambling-in-digital-electronics/)*  

---

### **Analog-to-Digital Conversion**

#### **Pulse Code Modulation (PCM)**  
- **Description**:  
  Converts analog signals into digital using:  
  1. **Sampling**: Discrete-time representation of the signal.  
  2. **Quantization**: Approximation to a finite set of levels.  
  3. **Encoding**: Conversion of quantized values to binary form.  

#### **Delta Modulation**  
- **Description**:  
  - Tracks the signal's change over time using a fixed step size.  
  - Efficiently encodes increasing or decreasing trends using a single bit.  

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dsp-workbench.git
   ```

2. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```

---

## **References**

1. *Electronic Design*: ["What’s the Difference Between NRZ, NRZI, and Manchester Encoding?"](https://www.electronicdesign.com/technologies/communications/article/21802271/electronic-design-whats-the-difference-between-nrz-nrzi-and-manchester-encoding)  
   - Line coding schemes and comparative definitions.  

2. *Wikipedia*:  
   - [NRZ-L](https://en.wikipedia.org/wiki/Non-return-to-zero)  
   - [Manchester Encoding](https://en.wikipedia.org/wiki/Manchester_code)  

3. *GeeksforGeeks*: ["What is Scrambling in Digital Electronics?"](https://www.geeksforgeeks.org/what-is-scrambling-in-digital-electronics/)  
   - Definitions and examples of B8ZS and HDB3.  

---
## Authors
- Furqan Makhdoomi - 2022BITE005
- Mohammad Owais - 2022BITE006
- Musharaf Maqbool - 2022BITE053

## Acknowledgments
- Department of Information Technology
```
