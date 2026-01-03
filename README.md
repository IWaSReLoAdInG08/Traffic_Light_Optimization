# Traffic Light Optimization and Optimal Path Prediction

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-red.svg)](https://pytorch.org/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8-green.svg)](https://ultralytics.com/)

A comprehensive AI-powered traffic management system that combines computer vision for real-time vehicle detection and machine learning for optimal path prediction and traffic light optimization.

## 🚀 Features

- **Real-time Vehicle Detection**: Uses YOLOv8 for accurate vehicle detection and tracking
- **Traffic Flow Analysis**: Monitors vehicle movement across different zones
- **Optimal Path Prediction**: Machine learning model to predict vehicle exit paths
- **Traffic Light Optimization**: Analyzes traffic patterns to optimize signal timing
- **Interactive Visualizations**: HTML plots for traffic density and optimization results

## 📁 Project Structure

```
Traffic_Light_Optimization/
├── data/                    # Dataset files
│   ├── traffic_data.csv
│   ├── vehicle_summary*.csv
│   └── lane_traffic_time_series.csv
├── models/                  # Trained models and encoders
│   ├── exit_path_model.pt
│   └── encoders.pkl
├── notebooks/               # Jupyter notebooks
│   └── Traffic_Green_Light_Optimization_And_Optimal_Path.ipynb
├── plots/                   # Generated visualizations
│   ├── green_light_optimization.html
│   ├── green_signal_optimization_plot.html
│   └── traffic_density_plot.html
├── src/                     # Source code
│   ├── ultralytics_example.py
│   └── CSV_data_ultralytics.py
├── requirements.txt         # Python dependencies
├── setup.ps1               # Setup script
├── .gitignore
└── README.md
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/traffic-light-optimization.git
   cd traffic-light-optimization
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run setup (Windows)**
   ```powershell
   .\setup.ps1
   ```

## 📊 Usage

### 1. Vehicle Detection and Tracking

Run the vehicle detection script:

```bash
python src/ultralytics_example.py --source path/to/video.mp4 --output results/
```

### 2. Path Prediction Model

Open the Jupyter notebook:

```bash
jupyter notebook notebooks/Traffic_Green_Light_Optimization_And_Optimal_Path.ipynb
```

The notebook includes:
- Data preprocessing
- Model training for exit path prediction
- Traffic optimization analysis
- Visualization of results

### 3. Traffic Analysis

The system analyzes traffic patterns from CSV data to:
- Predict optimal vehicle paths
- Optimize traffic light timings
- Generate density plots

## 🤖 Models and Algorithms

- **YOLOv8**: For real-time object detection
- **PyTorch Neural Network**: Custom model for path prediction
- **Supervisely**: For annotation and tracking
- **Scikit-learn**: For data preprocessing and encoding

## 📈 Results

The system provides:
- Real-time vehicle counting per zone
- Path prediction accuracy metrics
- Traffic light optimization recommendations
- Interactive HTML visualizations

## 🔧 Configuration

- Modify zone polygons in the source code for different camera setups
- Adjust model hyperparameters in the notebook
- Update data paths as needed

## 📝 Requirements

- Python 3.8+
- PyTorch
- Ultralytics YOLO
- OpenCV
- Pandas, NumPy
- Scikit-learn

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Ultralytics for YOLO implementation
- PyTorch team for the deep learning framework
- Supervision library for computer vision utilities

## 📞 Contact

For questions or collaborations, please open an issue on GitHub.