# FRCM Strengthened RC Beam Shear Strength Predictor

This tool predicts the shear strength of Fiber Reinforced Cementitious Matrix (FRCM) strengthened Reinforced Concrete (RC) beams using an XGBoost machine learning model. It provides a user-friendly graphical interface for engineers and researchers to input beam parameters and obtain accurate shear strength predictions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Input Parameters](#input-parameters)
  - [Output](#output)
- [Dependencies](#dependencies)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Accurate Predictions**: Utilizes a pre-trained XGBoost model for high-accuracy shear strength predictions.
- **User-Friendly Interface**: Easy-to-use GUI built with Tkinter and ttk themes.
- **Customizable Inputs**: Supports a wide range of input parameters for different beam configurations.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux systems.

## Installation

### Prerequisites

- **Python 3.x**
- **pip** (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/frcm-shear-strength-predictor.git
cd frcm-shear-strength-predictor
```

### Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Ensure that the model files `XG5.dat` and `std.pkl` are located in the same directory as the main script.

Run the application:

```bash
python shear_capacity_prediction.py
```

### Input Parameters

- **b<sub>w</sub> (mm)**: Width of the beam.
- **d (mm)**: Effective depth of the beam.
- **a/d**: Shear span to depth ratio.
- **f'<sub>c</sub> (MPa)**: Compressive strength of concrete.
- **f<sub>yw</sub> (MPa)**: Yield strength of transverse reinforcement.
- **ρ<sub>long</sub>**: Longitudinal reinforcement ratio.
- **ρ<sub>w</sub>**: Transverse reinforcement ratio.
- **SC**: Strengthening configuration.
  - U-shaped = 1
  - Side bonded = 2
  - Fully wrapped = 3
- **FT**: Fiber type.
  - Basalt = 1
  - Carbon = 2
  - Glass = 3
  - PBO = 4
  - Steel = 5
- **ρ<sub>f</sub>**: Fiber reinforcement ratio.
- **ε<sub>fu</sub>**: Ultimate strain of the fiber.
- **E<sub>f</sub> (GPa)**: Elastic modulus of the fiber.
- **t<sub>cm</sub> (mm)**: Thickness of the cementitious matrix.
- **f<sub>cm</sub> (MPa)**: Compressive strength of the cementitious matrix.

### Output

- After clicking the **Calculate** button, the predicted shear strength will be displayed in kilonewtons (kN) with two decimal places.
<img width="795" alt="4100d526bb597ed448825149cd54767" src="https://github.com/user-attachments/assets/43f4fcde-03be-4283-9166-9ac596a5f27d">


## Dependencies

The application requires the following Python libraries:

- **tkinter**
- **ttkthemes**
- **numpy**
- **xgboost**

All dependencies can be installed using the `requirements.txt` file provided.

## Authors

- **Xiangsheng Liu**
- **Grazziela P. Figueredo**
- **George S.D. Gordon**
- **Georgia E. Thermou**

**Affiliation**: University of Nottingham

For inquiries, please contact: [evxxl17@nottingham.ac.uk](mailto:evxxl17@nottingham.ac.uk)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to thank the contributors and the University of Nottingham for supporting this project.

---

**Note**: Replace `yourusername` in the clone URL with your actual GitHub username.

**Important**:

- If the model files `XG5.dat` and `std.pkl` are too large to include directly in the repository, please provide download links or instructions on how to obtain them.
- Ensure that the file paths in your code are relative and correctly point to the model files in the project directory.
