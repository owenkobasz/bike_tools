#!/bin/bash
docker build -t stem_viewer .
docker run -p 8501:8501 stem_viewer

