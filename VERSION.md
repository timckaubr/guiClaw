# guiClaw v0.35

## Version Information
- **Version:** v0.35
- **Date:** 2026-02-18
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
- **v3.1:** Previous version with session key fix (45,647 bytes index.html)
- **v0.32:** GitHub release (2026-02-17)
- **v0.32.1:** Updated with OpenClaw gateway token integration (2026-02-18)
- **v0.33:** Updated with description before Update Token button (2026-02-18)
- **v0.34:** Updated with light blue copy buttons (2026-02-18)
- **v0.35:** Updated with all buttons using consistent font size (2026-02-18) - THIS VERSION

## Testing Results
- ✅ All navigation buttons clickable
- ✅ Section switching working (all 6 sections)
- ✅ Channel section accessible and displays correctly
- ✅ WhatsApp configuration interface working
- ✅ Connect and Show QR buttons functional
- ✅ Status display working
- ✅ Existing functionality preserved
- ✅ No breaking changes introduced

## Changelog v0.35 (2026-02-18)
### Changes
- **Title:** Changed from "macClaw" to "guiClaw"
- **Gateway Token:** Updated to current OpenClaw gateway token
- **Status Bar:** Removed (clean interface)
- **Version:** Updated to v0.32.1
- **Installation Guide:** Updated with 4-step installation process

### Installation Guide Updates
- **Step 1:** Installation and Uninstallation of OpenClaw in macOS
  - Added installation methods (script, npm, macOS app, wizard)
  - Added uninstallation methods (easy, manual, service removal)
  - Added verification steps
  - ✅ Added copy buttons for each command
  - ✅ Commands use light grey background (#f3f4f6) with dark grey text (#6b7280)
- **Step 2:** Setup of the OpenClaw environment
  - Added gateway startup instructions
  - Added HTTP API endpoint configuration
  - Added environment variable setup
  - Added configuration verification
  - ✅ Added copy buttons for each command
  - ✅ Commands use light grey background (#f3f4f6) with dark grey text (#6b7280)
- **Step 3:** Update guiClaw to the correct OpenClaw gateway token
  - Added token retrieval methods
  - ✅ Changed "3.2 Display the Gateway Token" to "3.2 Show the Current Gateway Token"
  - ✅ **Step 3.2 automatically loads token from openclaw.json on page load**
  - ✅ **Token displayed immediately in green, bold text (no button press needed)**
  - ✅ **Token value extracted cleanly from gateway response** (64-character hex only)
  - ✅ **Added "Copy" button next to token** to copy token to clipboard
  - ✅ **Added description "Update the token value of guiClaw"** before the Update Token button
  - ✅ **Added "Update Token" button** to update const AUTH_TOKEN in index.html
  - ✅ **Button "Automated Update" runs update script directly**
  - ✅ **Removed command display for step 3.2** (only shows token value)
  - ✅ **Updated token fetch command to use jq** (Method 2: `cat ~/.openclaw/openclaw.json | jq -r '.gateway.auth.token'`)
  - ✅ **Step 3.1 and 3.2 both use jq command** for token extraction
  - Added token update instructions (manual, sed, script)
  - Added token verification steps
  - Added troubleshooting for token issues
  - ✅ Added copy buttons for each command
  - ✅ Commands use light grey background (#f3f4f6) with dark grey text (#6b7280)
- **Step 4:** Refresh guiClaw
  - Added server stop instructions
  - Added start script execution
  - Added verification steps
  - Added troubleshooting for refresh issues
  - ✅ Added copy buttons for each command
  - ✅ Commands use light grey background (#f3f4f6) with dark grey text (#6b7280)

### UI Improvements
- ✅ **Copy buttons:** Added to every command in installation section
- ✅ **Copy button color:** Light blue background (#dbeafe) with blue text (#2563eb)
- ✅ **Copy button size:** Consistent size (padding: 0.5rem 0.75rem, font-size: 0.85rem)
- ✅ **All buttons:** Consistent font size (0.85rem) for all buttons (including Refresh guiClaw button)
- ✅ **Command styling:** Light grey background (#f3f4f6) with dark grey text (#6b7280)
- ✅ **Result display:** Results shown below buttons (not in troubleshooting section)
- ✅ **Button feedback:** "Copy" button changes to "✓ Copied!" for 2 seconds when clicked
- ✅ **Button feedback color:** Light blue background (#dbeafe) with blue text (#2563eb)
- ✅ **Section title:** Changed "Change Token" to "Automated Update (Recommended)"
- ✅ **Step 3.2:** Token value automatically displayed on page load (no button press needed)
- ✅ **Step 3.2:** Token extracted cleanly (64-character hex only, no extra text)
- ✅ **Step 3.2:** "Copy" button added next to token to copy to clipboard
- ✅ **Step 3.2:** "Update Token" button updates const AUTH_TOKEN in index.html
- ✅ **Step 3.2:** Token displayed in green (#10b981) with bold font
- ✅ **Step 3.3:** "Automated Update" button runs update script directly

### Files Modified
- `index.html` - Updated title, removed status bar, updated token
- `proxy.js` - Removed status-indicator.js serving code
- `VERSION.md` - Updated version and changelog
- `INSTALLATION.md` - Updated with 4-step installation process

### Backup
- **Location:** `~/Desktop/backups/guiClaw/guiClaw-v0.32.1`
- **Contents:** Complete backup of guiClaw v0.32.1
- **Purpose:** Version preservation before future updates

### Security
- ✅ Gateway bound to loopback (127.0.0.1) - only local access
- ✅ guiClaw running on localhost:8000 - only local access
- ⚠️ Token visible in guiClaw interface (for debugging)
- ✅ No external exposure

### Features Preserved
- ✅ Web-based GUI for OpenClaw
- ✅ File upload support
- ✅ Model switching capability
- ✅ WhatsApp configuration interface
- ✅ Clean interface (no status bar)