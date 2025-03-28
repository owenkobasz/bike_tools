# Stem Viewer

This is a simple Streamlit app to compare two bike stem setups side by side,
factoring in spacer stack heights and headtube angles.  
The visualization shows stem positions in a clean side view.

## How to Run

1. Build the Docker image:

    docker build -t stem_viewer .

2. Run the app (automatically cleans up container after exit):

    docker run --rm -p 8501:8501 stem_viewer

3. Open in your browser:

    http://localhost:8501

## Optional: One-click run
You can use:

    ./run.sh

This will build and run the app automatically.

## Cleanup
If you want to remove all Docker images and cache (optional):

    docker system prune -a
