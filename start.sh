#!/bin/bash

# Port to check
PORT=8000

echo "🍙 Stopping any process on port $PORT..."
# Find PID of process using port 8000 and kill it
lsof -ti:$PORT | xargs kill -9 2>/dev/null

# Wait a moment
sleep 1

echo "🍙 Starting macClaw server..."
# Start server in background & save PID
cd ~/Desktop/guiClaw
node proxy.js &
SERVER_PID=$!

# Wait for server to start
sleep 2

echo "🍙 Opening macClaw..."
# Open in default browser
open "http://localhost:$PORT"

echo "✅ macClaw is running! (PID: $SERVER_PID)"
echo "Press Ctrl+C to stop."

# Keep script running to maintain background process
# wait $SERVER_PID

# openclaw tui
