#!/bin/bash

echo "Building Stem Viewer image..."
docker build -t stem_viewer .

echo "Running Stem Viewer app on http://localhost:8501"
docker run --rm -p 8501:8501 stem_viewer
