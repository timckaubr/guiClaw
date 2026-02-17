# guiClaw - Custom OpenClaw Web GUI

A local web interface for OpenClaw.

## Quick Start

**Get started in 30 seconds:**

1. **Double-click** `guiClaw.command` on your Desktop
2. **Open your browser** to: **http://localhost:8000**
3. **Start chatting** with OpenClaw!

*That's it! No installation needed if guiClaw is already on your Desktop.*

## Installation

### Prerequisites

Before using guiClaw, ensure you have:

1. **OpenClaw Gateway** running:
   ```bash
   openclaw gateway start
   ```

2. **HTTP API enabled** (one-time setup):
   ```bash
   openclaw config set gateway.http.endpoints.responses.enabled true
   openclaw gateway restart
   ```

3. **lsof** installed (for port management):
   ```bash
   brew install lsof
   ```

### Installation Methods

#### Method 1: Desktop Shortcut (Recommended)

1. **Locate the guiClaw folder** on your Desktop
2. **Double-click** `guiClaw.command`
3. **Keep the terminal window open** while using guiClaw

#### Method 2: Terminal Script

```bash
cd ~/Desktop/guiClaw
./start.sh
```

#### Method 3: Manual Execution

```bash
cd ~/Desktop/guiClaw
node proxy.js
```

### First-Time Setup

If guiClaw is not on your Desktop:

1. **Download or clone** the guiClaw project
2. **Place the folder** on your Desktop
3. **Make scripts executable**:
   ```bash
   chmod +x ~/Desktop/guiClaw/start.sh
   chmod +x ~/Desktop/guiClaw/guiClaw.command
   ```

## How to Run

### Option A: Desktop Launcher (Easiest)

1. **Double-click** `guiClaw.command` on your Desktop
2. **Wait** for the terminal to show "guiClaw is running!"
3. **Browser will open automatically** to http://localhost:8000

### Option B: Terminal Command

```bash
cd ~/Desktop/guiClaw && ./start.sh
```

### Option C: Manual Node.js

```bash
cd ~/Desktop/guiClaw
node proxy.js
```

Then open your browser to: **http://localhost:8000**

## Configuration

### Gateway Settings

guiClaw requires specific OpenClaw gateway settings:

```bash
# Enable HTTP responses endpoint
openclaw config set gateway.http.endpoints.responses.enabled true

# Add trusted proxy
openclaw config set gateway.trustedProxies '["127.0.0.1"]'

# Restart gateway
openclaw gateway restart
```

### guiClaw Settings

- **Port:** 8000 (change in `proxy.js` if needed)
- **Gateway URL:** http://localhost:18789
- **Upload Directory:** `~/Desktop/guiClaw/upload/`

## Troubleshooting

### Port 8000 Already in Use

```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9

# Then start guiClaw again
cd ~/Desktop/guiClaw && ./start.sh
```

### Gateway Connection Issues

```bash
# Check gateway status
openclaw status

# Restart gateway if needed
openclaw gateway restart
```

### Browser Issues

- Clear browser cache (Ctrl+Shift+Delete)
- Try a different browser
- Ensure server is running: `curl http://localhost:8000`

## Customization

- **Edit `index.html`** to change the UI/CSS
- **Edit `proxy.js`** to change the port or server logic
- **Edit `start.sh`** or `guiClaw.command` to modify startup behavior

## Version

Current version: **v3.1** (2026-02-16)

See `VERSION.md` for detailed version history and changes.

## More Information

For detailed installation instructions, troubleshooting, and advanced configuration, see [INSTALLATION.md](INSTALLATION.md).

## Support

- **OpenClaw Status:** `openclaw status`
- **OpenClaw Logs:** `openclaw logs --follow`
- **Documentation:** https://docs.openclaw.ai
