# AI-Driven Traffic Management System

An intelligent traffic signal management system that uses computer vision and machine learning to optimize traffic flow by analyzing real-time vehicle counts from multiple traffic cameras.

---

## 🚀 Features

- 🚗 **Real-time Vehicle Detection**: Uses YOLO model to detect and count vehicles in traffic videos  
- 🚦 **Dynamic Signal Timing**: Automatically adjusts green light duration based on vehicle density  
- 📹 **Multi-Camera Support**: Analyzes up to 4 traffic feeds simultaneously  
- 🔄 **Continuous Analysis**: Progresses through video timeline for realistic simulation  
- 🌐 **Web Interface**: User-friendly web dashboard with live signal visualization  
- ⚡ **WebSocket Communication**: Real-time updates of traffic signal states  

---

## 🎥 Demo

The system processes traffic videos from multiple intersections and dynamically calculates optimal green light timing for each direction based on vehicle count, creating an adaptive traffic management solution.

---

## 📦 Installation

### 🔧 Prerequisites

- Python 3.8 or higher  
- `pip` (Python package installer)  

### 📁 Setup

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-traffic-management.git
cd ai-traffic-management
```

#### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Linux/Mac:
source .venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Ensure model weights are in place

- Make sure your YOLO model weights file (`best.pt`) is in the `weight/` directory  
- If you don't have the weights, you'll need to train a YOLO model or use a pre-trained one  

---

## ▶️ Usage

### 🔧 Running the Application

```bash
uvicorn main_websocket:app --reload
```

### 🌐 Access the Web Interface

Open your browser and go to: [http://localhost:8000](http://localhost:8000)  
The web interface will load automatically.

### 🚦 Using the System

1. Upload 4 traffic video files (one for each intersection direction)  
2. Set the cycle time (total time for one complete signal cycle)  
3. Click **Start** to begin the simulation  
4. Watch as the system analyzes traffic and updates signal timings in real-time  

---

## 📂 File Structure

```
ai-traffic-management/
├── main_websocket.py          # FastAPI server and API endpoints
├── model.py                   # YOLO model initialization
├── getCount.py                # Vehicle counting logic
├── getTimings.py              # Signal timing calculation
├── setSequence.py             # Signal sequence optimization
├── send_data_websocket.py     # WebSocket communication handler
├── index_websocket.html       # Frontend web interface
├── requirements.txt           # Python dependencies
├── weight/                    # Directory for model weights
│   └── best.pt                # YOLO model weights
├── temp_videos/               # Temporary uploaded video storage
└── README.md                  # This file
```

---

## ⚙️ How It Works

- **Video Analysis**: The system analyzes frames from each traffic video at specific timestamps  
- **Vehicle Detection**: YOLO model detects and counts vehicles in each frame  
- **Timing Calculation**: Green light duration is calculated proportionally to vehicle count  
- **Signal Sequencing**: Intersections are prioritized based on traffic density  
- **Continuous Monitoring**: System progresses through video timeline, updating analysis every cycle  

---

## 📡 API Endpoints

- `GET /`: Serves the web interface  
- `POST /start`: Accepts video uploads and cycle time, starts traffic analysis  
- `WebSocket /ws`: Real-time communication for signal state updates  

---

## 🔧 Configuration

### Model Configuration

- Edit `model.py` to change the YOLO model weights file  
- Supported formats: `.pt` (PyTorch)  

### Timing Parameters

- **Cycle Time**: Total duration for complete signal cycle (user input)  
- **Yellow Time**: Fixed duration for yellow lights (default: 5 seconds)  
- **Minimum Green Time**: Minimum green light duration (default: 5 seconds)  

---

## 📋 Requirements

See `requirements.txt` for the complete dependency list. Key packages include:

- `fastapi`: Web framework for API  
- `uvicorn`: ASGI server  
- `opencv-python`: Video processing  
- `ultralytics`: YOLO model implementation  
- `websockets`: Real-time communication  
- `python-multipart`: File upload handling  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -am 'Add some feature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature
   ```
5. Create a Pull Request  

---

## 🧯 Troubleshooting

### Server won't start:
- Check if port 8000 is available  
- Ensure all dependencies are installed  
- Verify Python version compatibility  

### Videos won't upload:
- Check video format (MP4 recommended)  
- Ensure sufficient disk space  
- Verify file size limits  

### No vehicle detection:
- Confirm YOLO weights file is present and valid  
- Check video quality and resolution  
- Ensure proper lighting in video footage  

### WebSocket connection fails:
- Check browser console for errors  
- Verify server is running  
- Try refreshing the page  

---

## 📄 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- [Ultralytics YOLO](https://github.com/ultralytics/yolov5) for the object detection model  
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework  
- [OpenCV](https://opencv.org/) for video processing capabilities  

---

## 📬 Contact

For questions, issues, or contributions, please:

- Open an [issue on GitHub](https://github.com/yourusername/ai-traffic-management/issues)  
- Contact: [your-email@example.com]

---

> **Note**: This system is designed for simulation and educational purposes. For production traffic management systems, additional safety measures, redundancy, and compliance with traffic regulations would be required.
