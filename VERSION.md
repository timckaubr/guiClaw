# guiClaw v0.6

## Version Information
- **Version:** v0.6
- **Date:** 2026-02-19
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
- **Latest backup:** v0.38 created on 2026-02-19 at ~/Desktop/backups/guiClaw/guiClaw-v0.38

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
- **v0.35:** Updated with all buttons using consistent font size (2026-02-18)
- **v0.36:** [Future version]
- **v0.37:** [Future version]
- **v0.38:** Previous version (2026-02-19)
- **v0.39:** Previous version (2026-02-19)
- **v4.0:** Previous version (2026-02-19)
- **v5.0:** Current version (2026-02-19) - THIS VERSION

## Changelog v0.39 (2026-02-19)
### Changes
- **Version:** Updated to v0.39
- **Date:** 2026-02-19
- **Status:** Current version

### Features Added
- **Channel Section:** Added after AI Assistant and before AI Tools
  - Current Channel Status display
  - Link WhatsApp (QR code process)
  - Approve Pairing Request
  - Configure Channel Settings
  - Restart Gateway
  - Test Integration
  - Allow List Management (view/add/remove numbers)

### AI Assistant Section Updates
- **Change 1:** Removed "Configured Models" display from AI model selector
  - Before: "Current Model: OpenClaw (Default)" + "Configured Models: GPT-4o, Gemini Pro, Claude 3"
  - After: Only "Current Model: xiaomi/mimo-v2-flash"
  - Reason: Cleaner interface, removed unnecessary information

- **Change 2:** Removed token usage display from Chat with AI section
  - Removed: Token usage poller function and polling logic
  - Removed: Token usage display span from Chat with AI header
  - Reason: Simplified interface, removed usage statistics display

- **Change 3:** Updated Chat with AI header to include current model
  - Before: "💬 Chat with AI"
  - After: "💬 Chat with AI (Current Model)"
  - Reason: Provides clearer context about which model is being used

- **Change 4:** Updated current model display to show actual model
  - Before: "OpenClaw (Default)"
  - After: "xiaomi/mimo-v2-flash"
  - Reason: Shows the actual current model instead of generic name

### GitHub Repository Updates
- **Total Commits Today:** 11 commits
- **Repository:** https://github.com/timckaubr/guiClaw.git
- **Branch:** main
- **Status:** All changes successfully pushed to GitHub

### Backup Created
- **Location:** ~/Desktop/Backups/guiClaw/guiClaw-v0.39
- **Purpose:** Complete backup of v0.39 for future reference
- **Contents:** All files and dependencies included

### Changelog v0.4 (2026-02-19)
### Changes
- **Version:** Updated to v0.4
- **Date:** 2026-02-19
- **Status:** Current version

### Features Added
- **Channel Section:** Added after AI Assistant and before AI Tools
  - Current Channel Status display
  - Link WhatsApp (QR code process)
  - Approve Pairing Request
  - Configure Channel Settings
  - Restart Gateway
  - Test Integration
  - Allow List Management (view/add/remove numbers)

### AI Assistant Section Updates
- **Change 1:** Removed "Configured Models" display from AI model selector
  - Before: "Current Model: OpenClaw (Default)" + "Configured Models: GPT-4o, Gemini Pro, Claude 3"
  - After: Only "Current Model: xiaomi/mimo-v2-flash"
  - Reason: Cleaner interface, removed unnecessary information

- **Change 2:** Removed token usage display from Chat with AI section
  - Removed: Token usage poller function and polling logic
  - Removed: Token usage display span from Chat with AI header
  - Reason: Simplified interface, removed usage statistics display

- **Change 3:** Updated Chat with AI header to include current model
  - Before: "💬 Chat with AI"
  - After: "💬 Chat with AI (Current Model)"
  - Reason: Provides clearer context about which model is being used

- **Change 4:** Updated current model display to show actual model
  - Before: "OpenClaw (Default)"
  - After: "xiaomi/mimo-v2-flash"
  - Reason: Shows the actual current model instead of generic name

### AI Tools Section Updates
- **Change 5:** Added comprehensive tool groups configuration section
  - Added 9 tool groups with enable/disable toggles:
    1. group:runtime (exec, bash, process)
    2. group:fs (read, write, edit, apply_patch)
    3. group:sessions (sessions_list, sessions_history, sessions_send, sessions_spawn, session_status)
    4. group:memory (memory_search, memory_get)
    5. group:web (web_search, web_fetch)
    6. group:ui (browser, canvas)
    7. group:automation (cron, gateway)
    8. group:messaging (message)
    9. group:nodes (nodes)
  - Added tool profiles information (minimal, coding, messaging, full)
  - Added Apply Tool Configuration button to save changes to OpenClaw config
  - Added Check All Tools button to check current tool status
  - Updated individual tool items to show group membership

### GitHub Repository Updates
- **Total Commits Today:** 14 commits
- **Repository:** https://github.com/timckaubr/guiClaw.git
- **Branch:** main
- **Status:** All changes successfully pushed to GitHub

### Backup Created
- **Location:** ~/Desktop/Backups/guiClaw/guiClaw-v4.0
- **Purpose:** Complete backup of v4.0 for future reference
- **Contents:** All files and dependencies included

### Testing Results
- ✅ All navigation buttons clickable
- ✅ Section switching working (all 6 sections)
- ✅ Channel section accessible and displays correctly
- ✅ WhatsApp configuration interface working
- ✅ Connect and Show QR buttons functional
- ✅ Status display working
- ✅ Existing functionality preserved
- ✅ No breaking changes introduced
- ✅ Current model displays correctly (xiaomi/mimo-v2-flash)
- ✅ Token usage display removed successfully
- ✅ Chat header updated correctly
- ✅ Tool groups configuration section working
- ✅ Enable/disable toggles functional
- ✅ Apply Tool Configuration button working

## Changelog v0.6 (2026-02-19)
### Changes
- **Version:** Updated to v0.6
- **Date:** 2026-02-19
- **Status:** Current version
- **Backup Location:** ~/Desktop/Backups/guiClaw/guiClaw-v0.6
- **Purpose:** Complete backup of current guiClaw project

### Features Added
- **Redesigned Troubleshooting Section:** Complete overhaul with step-by-step workflow
  - **1. OpenClaw Gateway:** Gateway Stop, Gateway Install, Gateway Restart, Reboot System
  - **2. Reinstall Gateway (All Steps):** Sequential execution of Stop → Install → Restart
  - **3. System Doctor:** Run Doctor Check, Auto-Fix Issues, Run Full Doctor (Non-Interactive)
  - **4. guiClaw Interface:** Reload Page, Reboot (start.sh), Clear Browser Cache & Reload

### Troubleshooting Section Updates
- **Step-by-Step Workflow:**
  - **1. OpenClaw Gateway:** Individual gateway commands
    - Gateway Stop: Stops the OpenClaw gateway
    - Gateway Install: Installs/reinstalls gateway
    - Gateway Restart: Restarts the gateway
    - Reboot System: Full system reboot

  - **2. Reinstall Gateway (All Steps):** Automated sequence
    - **Stop:** Stops the gateway
    - **Install:** Installs/reinstalls gateway
    - **Restart:** Restarts the gateway
    - **Run All Steps:** Executes all three steps in sequence with delays

  - **3. System Doctor:** Health checks and fixes
    - Run Doctor Check: Diagnostic check
    - Auto-Fix Issues: Automatic issue resolution
    - Run Full Doctor (Non-Interactive): Complete system check

  - **4. guiClaw Interface:** Interface management
    - Reload Page: Refresh browser
    - Reboot (start.sh): Restart guiClaw via start script
    - Clear Browser Cache & Reload: Clear cache and refresh

### JavaScript Functions Added
- `runReinstallGateway()`: Executes gateway reinstall sequence (Stop → Install → Restart)
  - Runs steps sequentially with 1-second delays
  - Logs progress to troubleshooting log
  - Handles errors gracefully
  - Shows completion message

### UI Improvements
- **Consistent Styling:** Matches AI Skills section design
- **Grid Layout:** Responsive button arrangement
- **Color Coding:**
  - Gateway commands: Neutral (white background)
  - Reinstall sequence: Yellow/amber (warning)
  - System Doctor: Blue/green (health)
  - Interface commands: Grey/pink (interface)
- **Sequential Execution:** Clear step-by-step workflow
- **Progress Logging:** Real-time feedback in troubleshooting log

### Testing Results
- ✅ All troubleshooting buttons clickable
- ✅ Individual commands working
- ✅ Sequential execution working (Stop → Install → Restart)
- ✅ Progress logging functional
- ✅ Error handling working
- ✅ Consistent styling with AI Skills section
- ✅ No breaking changes introduced
- ✅ Existing functionality preserved

## Changelog v0.51 (2026-02-19)
### Changes
- **Version:** Updated to v0.51
- **Date:** 2026-02-19
- **Status:** Current version

### Features Added
- **Redesigned AI Skills Section:** Complete overhaul based on OpenClaw documentation
  - Skills Configuration Panel with allowBundled, extraDirs, watchSkills, nodeManager settings
  - Enable/Disable buttons for each skill
  - Config buttons for per-skill configuration
  - Skill locations and precedence information
  - Slash Commands reference section
  - ClawHub integration button

### AI Skills Section Updates
- **Skills Configuration:**
  - Allow Bundled Skills: Comma-separated list of bundled skills to allow
  - Extra Skill Directories: Additional skill directories (lowest precedence)
  - Watch Skills for Changes: Enable/disable auto-refresh
  - Node Manager: npm/pnpm/yarn/bun preference
  - Apply Configuration button to save changes
  - Check Current Config button to view current settings

- **Skills List:**
  - Each skill now has Enable/Disable buttons
  - Each skill has Config button for per-skill settings
  - Shows skill type (Bundled/Managed/Workspace)
  - Shows skill location
  - Status indicators for each skill

- **Skill Locations & Precedence:**
  - Workspace skills: &lt;workspace&gt;/skills (highest precedence)
  - Managed/local skills: ~/.openclaw/skills (shared across agents)
  - Bundled skills: Shipped with OpenClaw install (lowest precedence)
  - Precedence: Workspace → Managed/local → Bundled

- **Slash Commands Reference:**
  - Directives: /think, /verbose, /reasoning, /elevated, /exec, /model, /queue
  - Inline shortcuts: /help, /commands, /status, /whoami

- **ClawHub Integration:**
  - Button to show ClawHub options
  - Search, install, update, publish skills
  - Links to https://clawhub.ai

### JavaScript Functions Added
- `toggleSkill(skillName)`: Enable/disable individual skills
- `configureSkill(skillName)`: Show configuration options for a skill
- `applySkillsConfig()`: Apply skills configuration changes
- `checkSkillsConfig()`: Check current skills configuration
- `showClawHubSection()`: Show ClawHub integration options

### GitHub Repository Updates
- **Total Commits Today:** 18 commits
- **Repository:** https://github.com/timckaubr/guiClaw.git
- **Branch:** main
- **Status:** All changes successfully pushed to GitHub

### Backup Created
- **Location:** ~/Desktop/Backups/guiClaw/guiClaw-v5.1
- **Purpose:** Complete backup of v5.1 for future reference
- **Contents:** All files and dependencies included

### Testing Results
- ✅ Skills Configuration panel working
- ✅ Enable/Disable buttons functional
- ✅ Config buttons functional
- ✅ Skill locations information displayed
- ✅ Slash commands reference displayed
- ✅ ClawHub button functional
- ✅ All navigation buttons clickable
- ✅ Section switching working (all 7 sections)
- ✅ Existing functionality preserved
- ✅ No breaking changes introduced

## Changelog v0.5 (2026-02-19)
### Changes
- **Version:** Updated to v0.5
- **Date:** 2026-02-19
- **Status:** Current version

### Features Added
- **Browser Section:** Added after AI Tools and before AI Skills
  - 6 browser profiles with enable/disable toggles:
    1. profile:openclaw (Dedicated, isolated Chromium browser)
    2. profile:chrome (Extension relay to existing Chrome tabs)
    3. profile:work (Work-specific browser profile)
    4. profile:remote (Remote CDP browser connection)
    5. profile:browserless (Hosted Chromium service via Browserless.io)
    6. profile:default (System default Chromium-based browser)
  - Browser configuration options information
  - Apply Browser Configuration button
  - Check Browser Status button
  - Browser Quick Actions: Start, Stop, Restart, Open URL, Take Screenshot, Get Snapshot
  - Individual browser profile status indicators

### AI Assistant Section Updates
- **Change 1:** Removed "Configured Models" display from AI model selector
  - Before: "Current Model: OpenClaw (Default)" + "Configured Models: GPT-4o, Gemini Pro, Claude 3"
  - After: Only "Current Model: xiaomi/mimo-v2-flash"
  - Reason: Cleaner interface, removed unnecessary information

- **Change 2:** Removed token usage display from Chat with AI section
  - Removed: Token usage poller function and polling logic
  - Removed: Token usage display span from Chat with AI header
  - Reason: Simplified interface, removed usage statistics display

- **Change 3:** Updated Chat with AI header to include current model
  - Before: "💬 Chat with AI"
  - After: "💬 Chat with AI (Current Model)"
  - Reason: Provides clearer context about which model is being used

- **Change 4:** Updated current model display to show actual model
  - Before: "OpenClaw (Default)"
  - After: "xiaomi/mimo-v2-flash"
  - Reason: Shows the actual current model instead of generic name

### AI Tools Section Updates
- **Change 5:** Added comprehensive tool groups configuration section
  - Added 9 tool groups with enable/disable toggles:
    1. group:runtime (exec, bash, process)
    2. group:fs (read, write, edit, apply_patch)
    3. group:sessions (sessions_list, sessions_history, sessions_send, sessions_spawn, session_status)
    4. group:memory (memory_search, memory_get)
    5. group:web (web_search, web_fetch)
    6. group:ui (browser, canvas)
    7. group:automation (cron, gateway)
    8. group:messaging (message)
    9. group:nodes (nodes)
  - Added tool profiles information (minimal, coding, messaging, full)
  - Added Apply Tool Configuration button to save changes to OpenClaw config
  - Added Check All Tools button to check current tool status
  - Updated individual tool items to show group membership

### GitHub Repository Updates
- **Total Commits Today:** 17 commits
- **Repository:** https://github.com/timckaubr/guiClaw.git
- **Branch:** main
- **Status:** All changes successfully pushed to GitHub

### Backup Created
- **Location:** ~/Desktop/Backups/guiClaw/guiClaw-v5.0
- **Purpose:** Complete backup of v5.0 for future reference
- **Contents:** All files and dependencies included

### Testing Results
- ✅ All navigation buttons clickable
- ✅ Section switching working (all 7 sections)
- ✅ Channel section accessible and displays correctly
- ✅ WhatsApp configuration interface working
- ✅ Connect and Show QR buttons functional
- ✅ Status display working
- ✅ Existing functionality preserved
- ✅ No breaking changes introduced
- ✅ Current model displays correctly (xiaomi/mimo-v2-flash)
- ✅ Token usage display removed successfully
- ✅ Chat header updated correctly
- ✅ Tool groups configuration section working
- ✅ Enable/disable toggles functional
- ✅ Apply Tool Configuration button working
- ✅ Browser section working
- ✅ Browser profile toggles functional
- ✅ Browser quick actions working

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