# guiClaw v0.32

## Version Information
- **Version:** v0.32
- **Date:** 2026-02-17
- **Source:** guiClaw project on GitHub
- **Status:** GitHub release

## Changes from v2.1
- **index.html:** Updated from 18,392 bytes to 22,188 bytes (added WhatsApp configuration)
- **Upload directory:** Contains 4 screenshots from previous sessions
- **All other files:** Identical to v2.1

## Channel Section Features
### WhatsApp Configuration
- **Status:** ✅ Working and functional
- **Location:** Between AI Assistant and AI Tools sections
- **Features:**
  - WhatsApp connection button
  - Show QR code button
  - Real-time status display
  - Configuration alerts

## Project Details
- **Name:** guiClaw (macClaw)
- **Description:** Custom OpenClaw Web GUI - local web interface for OpenClaw
- **URL:** http://localhost:8000
- **Status:** Currently running and connected to OpenClaw gateway

## Key Features
- Web-based GUI for OpenClaw
- File upload support
- Model switching capability
- Custom styling with CSS variables
- CORS enabled for cross-origin requests
- **NEW:** Channel section with WhatsApp configuration

## File Structure
```
~/Desktop/guiClaw v2.2/
├── README.md           # Project documentation
├── guiClaw.command     # Mac executable script
├── guiClaw             # Binary file
├── proxy.js            # Node.js proxy server
├── index.html          # Web interface (22,188 bytes)
├── package.json        # Dependencies (busboy, http-proxy)
├── package-lock.json
├── node_modules/       # Dependencies
├── start.sh            # Alternative startup script
└── upload/             # Upload directory (contains screenshots)
```

## Current Status (when running)
- **Proxy Server:** Running on port 8000
- **Gateway Connection:** ✅ Connected to OpenClaw gateway
- **Current Model:** xiaomi/mimo-v2-flash
- **Configured Models:** Xiaomi MiMo V2 Flash, Gemini 3 Pro Preview
- **Web Interface:** Accessible at http://localhost:8000

## How to Use
1. **Access:** Open http://localhost:8000 in browser
2. **Chat:** Use the web interface to interact with OpenClaw
3. **Upload:** Files can be uploaded through the interface
4. **Model Switching:** Can change AI models via the GUI
5. **Channel Section:** Click "Channel" in navigation to view WhatsApp configuration

## WhatsApp Configuration Features
- **Connect Button:** Initiates WhatsApp connection process
- **Show QR Button:** Displays QR code for WhatsApp linking
- **Status Display:** Shows current WhatsApp connection status
- **Alerts:** User-friendly messages for configuration guidance

## Startup Scripts
- **guiClaw.command:** Double-click to start (opens browser automatically)
- **start.sh:** Terminal script with more control
- **Manual:** `node ~/Desktop/guiClaw/proxy.js`

## Backup Notes
- This is a complete copy of the current guiClaw project
- All files and dependencies are included
- Upload directory contains previous session screenshots
- Ready to be used as a starting point for future development
- **WhatsApp configuration is working and functional**

## Version History
- **v1.0:** Initial version
- **v1.1:** Updated version
- **v2.0:** Previous version (18,070 bytes index.html, no Channel section)
- **v2.1:** Working Channel section (18,392 bytes index.html)
- **v2.2:** WhatsApp configuration (22,188 bytes index.html)
- **v2.3:** Additional features (42,987 bytes index.html)
- **v2.4:** More features (51,466 bytes index.html)
- **v3.0:** Updated version (42,939 bytes index.html)
- **v3.1:** Current version with session key fix (45,647 bytes index.html) - THIS VERSION

## Testing Results
- ✅ All navigation buttons clickable
- ✅ Section switching working (all 6 sections)
- ✅ Channel section accessible and displays correctly
- ✅ WhatsApp configuration interface working
- ✅ Connect and Show QR buttons functional
- ✅ Status display working
- ✅ Existing functionality preserved
- ✅ No breaking changes introduced