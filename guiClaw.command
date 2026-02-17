#!/bin/bash

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Port to check
PORT=8000

echo "🦁 Starting guiClaw..."

# Kill any existing process on port 8000
lsof -ti:$PORT | xargs kill -9 2>/dev/null

# Add Homebrew bin to PATH just in case
export PATH=$PATH:/opt/homebrew/bin:/usr/local/bin

# Start the server in the background
/opt/homebrew/bin/node proxy.js &
SERVER_PID=$!

# Wait for the server to initialize
sleep 2

# Open in default browser
open "http://localhost:$PORT"

echo "✅ guiClaw is running! (PID: $SERVER_PID)"
echo "Keep this window open while using guiClaw."
echo "Press Ctrl+C to stop."

# Wait for the process to finish
wait $SERVER_PID
