# Bike Tools

A collection of tools for bicycle setup, analysis, and comparison. This project provides utilities to help cyclists optimize their bike fit and compare different component configurations.

## 🚴‍♂️ Project Overview

This repo is designed to host various tools to help cyclists and bike fitters make informed decisions about bike setup.

### Stem Viewer
A Streamlit-based web application that allows you to compare two bike stem setups side by side, factoring in:
- Spacer stack heights
- Headtube angles
- Stem lengths and rise angles
- Frame reach and stack (in advanced mode)

**Features:**
- **Basic Mode**: Compare stems on the same bike
- **Advanced Mode**: Compare setups across different bikes with different frame geometries
- Visual side-by-side comparison with reach and stack differences
- Real-time calculations and updates

## 🚀 Quick Start

### Prerequisites
- Docker (recommended) or Python 3.7+
- For Python installation: pip

### Running with Docker

1. **One-click run:**
   ```bash
   cd stem-viewer
   ./run.sh
   ```

2. **Manual Docker build and run:**
   ```bash
   cd stem-viewer
   docker build -t stem_viewer .
   docker run --rm -p 8501:8501 stem_viewer
   ```

3. **Open in browser:**
   ```
   http://localhost:8501
   ```

## 📖 Usage Guide

### Basic Mode
Use this mode when comparing different stems on the same bike:
1. Set the headtube angle
2. Configure original stem (length, rise, spacers)
3. Configure new stem (length, rise, spacers)
4. View the visual comparison and reach/stack differences

### Advanced Mode
Use this mode when comparing setups across different bikes:
1. Configure original bike (frame reach/stack, headtube angle, stem, spacers)
2. Configure new bike (frame reach/stack, headtube angle, stem, spacers)
3. View the comprehensive comparison

## 🧹 Cleanup

To remove Docker images and cache (optional):
```bash
docker system prune -a
```

## 🤝 Contributing

This project is open to contributions! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Add new bike tools