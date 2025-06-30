#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pickle
import numpy as np
import threading

# Load XGBoost model and scaler
with open("XG5.dat", "rb") as file:
    xgb_model = pickle.load(file)

with open("std.pkl", "rb") as f:
    scaler = pickle.load(f)

# Define prediction function
def predict_shear_strength_gui():
    try:
        # Get user inputs
        inputs = [float(bw_entry.get()), float(d_entry.get()), float(ad_entry.get()), float(fc_entry.get()),
                  float(fywd_entry.get()), float(rlong_entry.get()), float(rw_entry.get()), float(sc_entry.get()),
                  float(fiber_type_entry.get()), float(rf_entry.get()), float(efu_entry.get()), float(ef_entry.get()),
                  float(tcm_entry.get()), float(fcm_entry.get())]
        input_data = np.array([inputs])

        # Scale input data
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        shear_strength = xgb_model.predict(input_data_scaled)

        # Display result (rounded to two decimal places)
        result_label.config(text=f"{shear_strength[0]:.2f} kN")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Function to create the main window
def create_main_window():
    # Create the main window
    window = ThemedTk(theme="breeze")
    window.title("Shear Capacity Prediction Tool")
    window.geometry("1060x540")
    window.resizable(False, False)

    # Define create_subscript_label function
    def create_subscript_label(parent, main_text, sub_text, unit_text=None, font=("Times New Roman", 11), italic=True):
        label_frame = tk.Frame(parent, bg="white")
        if italic:
            main_font = (font[0], font[1], "bold italic")
            sub_font = (font[0], font[1]-3, "bold italic")
        else:
            main_font = (font[0], font[1], "bold")
            sub_font = (font[0], font[1]-3, "bold")

        main_label = tk.Label(label_frame, text=main_text, font=main_font, bg="white")
        main_label.pack(side="left", pady=0)

        if sub_text:
            sub_label = tk.Label(label_frame, text=sub_text, font=sub_font, bg="white")
            sub_label.pack(side="left", pady=0, anchor='s')

        if unit_text:
            unit_label = tk.Label(label_frame, text=f" ({unit_text})", font=(font[0], font[1], "bold"), bg="white")
            unit_label.pack(side="left", pady=0)

        label_frame.pack(side="left", padx=0, pady=0)
        return label_frame

    # Create left input parameter frame
    input_frame = tk.Frame(window, highlightbackground="#39678d", highlightthickness=1, bd=0, bg="white")
    input_frame.place(x=30, y=70, width=580, height=360)

    # Input frame title
    input_title = tk.Label(window, text="INPUT PARAMETERS", font=("Helvetica", 22, "bold"), fg="#39678d", bg="white")
    input_title.place(x=310, y=35, anchor="center")

    # Input fields and labels
    labels_with_subscript = [
        ('b', 'w'), ('d', ''), ('a/d', ''), ("f'", 'c'), ("f", 'yw'),
        ('ρ', 'long'), ('ρ', 'w'), ('SC', ''), ('FT', ''),
        ('ρ', 'f'), ('ε', 'fu'), ('E', 'f'), ('t', 'cm'), ('f', 'cm')
    ]
    units = ['mm', 'mm', '', 'MPa', 'MPa', '', '', '', '', '', '', 'GPa', 'mm', 'MPa']
    entries = []

    for i, (label, unit) in enumerate(zip(labels_with_subscript, units)):
        main_text, sub_text = label

        # Decide whether to use italic font
        if main_text in ['SC', 'FT', 'a/d']:
            font = ("Helvetica", 11)
            italic = False
        else:
            font = ("Times New Roman", 11)
            italic = True

        # Create label
        row = i % 7
        col = (i // 7) * 2

        # Adjust padding based on column
        if col == 2:
            label_padx = 25  # Increase padding for the second column labels to shift them right
        else:
            label_padx = 10  # Original padding

        # Create frame for label and entry
        frame = tk.Frame(input_frame, bg="white")
        frame.grid(row=row, column=col, columnspan=2, padx=label_padx, pady=5, sticky="w")

        # Create label
        create_subscript_label(frame, main_text, sub_text, unit_text=unit, font=font, italic=italic)

        # Create entry
        entry = ttk.Entry(frame)
        entry.pack(side="left", padx=5, pady=0)
        entries.append(entry)

    # Assign entry variables
    bw_entry, d_entry, ad_entry, fc_entry, fywd_entry, rlong_entry, rw_entry = entries[:7]
    sc_entry, fiber_type_entry, rf_entry, efu_entry, ef_entry, tcm_entry, fcm_entry = entries[7:]

    # Add annotations
    annotation_text = (
        "Note: 1. FT refers to Fibre type: Basalt=1, Carbon=2, Glass=3, PBO=4, Steel=5;\n"
        "         2. SC refers to Strengthening configuration: U-shaped=1, side bonded=2, fully wrapped=3\n"
        "This tool was developed by Xiangsheng Liu, Grazziela P. Figueredo, George S.D. Gordon, and Georgia E. Thermou.\n"
        "University of Nottingham\n"
        "For inquiries, please contact: evxxl17@nottingham.ac.uk"
    )
    annotation_lines = annotation_text.split('\n')
    First_two_notes = '\n'.join(annotation_lines[:2])
    Rest_notes = '\n'.join(annotation_lines[2:])

    # Add the first two notes to the left frame
    first_two_notes_label = tk.Label(input_frame, text=First_two_notes, font=("Helvetica", 10), justify="left",
                                     anchor="w", fg="black", bg="white", wraplength=560)
    first_two_notes_label.grid(row=7, column=0, columnspan=4, padx=10, pady=5, sticky="w")

    # Create right output parameter frame
    output_frame = tk.Frame(window, highlightbackground="darkblue", highlightthickness=1, bd=0)
    output_frame.place(x=640, y=70, width=400, height=360)

    # Output frame title
    output_title = tk.Label(window, text="OUTPUT PARAMETER", font=("Helvetica", 22, "bold"), fg="darkblue")
    output_title.place(x=840, y=35, anchor="center")

    # Center content in output frame
    output_frame.pack_propagate(False)

    # Output label
    output_label = ttk.Label(output_frame, text="Shear Capacity of\nFRCM Strengthened Beam",
                             font=("Helvetica", 16, "bold"), foreground="darkblue", anchor="center", justify="center")
    output_label.pack(pady=20)

    # Calculate button with maroon border
    calculate_frame = tk.Frame(output_frame, bg="white", width=200, height=40, highlightbackground="#8B0000", highlightthickness=2)
    calculate_frame.pack(pady=10)

    calculate_button = tk.Button(calculate_frame, text="Calculate", command=predict_shear_strength_gui,
                                 font=("Helvetica", 12, "bold"), fg="#8B0000", bg="white", bd=0)
    calculate_button.place(relx=0.5, rely=0.5, anchor="center")

    # Result frame with maroon border
    result_frame = tk.Frame(output_frame, bg="white", width=200, height=40, highlightbackground="#8B0000", highlightthickness=2)
    result_frame.pack(pady=10)

    global result_label  # Declare as global variable to access in the prediction function
    result_label = ttk.Label(result_frame, text="", font=("Helvetica", 12, "bold"), foreground="black", background="white")
    result_label.place(relx=0.5, rely=0.5, anchor="center")

    # Add developer information below the result frame
    credits_label = tk.Label(output_frame, text=Rest_notes, font=("Helvetica", 10), justify="center",
                             anchor="center", fg="black", wraplength=390)
    credits_label.pack(pady=10)

    # Bottom frame
    bottom_frame = tk.Frame(window, bg="#00008B", width=1030, height=50)
    bottom_frame.place(x=20, y=440)

    bottom_label = ttk.Label(bottom_frame, text="Shear Capacity Prediction Tool of FRCM Strengthened RC Beam ",
                             font=("Helvetica", 22, "bold"), foreground="white", background="#00008B")
    bottom_label.place(relx=0.5, rely=0.5, anchor="center")

    # Run the main loop
    window.mainloop()

# Start the GUI application
threading.Thread(target=create_main_window).start()

