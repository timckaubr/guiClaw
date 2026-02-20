#!/usr/bin/env python3
import re

# Read the original file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Replace the loadAgentSessions function
old_load_agent_sessions = '''        async function loadAgentSessions() {
            const agentSelect = document.getElementById('sessionAgentSelect');
            const sessionSelect = document.getElementById('sessionSelect');
            const detailsDisplay = document.getElementById('sessionDetailsDisplay');
            
            const selectedAgent = agentSelect.value;
            
            if (!selectedAgent) {
                sessionSelect.innerHTML = '<option value=\"\">-- Select Session --</option>';
                detailsDisplay.innerHTML = '<div style=\"color: #6b7280; font-style: italic;\">Select an agent to see available sessions...</div>';
                return;
            }
            
            // Show loading state
            detailsDisplay.innerHTML = '<div style=\"color: #6b7280; font-style: italic;\">Loading sessions for ' + selectedAgent + ' agent...</div>';
            
            try {
                const response = await fetch('/v1/responses', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${AUTH_TOKEN}`,
                        'x-openclaw-agent-id': 'main'
                    },
                    body: JSON.stringify({
                        model: 'openclaw',
                        input: `[COMMAND] openclaw sessions list --kinds ${selectedAgent}`
                    })
                });
                
                const data = await response.json();
                let result = '';
                
                if (data.choices?.[0]?.message?.content) {
                    result = data.choices[0].message.content.trim();
                } else if (data.output) {
                    const msg = data.output.find(item => item.type === 'message' && item.role === 'assistant');
                    if (msg && msg.content) {
                        result = msg.content.filter(p => p.type === 'output_text').map(p => p.text).join('').trim();
                    }
                }
                
                // Parse the session list and populate the dropdown
                const sessions = parseSessions(result);
                
                if (sessions.length === 0) {
                    sessionSelect.innerHTML = '<option value=\"\">-- No sessions found --</option>';
                    detailsDisplay.innerHTML = '<div style=\"color: #6b7280; font-style: italic;\">No sessions found for ' + selectedAgent + ' agent.</div>';
                    return;
                }
                
                // Populate session dropdown
                sessionSelect.innerHTML = '<option value=\"\">-- Select Session --</option>';
                sessions.forEach(session => {
                    const option = document.createElement('option');
                    option.value = session.key;
                    option.textContent = `${session.key} (${session.updatedAt || 'unknown'})`;
                    sessionSelect.appendChild(option);
                });
                
                // Show session details
                detailsDisplay.innerHTML = `<div style=\"color: #111827; font-weight: 600; margin-bottom: 0.5rem;\">Available sessions for ${selectedAgent} agent:</div>` +
                    sessions.map(s => `• ${s.key} - ${s.updatedAt || 'unknown'}`).join('<br>');
                
            } catch (err) {
                detailsDisplay.innerHTML = `<div style=\"color: #ef4444;\">Error: ${err.message}</div>`;
                sessionSelect.innerHTML = '<option value=\"\">-- Error loading sessions --</option>';
            }
        }'''

new_load_agent_sessions = '''        async function loadAgentSessions() {
            const agentSelect = document.getElementById('sessionAgentSelect');
            const sessionSelect = document.getElementById('sessionSelect');
            const detailsDisplay = document.getElementById('sessionDetailsDisplay');
            
            const selectedAgent = agentSelect.value;
            
            if (!selectedAgent) {
                sessionSelect.innerHTML = '<option value=\"\">-- Select Session --</option>';
                detailsDisplay.innerHTML = '<div style=\"color: #6b7280; font-style: italic;\">Select an agent to see available sessions...</div>';
                return;
            }
            
            // Show loading state
            detailsDisplay.innerHTML = '<div style=\"color: #6b7280; font-style: italic;\">Loading sessions for ' + selectedAgent + ' agent...</div>';
            
            try {
                // Map agent name to session store path
                const agentPaths = {
                    'main': '~/.openclaw/agents/main/sessions/sessions.json',
                    'assistant': '~/.openclaw/agents/assistant/sessions/sessions.json',
                    'developer': '~/.openclaw/agents/developer/sessions/sessions.json'
                };
                
                const sessionStorePath = agentPaths[selectedAgent];
                
                const response = await fetch('/api/execute', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        command: `openclaw sessions list --store ${sessionStorePath} --json`
                    })
                });
                
                const data = await response.json();
                let result = '';
                
                if (data.output) {
                    result = data.output.trim();
                }
                
                // Parse the session list and populate the dropdown
                const sessions = parseSessions(result);
                
                if (sessions.length === 0) {
                    sessionSelect.innerHTML = '<option value=\"\">-- No sessions found --</option>';
                    detailsDisplay.innerHTML = '<div style=\"color: #6b7280; font-style: italic;\">No sessions found for ' + selectedAgent + ' agent.</div>';
                    return;
                }
                
                // Populate session dropdown
                sessionSelect.innerHTML = '<option value=\"\">-- Select Session --</option>';
                sessions.forEach(session => {
                    const option = document.createElement('option');
                    option.value = session.key;
                    option.textContent = `${session.key} (${session.updatedAt || 'unknown'})`;
                    sessionSelect.appendChild(option);
                });
                
                // Show session details
                detailsDisplay.innerHTML = `<div style=\"color: #111827; font-weight: 600; margin-bottom: 0.5rem;\">Available sessions for ${selectedAgent} agent:</div>` +
                    sessions.map(s => `• ${s.key} - ${s.updatedAt || 'unknown'}`).join('<br>');
                
            } catch (err) {
                detailsDisplay.innerHTML = `<div style=\"color: #ef4444;\">Error: ${err.message}</div>`;
                sessionSelect.innerHTML = '<option value=\"\">-- Error loading sessions --</option>';
            }
        }'''

# Fix 2: Replace the parseSessions function
old_parse_sessions = '''        // Parse session list from OpenClaw output
        function parseSessions(sessionListText) {
            const sessions = [];
            
            if (!sessionListText || sessionListText.includes('No sessions found')) {
                return sessions;
            }
            
            // Parse session list (format: "key: sessionKey, updated: timestamp")
            const lines = sessionListText.split('\\n');
            lines.forEach(line => {
                const match = line.match(/key:\\s*([^,]+),\\s*updated:\\s*([^,]+)/);
                if (match) {
                    sessions.push({
                        key: match[1].trim(),
                        updatedAt: match[2].trim()
                    });
                }
            });
            
            return sessions;
        }'''

new_parse_sessions = '''        // Parse session list from OpenClaw output
        function parseSessions(sessionListText) {
            const sessions = [];
            
            if (!sessionListText || sessionListText.includes('No sessions found')) {
                return sessions;
            }
            
            try {
                // Parse JSON output from OpenClaw
                const data = JSON.parse(sessionListText);
                
                if (data.sessions && Array.isArray(data.sessions)) {
                    data.sessions.forEach(session => {
                        // Convert Unix timestamp to readable date
                        let updatedAt = 'unknown';
                        if (session.updatedAt) {
                            const date = new Date(session.updatedAt);
                            updatedAt = date.toLocaleString();
                        }
                        
                        sessions.push({
                            key: session.key,
                            updatedAt: updatedAt
                        });
                    });
                }
            } catch (err) {
                // Fallback to old parsing if JSON fails
                const lines = sessionListText.split('\\n');
                lines.forEach(line => {
                    const match = line.match(/key:\\s*([^,]+),\\s*updated:\\s*([^,]+)/);
                    if (match) {
                        sessions.push({
                            key: match[1].trim(),
                            updatedAt: match[2].trim()
                        });
                    }
                });
            }
            
            return sessions;
        }'''

# Fix 3: Replace the loadSelectedSession function
old_load_selected_session = '''        // Load selected session for the selected agent
        async function loadSelectedSession() {
            const agentSelect = document.getElementById('sessionAgentSelect');
            const sessionSelect = document.getElementById('sessionSelect');
            const detailsDisplay = document.getElementById('sessionDetailsDisplay');
            
            const selectedAgent = agentSelect.value;
            const selectedSession = sessionSelect.value;
            
            if (!selectedAgent || !selectedSession) {
                alert('Please select both an agent and a session.');
                return;
            }
            
            // Show loading state
            detailsDisplay.innerHTML = `<div style=\"color: #6b7280; font-style: italic;\">Loading session ${selectedSession} for ${selectedAgent} agent...</div>`;
            
            try {
                const response = await fetch('/v1/responses', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${AUTH_TOKEN}`,
                        'x-openclaw-agent-id': 'main'
                    },
                    body: JSON.stringify({
                        model: 'openclaw',
                        input: `[COMMAND] openclaw sessions send --session ${selectedSession} --agent ${selectedAgent} --message "Load session ${selectedSession}"`
                    })
                });
                
                const data = await response.json();
                let result = '';
                
                if (data.choices?.[0]?.message?.content) {
                    result = data.choices[0].message.content.trim();
                } else if (data.output) {
                    const msg = data.output.find(item => item.type === 'message' && item.role === 'assistant');
                    if (msg && msg.content) {
                        result = msg.content.filter(p => p.type === 'output_text').map(p => p.text).join('').trim();
                    }
                }
                
                detailsDisplay.innerHTML = `<div style=\"color: #10b981; font-weight: 600;\">✅ Session loaded successfully!</div>` +
                    `<div style=\"margin-top: 0.5rem; color: #374151;\">Agent: ${selectedAgent}</div>` +
                    `<div style=\"color: #374151;\">Session: ${selectedSession}</div>` +
                    `<div style=\"margin-top: 0.5rem; font-size: 0.8rem; color: #6b7280;\">${result || 'Session loaded successfully.'}</div>`;
                
            } catch (err) {
                detailsDisplay.innerHTML = `<div style=\"color: #ef4444;\">Error: ${err.message}</div>`;
            }
        }'''

new_load_selected_session = '''        // Load selected session for the selected agent
        async function loadSelectedSession() {
            const agentSelect = document.getElementById('sessionAgentSelect');
            const sessionSelect = document.getElementById('sessionSelect');
            const detailsDisplay = document.getElementById('sessionDetailsDisplay');
            
            const selectedAgent = agentSelect.value;
            const selectedSession = sessionSelect.value;
            
            if (!selectedAgent || !selectedSession) {
                alert('Please select both an agent and a session.');
                return;
            }
            
            // Show loading state
            detailsDisplay.innerHTML = `<div style=\"color: #6b7280; font-style: italic;\">Loading session ${selectedSession} for ${selectedAgent} agent...</div>`;
            
            try {
                // Map agent name to session key
                const agentKeys = {
                    'main': 'agent:main:main',
                    'assistant': 'agent:assistant:main',
                    'developer': 'agent:developer:main'
                };
                
                const sessionKey = agentKeys[selectedAgent];
                
                const response = await fetch('/api/execute', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        command: `openclaw agent --session-id ${selectedSession} --message "Load session ${selectedSession}"`
                    })
                });
                
                const data = await response.json();
                let result = '';
                
                if (data.output) {
                    result = data.output.trim();
                }
                
                detailsDisplay.innerHTML = `<div style=\"color: #10b981; font-weight: 600;\">✅ Session loaded successfully!</div>` +
                    `<div style=\"margin-top: 0.5rem; color: #374151;\">Agent: ${selectedAgent}</div>` +
                    `<div style=\"color: #374151;\">Session: ${selectedSession}</div>` +
                    `<div style=\"margin-top: 0.5rem; font-size: 0.8rem; color: #6b7280;\">${result || 'Session loaded successfully.'}</div>`;
                
            } catch (err) {
                detailsDisplay.innerHTML = `<div style=\"color: #ef4444;\">Error: ${err.message}</div>`;
            }
        }'''

# Apply the fixes
content = content.replace(old_load_agent_sessions, new_load_agent_sessions)
content = content.replace(old_parse_sessions, new_parse_sessions)
content = content.replace(old_load_selected_session, new_load_selected_session)

# Write the fixed content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ guiClaw index.html has been fixed!")
print("✅ Fixed loadAgentSessions function")
print("✅ Fixed parseSessions function")
print("✅ Fixed loadSelectedSession function")
print("\nChanges made:")
print("1. Replaced --kinds with --store parameter for listing sessions")
print("2. Replaced /v1/responses with /api/execute endpoint")
print("3. Replaced openclaw sessions send with openclaw agent --session-id")
print("4. Added JSON parsing for session list output")
print("5. Added agent path mapping for different agent types")
print("\nBackup saved as: index.html.backup")