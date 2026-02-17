# guiClaw Installation Guide

This guide provides detailed installation instructions for guiClaw, the custom OpenClaw web interface.

## Quick Start

For most users, the quickest way to get started is:

1. **Ensure OpenClaw Gateway is running:**
   ```bash
   openclaw gateway start
   ```

2. **Enable HTTP API (one-time setup):**
   ```bash
   openclaw config set gateway.http.endpoints.responses.enabled true
   openclaw gateway restart
   ```

3. **Start guiClaw:**
   - **Option A:** Double-click `guiClaw.command` on your Desktop
   - **Option B:** Run in terminal:
     ```bash
     cd ~/Desktop/guiClaw && ./start.sh
     ```

4. **Access the interface:**
   Open your browser to: **http://localhost:8000**

## Prerequisites

### System Requirements
- **Node.js 22+** (required for OpenClaw gateway)
- **macOS** (tested on macOS 15+)
- **Terminal access** (for command-line setup)

### OpenClaw Gateway
guiClaw requires the OpenClaw gateway to be running and configured:

1. **Start the gateway:**
   ```bash
   openclaw gateway start
   ```

2. **Verify gateway status:**
   ```bash
   openclaw status
   ```

3. **Enable HTTP API endpoints:**
   ```bash
   openclaw config set gateway.http.endpoints.responses.enabled true
   openclaw gateway restart
   ```

### Required Tools
- **lsof** (for port management): Install via Homebrew:
  ```bash
  brew install lsof
  ```

## Installation Methods

### Method 1: Desktop Shortcut (Recommended)

1. **Locate the guiClaw folder:**
   The guiClaw folder should be on your Desktop at:
   ```
   ~/Desktop/guiClaw/
   ```

2. **Double-click `guiClaw.command`:**
   This will:
   - Kill any existing process on port 8000
   - Start the guiClaw proxy server
   - Open your default browser to http://localhost:8000

3. **Keep the terminal window open** while using guiClaw.

### Method 2: Terminal Script

1. **Open Terminal** and navigate to the guiClaw folder:
   ```bash
   cd ~/Desktop/guiClaw
   ```

2. **Run the startup script:**
   ```bash
   ./start.sh
   ```

3. **Access the interface:**
   The script will automatically open your browser to http://localhost:8000

### Method 3: Manual Node.js Execution

1. **Navigate to the guiClaw folder:**
   ```bash
   cd ~/Desktop/guiClaw
   ```

2. **Start the proxy server:**
   ```bash
   node proxy.js
   ```

3. **Open your browser** to: http://localhost:8000

## Configuration

### Gateway Configuration

guiClaw requires specific gateway settings. Check your current configuration:

```bash
openclaw config get
```

Look for these settings:

```json
{
  "gateway": {
    "trustedProxies": ["127.0.0.1"],
    "http": {
      "endpoints": {
        "responses": {
          "enabled": true
        }
      }
    }
  }
}
```

If these settings are missing, add them:

```bash
# Enable HTTP responses endpoint
openclaw config set gateway.http.endpoints.responses.enabled true

# Add trusted proxy
openclaw config set gateway.trustedProxies '["127.0.0.1"]'

# Restart gateway
openclaw gateway restart
```

### guiClaw Configuration

The guiClaw proxy server uses these default settings:

- **Port:** 8000
- **Gateway URL:** http://localhost:18789
- **Upload Directory:** `~/Desktop/guiClaw/upload/`

To change the port, edit `proxy.js`:
```javascript
const PORT = 8000; // Change this value
```

## Troubleshooting

### Port 8000 Already in Use

If you get an error about port 8000 being in use:

```bash
# Find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9

# Or use the start.sh script which handles this automatically
./start.sh
```

### Gateway Connection Issues

If guiClaw can't connect to the OpenClaw gateway:

1. **Check gateway status:**
   ```bash
   openclaw status
   ```

2. **Verify gateway is running:**
   ```bash
   openclaw gateway status
   ```

3. **Restart the gateway:**
   ```bash
   openclaw gateway restart
   ```

4. **Check configuration:**
   ```bash
   openclaw config get gateway.http.endpoints.responses.enabled
   ```

### Browser Issues

If the interface doesn't load properly:

1. **Clear browser cache** (Ctrl+Shift+Delete or Cmd+Shift+Delete)
2. **Try a different browser** (Chrome, Firefox, Safari)
3. **Check if the server is running:**
   ```bash
   curl http://localhost:8000
   ```
   Should return HTML content.

### Permission Issues

If you get permission errors:

```bash
# Make scripts executable
chmod +x ~/Desktop/guiClaw/start.sh
chmod +x ~/Desktop/guiClaw/guiClaw.command

# Ensure Node.js is in your PATH
which node
```

## Advanced Configuration

### Custom Gateway URL

If your OpenClaw gateway runs on a different port or host, edit `index.html`:

```javascript
// Find this line in index.html
const GATEWAY_URL = 'http://127.0.0.1:8000/v1/responses';

// Change to your gateway URL
const GATEWAY_URL = 'http://your-gateway-host:port/v1/responses';
```

### Authentication

guiClaw uses the OpenClaw gateway authentication token. Ensure your token is configured:

```bash
# Check current token
openclaw config get gateway.token

# Set a custom token if needed
openclaw config set gateway.token "your-token-here"
```

### Custom Upload Directory

To change the upload directory, edit `proxy.js`:

```javascript
const UPLOAD_DIR = path.join(__dirname, 'your-custom-upload-dir');
```

## Development Setup

For development or customization:

1. **Install dependencies** (if modifying the code):
   ```bash
   cd ~/Desktop/guiClaw
   npm install
   ```

2. **Edit files:**
   - `index.html` - Main UI and styling
   - `proxy.js` - Server logic and routing
   - `start.sh` - Startup script
   - `guiClaw.command` - Desktop launcher

3. **Test changes:**
   ```bash
   # Kill existing server
   lsof -ti:8000 | xargs kill -9

   # Start with your changes
   node proxy.js
   ```

## Version Information

Current version: **v3.1** (2026-02-16)

For version details and changelog, see `VERSION.md`.

## Getting Help

If you encounter issues:

1. **Check the OpenClaw status:**
   ```bash
   openclaw status
   ```

2. **View OpenClaw logs:**
   ```bash
   openclaw logs --follow
   ```

3. **Check guiClaw proxy logs:**
   The proxy server logs to the terminal where it's running.

4. **Visit the OpenClaw documentation:**
   https://docs.openclaw.ai

## Next Steps

Once guiClaw is running:

1. **Explore the interface** - Click through different sections
2. **Try WhatsApp integration** - Configure WhatsApp channel
3. **Upload files** - Use the file upload feature
4. **Switch models** - Change AI models via the interface
5. **Customize** - Edit the UI to match your preferences

## Uninstallation

To remove guiClaw:

1. **Stop the server** (if running):
   ```bash
   lsof -ti:8000 | xargs kill -9
   ```

2. **Delete the folder:**
   ```bash
   rm -rf ~/Desktop/guiClaw
   ```

3. **Remove any desktop shortcuts:**
   Delete `guiClaw.command` if you moved it elsewhere.

4. **Revert OpenClaw configuration** (optional):
   ```bash
   openclaw config set gateway.http.endpoints.responses.enabled false
   openclaw gateway restart
   ```

---

**Note:** This installation guide is specific to guiClaw v3.1. For OpenClaw installation, see the [OpenClaw Installation Guide](https://docs.openclaw.ai/install).