#!/bin/bash

# Configuration
CONFIG_FILE="$HOME/.openclaw/openclaw.json"
GUI_DIR="guiClaw"
INDEX_FILE="$GUI_DIR/index.html"

# Ensure jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed. Please install jq first."
    exit 1
fi

echo "🔧 Configuring OpenClaw environment..."

# 1. Gateway & CORS Configuration
# Add localhost:8000 to allowed origins if not present
echo "Updating CORS configuration in $CONFIG_FILE..."
jq '.gateway.controlUi.allowedOrigins += ["http://127.0.0.1:8000", "http://localhost:8000"] | .gateway.controlUi.allowedOrigins |= unique' "$CONFIG_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
echo "✅ CORS updated."

# 2. Update token in guiClaw/index.html
TOKEN=$(jq -r '.gateway.auth.token' "$CONFIG_FILE")

if [ -f "$INDEX_FILE" ]; then
    echo "Updating token in $INDEX_FILE..."
    # Replace existing token value with the new one
    # Assuming format: token: "..."
    sed -i '' "s/token: *['\"][^'\"]*['\"]/token: \"$TOKEN\"/" "$INDEX_FILE"
    echo "✅ Token updated."
else
    echo "⚠️  $INDEX_FILE not found. skipping token update."
fi

# 3. Restart Gateway
echo "Restarting OpenClaw Gateway..."
openclaw gateway restart

echo "🎉 Setup complete! Gateway restarted."
