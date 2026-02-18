# guiClaw Installation Guide

This guide provides detailed installation instructions for guiClaw, the custom OpenClaw web interface.

## Quick Start

For most users, the quickest way to get started is:

1. **Install OpenClaw on macOS** (Step 1)
2. **Setup OpenClaw environment** (Step 2)
3. **Update guiClaw with gateway token** (Step 3)
4. **Refresh guiClaw** (Step 4)

## Step 1: Installation and Uninstallation of OpenClaw in macOS

### Installation

#### Method A: Recommended Installation Script (macOS/Linux)

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

This will:
- Download and run the OpenClaw installer
- Install the OpenClaw CLI tool
- Set up the gateway service

#### Method B: Manual Installation via npm

```bash
npm install -g openclaw@latest
```

#### Method C: macOS App

1. **Download the macOS app** from [OpenClaw website](https://openclaw.ai)
2. **Drag OpenClaw.app to Applications folder**
3. **Run the app** from Applications

#### Method D: Onboarding Wizard

After installation, run the onboarding wizard:

```bash
openclaw onboard --install-daemon
```

This wizard will:
- Configure authentication
- Set up gateway settings
- Configure optional channels (WhatsApp, Discord, etc.)

### Verification

After installation, verify OpenClaw is working:

```bash
# Check CLI is installed
openclaw --version

# Check gateway status
openclaw gateway status

# Check gateway health
openclaw gateway health
```

### Uninstallation

#### Method A: Easy Uninstall (CLI still installed)

```bash
openclaw uninstall --all --yes --non-interactive
```

#### Method B: Manual Uninstallation Steps

1. **Stop the gateway service:**
   ```bash
   openclaw gateway stop
   ```

2. **Uninstall the gateway service:**
   ```bash
   openclaw gateway uninstall
   ```

3. **Delete state and config:**
   ```bash
   rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
   ```

4. **Delete workspace (optional):**
   ```bash
   rm -rf ~/.openclaw/workspace
   ```

5. **Remove CLI:**
   ```bash
   npm rm -g openclaw
   ```

6. **Remove macOS app (if installed):**
   ```bash
   rm -rf /Applications/OpenClaw.app
   ```

#### Method C: Manual Service Removal (CLI not installed)

If the CLI is missing but the service is still running:

```bash
# Stop and remove launchd service
launchctl bootout gui/$UID/bot.molt.gateway
rm -f ~/Library/LaunchAgents/bot.molt.gateway.plist
```

### System Requirements
- **Node.js 22+** (required for OpenClaw gateway)
- **macOS** (tested on macOS 15+)
- **Terminal access** (for command-line setup)

### Required Tools
- **lsof** (for port management): Install via Homebrew:
  ```bash
  brew install lsof
  ```

## Step 2: Setup of the OpenClaw Environment

After installing OpenClaw, you need to configure the environment for guiClaw to work properly.

### 2.1 Start the OpenClaw Gateway

```bash
openclaw gateway start
```

### 2.2 Verify Gateway Status

```bash
openclaw gateway status
```

Expected output:
```
Service: LaunchAgent (loaded)
Gateway: bind=loopback (127.0.0.1), port=18789
Runtime: running (pid XXXX, state active)
RPC probe: ok
```

### 2.3 Enable HTTP API Endpoints

This is the **critical step** for guiClaw to work:

```bash
openclaw config set gateway.http.endpoints.responses.enabled true
```

### 2.4 Restart the Gateway

After enabling the HTTP API, restart the gateway:

```bash
openclaw gateway restart
```

### 2.5 Verify Configuration

Check that the configuration was applied:

```bash
openclaw config get gateway.http.endpoints.responses.enabled
```

Expected output: `true`

### 2.6 Check Gateway Health

```bash
openclaw gateway health
```

Expected output:
```
Gateway Health
OK (XXXms)
WhatsApp: linked (auth age XXm)
Discord: ok (@Timclaw) (XXXms)
```

### 2.7 Enable Trusted Proxies (Optional but Recommended)

For better security and compatibility:

```bash
openclaw config set gateway.trustedProxies '["127.0.0.1"]'
openclaw gateway restart
```

### 2.8 Environment Variables (Optional)

If you need custom paths, set these environment variables:

```bash
# Set custom state directory
export OPENCLAW_STATE_DIR=~/.openclaw

# Set custom config path
export OPENCLAW_CONFIG_PATH=~/.openclaw/openclaw.json

# Set custom home directory
export OPENCLAW_HOME=~/.openclaw
```

### 2.9 Verify All Settings

Check your complete configuration:

```bash
openclaw config get
```

Look for these settings in the output:

```json
{
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "http": {
      "endpoints": {
        "responses": {
          "enabled": true
        }
      }
    },
    "trustedProxies": ["127.0.0.1"]
  }
}
```

## Step 3: Update guiClaw to the Correct OpenClaw Gateway Token

### 3.1 Get the Current Gateway Token

First, get your current OpenClaw gateway token:

```bash
cat ~/.openclaw/openclaw.json | jq -r '.gateway.auth.token'
```

If the token is not set or you need to generate a new one:

```bash
# Generate a new token
openclaw config set gateway.token "$(openssl rand -hex 32)"
```

### 3.2 Show the Current Gateway Token

The current OpenClaw gateway token is **automatically displayed** in guiClaw when the page loads. No button press needed!

- **Token displayed**: Green, bold text in the token display area
- **Token format**: Clean 64-character hexadecimal value (no extra text)
- **Token source**: Read directly from `~/.openclaw/openclaw.json`
- **Copy button**: Click **"Copy"** to copy the token to clipboard
- **Update description**: "Update the token value of guiClaw"
- **Update button**: Click **"Update Token"** to update the `const AUTH_TOKEN` in `index.html`

The token will be shown immediately when you open the Installation section.

### 3.3 Automated Update (Recommended)

Click the **"Automated Update"** button in guiClaw to automatically update guiClaw with the correct token.

This will run the update script:
```bash
cd ~/Desktop/guiClaw && ./update-guiclaw-project.sh
```

The script will:
- Get your current OpenClaw gateway token
- Update the `AUTH_TOKEN` in guiClaw's `index.html`
- Create a backup of the original file
- Verify the update was successful

**Note:** The script handles all the token management automatically.

### 3.4 Verify the Token Update

Check that the token was updated correctly:

```bash
grep "const AUTH_TOKEN" ~/Desktop/guiClaw/index.html
```

Expected output:
```
const AUTH_TOKEN = 'YOUR_ACTUAL_TOKEN_HERE';
```

### 3.5 Backup Current Configuration

Before making changes, create a backup:

```bash
cd ~/Desktop/guiClaw
cp index.html index.html.backup.$(date +%Y%m%d-%H%M%S)
```

## Step 4: Refresh guiClaw

### 4.1 Stop the Current guiClaw Server

If guiClaw is currently running, stop it:

```bash
# Method 1: Using pkill
pkill -f "node proxy.js"

# Method 2: Using lsof
lsof -ti:8000 | xargs kill -9 2>/dev/null

# Method 3: Using the start.sh script (which handles cleanup)
# The start.sh script will automatically kill existing processes
```

### 4.2 Run the Start Script

Navigate to the guiClaw folder and run the start script:

```bash
cd ~/Desktop/guiClaw
./start.sh
```

### 4.3 Verify guiClaw is Running

Check that the server is running:

```bash
# Check if port 8000 is listening
lsof -i :8000

# Or test the connection
curl http://localhost:8000
```

### 4.4 Access guiClaw

Open your browser and navigate to:

**http://localhost:8000**

### 4.5 Verify Token is Working

1. **Open the browser console** (F12 or Cmd+Option+I)
2. **Check the console for any errors**
3. **Test a simple message** to verify the connection works

### 4.6 Troubleshooting Token Issues

If you encounter token-related errors:

1. **Verify the token is correct:**
   ```bash
   cat ~/.openclaw/openclaw.json | jq -r '.gateway.auth.token'
   ```

2. **Check if the gateway is running:**
   ```bash
   openclaw gateway status
   ```

3. **Restart the gateway if needed:**
   ```bash
   openclaw gateway restart
   ```

4. **Update the token again:**
   ```bash
   cd ~/Desktop/guiClaw
   ./update-guiclaw-project.sh
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