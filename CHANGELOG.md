# guiClaw Changelog

## Version 1.5 (2026-02-22)

### New Features
- **Mobile Link Section**: Added new "Link to Mobile" section for mobile device access
- **Mobile Access**: Access OpenClaw from mobile devices using QR codes and dynamic DNS
- **Connection URLs**: Local network and internet access options
- **No-IP Integration**: Dynamic DNS setup for remote access
- **Port Forwarding**: Router configuration guide for external access
- **IP Detection**: Built-in IP address detection tool
- **Navigation**: Added "Mobile Link" button to navigation bar (8th section)

### Documentation
- **README.md**: Updated with Mobile Link feature documentation
- **VERSION.md**: Updated with v1.5 changelog
- **CHANGELOG.md**: Created new changelog file

### Technical Changes
- **index.html**: Added Mobile Link section with 4-step setup guide
- **styles.css**: Added styles for Mobile Link section
- **Version**: Updated from v1.4.2 to v1.5

### GitHub Upload
- **Backup**: Complete backup created at ~/Desktop/Backups/guiClaw/guiClaw-v1.5
- **Preparation**: Project prepared for GitHub upload with complete documentation
- **Organization**: All files properly organized for GitHub release

## Version 1.4.2 (2026-02-20)

### Multi-Agent Flow
- Combined agent session selection and inter-agent chat into unified flow
- User selects agent → shows loading sessions → user selects session → starts chat
- Added numbered steps (1-4) for clear workflow guidance
- Enhanced chat display with timestamps
- Removed sessionKey input field
- Added reset button to start over the flow

## Version 1.4.1 (2026-02-20)

### Multi-Agent Fix
- Fixed multi-agent session loading in guiClaw
- Fixed OpenClaw CLI command formats for session listing
- Changed API endpoint from /v1/responses to /api/execute
- Added JSON parsing for session list output
- Added agent path mapping for session store locations

## Version 1.4 (2026-02-20)

### Branding Updates
- Updated navigation bar brand text to "Riceball Mimo" (formerly riceball)
- Moved brand to center above navigation bar
- Updated header and navigation CSS for proper layout
- Added author information to all documentation files

## Version 1.3.3 (2026-02-19)

### Session & Memory Management
- Added "Session & Memory Management" section
- Session operations: Delete all sessions, delete all except last, delete sessions older than X hours
- Memory management: View memory files, backup memory, clear memory, export sessions
- Session statistics: View session counts, disk usage, and statistics
- Pruning configuration: Get, enable, disable, and configure session pruning
- API endpoint: Added `/api/execute` for CLI command execution

## Version 1.3.2 (2026-02-19)

### Modularization
- Started Phase 1 - CSS extraction to external file
- Extracted 8.5KB of CSS from index.html to styles.css
- Updated proxy.js to serve CSS files
- Reduced index.html from 236KB to 227KB
- Benefits: Better organization, improved maintainability, better caching

## Version 1.3.1 (2026-02-19)

### Multi-Agent Fix
- Fixed List All Agents button to display results in correct location (Inter-Agent Chat section)
- Updated `listAllAgents()` function to display results in `agentChatDisplay` element

## Version 1.3 (2026-02-19)

### Multi-Agent Management
- Added new Multi-Agent section after Skills section
- Added "Multi-Agent" button between Skills and Troubleshooting
- Inter-Agent Chat: Chat box for sending messages to other agents with session selection
- Session Management: Filter sessions by type, view session history, and manage sessions
- Agent Configuration: Create new agents, view current configuration
- Routing Bindings: Add, view, and clear routing bindings between channels and agents
- Added 15+ new functions for multi-agent management

## Version 1.2 (2026-02-19)

### Previous Features
- All features from previous versions
- WhatsApp configuration
- File upload support
- Model switching capability
- Custom styling with CSS variables
- CORS enabled for cross-origin requests
- 4-Step Installation Guide with copy buttons
- Token auto-loads on page load
- Gateway token integration with OpenClaw gateway
- Fixed authentication token issues (401 errors resolved)
- Updated GitHub repository with correct tokens
- Improved stability and reliability
- Browser Section: 6 browser profiles with enable/disable toggles
- Tool Groups Configuration: 9 tool groups with enable/disable toggles
- Enhanced UI: 7 navigation sections (Assistant, Channel, Tools, Browser, Skills, Troubleshooting, etc.)
- Current Model Display: Shows actual model name (xiaomi/mimo-v2-flash)
- Token Usage Display: Removed for cleaner interface
- Tool Profiles: Minimal, coding, messaging, full profiles
- Browser Quick Actions: Start, Stop, Restart, Open URL, Take Screenshot, Get Snapshot

## Version 1.1 (2026-02-19)

### Troubleshooting Redesign
- Redesigned troubleshooting section with installation section style
- Individual result boxes for each command instead of single dark terminal log
- Added copy buttons for all commands
- Results now show below each button instead of in a separate log
- Color-coded result boxes for different operation types

## Version 1.0 (2026-02-19)

### Initial Release
- Web-based GUI for OpenClaw
- File upload support
- Model switching capability
- Custom styling with CSS variables
- CORS enabled for cross-origin requests
- 4-Step Installation Guide with copy buttons
- Token auto-loads on page load
- Gateway token integration with OpenClaw gateway
- Fixed authentication token issues (401 errors resolved)
- Updated GitHub repository with correct tokens
- Improved stability and reliability

## Version 0.9.5 (2026-02-19)

### Previous Versions
- Complete version history from v0.32 to v0.9.5
- All features from previous versions included
- GitHub repository updates
- Backup creation for each version
- Testing results and verification