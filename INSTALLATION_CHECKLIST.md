# guiClaw Installation Checklist

## ✅ Quick Installation (30 seconds)

- [ ] **Double-click** `guiClaw.command` on Desktop
- [ ] **Open browser** to http://localhost:8000
- [ ] **Start using** guiClaw!

## ✅ Prerequisites Check

- [ ] OpenClaw Gateway is running (`openclaw gateway start`)
- [ ] HTTP API enabled (`openclaw config set gateway.http.endpoints.responses.enabled true`)
- [ ] lsof installed (`brew install lsof`)

## ✅ Installation Methods

### Method 1: Desktop Shortcut
- [ ] Locate guiClaw folder on Desktop
- [ ] Double-click `guiClaw.command`
- [ ] Keep terminal window open

### Method 2: Terminal Script
- [ ] Open Terminal
- [ ] Run: `cd ~/Desktop/guiClaw && ./start.sh`
- [ ] Browser opens automatically

### Method 3: Manual Execution
- [ ] Open Terminal
- [ ] Run: `cd ~/Desktop/guiClaw`
- [ ] Run: `node proxy.js`
- [ ] Open browser to http://localhost:8000

## ✅ First-Time Setup (if needed)

- [ ] Download/clone guiClaw project
- [ ] Place folder on Desktop
- [ ] Make scripts executable:
  ```bash
  chmod +x ~/Desktop/guiClaw/start.sh
  chmod +x ~/Desktop/guiClaw/guiClaw.command
  ```

## ✅ Configuration Check

- [ ] Gateway settings verified:
  ```bash
  openclaw config set gateway.http.endpoints.responses.enabled true
  openclaw config set gateway.trustedProxies '["127.0.0.1"]'
  openclaw gateway restart
  ```

## ✅ Troubleshooting

### If port 8000 is busy:
- [ ] Kill existing process: `lsof -ti:8000 | xargs kill -9`
- [ ] Restart guiClaw

### If gateway connection fails:
- [ ] Check status: `openclaw status`
- [ ] Restart gateway: `openclaw gateway restart`

### If browser doesn't load:
- [ ] Clear browser cache
- [ ] Try different browser
- [ ] Verify server: `curl http://localhost:8000`

## ✅ Post-Installation

- [ ] Verify guiClaw is running
- [ ] Test basic chat functionality
- [ ] Explore different sections
- [ ] Configure WhatsApp if needed

## ✅ Version Check

- [ ] Current version: v3.1 (2026-02-16)
- [ ] Check VERSION.md for details

## ✅ Support Resources

- [ ] OpenClaw status: `openclaw status`
- [ ] OpenClaw logs: `openclaw logs --follow`
- [ ] Documentation: https://docs.openclaw.ai
- [ ] Detailed guide: INSTALLATION.md

---

**Need help?** Check INSTALLATION.md for detailed instructions or visit https://docs.openclaw.ai