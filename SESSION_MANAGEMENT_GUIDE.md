# Session & Memory Management Guide

## Overview
guiClaw v1.3.3 includes a comprehensive session and memory management system for OpenClaw. This allows you to manage sessions across all agents and control memory usage.

**Created by:** Riceball Mimo (formerly riceball) 🍚

## Current Session Status
- **Main Agent:** 384 sessions
- **Assistant Agent:** 2 sessions  
- **Developer Agent:** 3 sessions
- **Total:** 389 sessions

## Session Management Features

### 1. Session Count Display
- Real-time session counts for each agent
- Total session count across all agents
- Refresh button to update counts

### 2. Session Deletion Operations

#### Delete All Sessions
- **Action:** Deletes ALL sessions for ALL agents
- **Warning:** ⚠️ This cannot be undone!
- **Use case:** Complete cleanup when needed

#### Delete All Except Last
- **Action:** Keeps only the most recent session for each agent
- **Warning:** ⚠️ This cannot be undone!
- **Use case:** Clean up old sessions while keeping the current one

#### Delete Sessions Older Than X Hours
- **Action:** Deletes sessions older than specified hours
- **Options:** 1 hour or 24 hours
- **Use case:** Regular cleanup of old sessions

### 3. Session Details
- View session files for selected agent
- See session IDs, timestamps, and file sizes
- Monitor session activity

### 4. Session Statistics
- **Session Counts:** Total files per agent
- **Disk Usage:** Size of session directories
- **Total Statistics:** Combined stats across all agents

### 5. Memory Management
- **View Memory Files:** Browse MEMORY.md and daily memory files
- **Backup Memory:** Create timestamped backups of memory files
- **Clear Memory:** Remove all memory files (⚠️ destructive)
- **Export Sessions:** Create complete session backups

### 6. Session Pruning Configuration
- **Get Config:** View current pruning settings
- **Enable/Disable:** Toggle session pruning
- **Set TTL:** Configure time-to-live for sessions

## How to Use

1. **Open guiClaw** at http://localhost:8000
2. **Navigate to "Session"** section in the navigation bar
3. **View Current Status** - Check session counts
4. **Choose Operation** - Select the appropriate action
5. **Confirm** - Always confirm destructive operations

## Safety Features

### Confirmation Dialogs
- All destructive operations require confirmation
- Clear warnings about irreversible actions
- Multiple confirmation steps for critical operations

### Backup Options
- Memory backup before clearing
- Session export before deletion
- Timestamped backups for easy recovery

### Error Handling
- Graceful error messages
- Partial operation recovery
- Detailed error reporting

## API Endpoints

### Execute CLI Commands
```
POST /api/execute
Content-Type: application/json

{
  "command": "ls ~/.openclaw/agents/main/sessions/ | wc -l"
}
```

### Response Format
```json
{
  "output": "384\n",
  "stderr": ""
}
```

## Session Structure

### Main Agent
```
~/.openclaw/agents/main/sessions/
├── *.jsonl (session conversation logs)
├── *.jsonl.reset.* (reset logs)
└── sessions.json (session metadata)
```

### Assistant Agent
```
~/.openclaw/agents/assistant/sessions/
├── *.jsonl (session conversation logs)
├── *.jsonl.reset.* (reset logs)
└── sessions.json (session metadata)
```

### Developer Agent
```
~/.openclaw/agents/developer/sessions/
├── *.jsonl (session conversation logs)
├── *.jsonl.reset.* (reset logs)
└── sessions.json (session metadata)
```

## Best Practices

### Regular Maintenance
1. **Weekly:** Delete sessions older than 24 hours
2. **Monthly:** Export sessions for backup
3. **Quarterly:** Review and clean up memory files

### Before Major Operations
1. **Backup sessions** using "Export Sessions"
2. **Backup memory** using "Backup Memory"
3. **Document current state** using "View Details"

### After Cleanup
1. **Refresh session counts** to verify cleanup
2. **Check disk usage** to confirm space recovery
3. **Test OpenClaw** to ensure functionality

## Troubleshooting

### Session Count Not Updating
- Click "Refresh Counts" button
- Check if proxy server is running
- Verify OpenClaw gateway is active

### Operations Failing
- Check proxy server logs
- Verify file permissions
- Ensure enough disk space

### Memory Issues
- Use "Disk Usage" to check space
- Export sessions before cleanup
- Consider increasing TTL if sessions fill up quickly

## Version History
- **v1.3.3:** Added Session & Memory Management section
- **v1.3.2:** CSS extraction and modularization
- **v1.3.1:** Fixed agent display issues
- **v1.3:** Multi-agent management features

## Next Steps
- Test all session management operations
- Monitor disk usage over time
- Consider adding automated cleanup schedules
- Explore session pruning optimization