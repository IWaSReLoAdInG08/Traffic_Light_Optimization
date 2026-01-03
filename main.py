#!/usr/bin/env python3
"""
Traffic Light Optimization and Optimal Path Prediction
Main entry point for the project
"""

import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Traffic Light Optimization System')
    parser.add_argument('--mode', choices=['detect', 'predict', 'analyze'],
                       default='analyze', help='Mode to run')
    parser.add_argument('--input', type=str, help='Input file or data path')
    parser.add_argument('--output', type=str, default='output/',
                       help='Output directory')

    args = parser.parse_args()

    print("🚦 Traffic Light Optimization System")
    print("=" * 40)

    if args.mode == 'detect':
        print("Running vehicle detection...")
        # Import and run detection
        from src.ultralytics_example import run_detection
        run_detection(args.input, args.output)

    elif args.mode == 'predict':
        print("Running path prediction...")
        # Load model and predict
        import torch
        import joblib
        from notebooks.Traffic_Green_Light_Optimization_And_Optimal_Path import ExitPredictor

        # Load model
        model = ExitPredictor(input_size=6, hidden_size=64, num_classes=4)
        model.load_state_dict(torch.load('models/exit_path_model.pt'))
        model.eval()

        # Load encoders
        scaler, le_vehicle_type, le_direction, le_entry, le_exit = joblib.load('models/encoders.pkl')

        print("Model loaded. Ready for predictions.")

    elif args.mode == 'analyze':
        print("Running traffic analysis...")
        # Run analysis from notebook
        print("Please run the Jupyter notebook for full analysis:")
        print("jupyter notebook notebooks/Traffic_Green_Light_Optimization_And_Optimal_Path.ipynb")

    print("✅ Done!")

if __name__ == "__main__":
    main()