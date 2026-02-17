# guiClaw v0.32

## Overview
guiClaw is a custom web-based GUI for OpenClaw - a personal assistant running inside OpenClaw. This version (v0.32) provides a local web interface for interacting with OpenClaw through a browser.

## Features
- **Web-based Interface**: Access OpenClaw through your browser at http://localhost:8000
- **File Upload Support**: Upload files directly through the web interface
- **Model Switching**: Change AI models via the GUI
- **Custom Styling**: Clean, modern interface with CSS variables
- **CORS Enabled**: Cross-origin requests supported
- **WhatsApp Integration**: Channel section with WhatsApp configuration (v0.32 feature)

## Architecture
```
guiClaw/
├── index.html          # Main web interface
├── proxy.js            # Node.js proxy server (port 8000)
├── guiClaw.command     # Mac executable script
├── guiClaw             # Binary file
├── package.json        # Node.js dependencies
├── setup.sh            # Setup script
├── start.sh            # Startup script
├── upload/             # File upload directory
└── README.md           # This file
```

## Quick Start

### Prerequisites
- Node.js installed
- OpenClaw gateway running (default: http://localhost:18789)

### Installation
1. **Install dependencies**:
   ```bash
   cd ~/Desktop/guiClaw
   npm install
   ```

2. **Run the proxy server**:
   ```bash
   node proxy.js
   ```
   or use the startup script:
   ```bash
   ./start.sh
   ```

3. **Access the interface**:
   Open your browser and go to: http://localhost:8000

## Configuration

### OpenClaw Gateway Settings
The gateway must be configured to trust the proxy server:
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

### guiClaw Settings
- **Proxy URL**: http://localhost:8000/v1/responses
- **Gateway URL**: http://localhost:18789 (default)
- **Authentication**: Uses gateway token from openclaw.json

## Version Information
- **Version**: v0.32
- **Date**: 2026-02-17
- **Status**: Operational
- **Features**: WhatsApp configuration, session key fix, all previous features

## Features in v0.32
- ✅ Web-based GUI for OpenClaw
- ✅ File upload support
- ✅ Model switching capability
- ✅ Custom styling with CSS variables
- ✅ CORS enabled for cross-origin requests
- ✅ Channel section with WhatsApp configuration
- ✅ Session key fix (ECONNREFUSED error resolved)
- ✅ All navigation buttons working
- ✅ Section switching functional
- ✅ WhatsApp configuration interface working

## Usage
1. **Start the proxy server**: `node proxy.js` or `./start.sh`
2. **Open browser**: Navigate to http://localhost:8000
3. **Chat**: Use the web interface to interact with OpenClaw
4. **Upload files**: Use the upload feature in the interface
5. **Switch models**: Change AI models via the GUI
6. **WhatsApp**: Click "Channel" in navigation to view WhatsApp configuration

## Troubleshooting

### Common Issues
1. **Port already in use**: Kill any process using port 8000
   ```bash
   lsof -ti:8000 | xargs kill -9
   ```

2. **ECONNREFUSED errors**: Ensure OpenClaw gateway is running and configured correctly

3. **CORS issues**: Verify CORS is enabled in gateway configuration

### Logs
- Check `proxy.log` for proxy server logs
- Check OpenClaw gateway logs for connection issues

## Development
- **Source**: Custom OpenClaw Web GUI
- **Framework**: Vanilla JavaScript + HTML/CSS
- **Backend**: Node.js proxy server
- **Dependencies**: busboy, http-proxy

## License
This project is part of the OpenClaw ecosystem.

## Support
For issues or questions, refer to the OpenClaw documentation or community resources.

## Changelog
### v0.32 (2026-02-17)
- Initial GitHub release
- WhatsApp configuration feature
- Session key fix for ECONNREFUSED errors
- All navigation and section switching working
- File upload support
- Model switching capability

### Previous Versions
- v3.1: Current version with session key fix
- v3.0: Updated version
- v2.4: More features
- v2.3: Additional features
- v2.2: WhatsApp configuration
- v2.1: Working Channel section
- v2.0: Previous version
- v1.1: Updated version
- v1.0: Initial version