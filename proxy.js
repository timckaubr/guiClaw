const http = require('http');
const fs = require('fs');
const path = require('path');
const busboy = require('busboy');

const PORT = 8000;
const UPLOAD_DIR = path.join(__dirname, 'upload');
const INDEX_HTML = path.join(__dirname, 'index.html');

if (!fs.existsSync(UPLOAD_DIR)) {
    fs.mkdirSync(UPLOAD_DIR, { recursive: true });
}

const server = http.createServer((req, res) => {
    // Enable CORS
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, GET, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, x-openclaw-agent-id');

    if (req.method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }

    // Serve HTML
    if (req.method === 'GET' && (req.url === '/' || req.url === '/index.html')) {
        fs.readFile(INDEX_HTML, (err, data) => {
            if (err) {
                res.writeHead(500);
                res.end('Error loading index.html');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
        return;
    }

    // Serve Config
    if (req.method === 'GET' && req.url === '/config') {
        const configPath = path.join(process.env.HOME, '.openclaw', 'openclaw.json');
        fs.readFile(configPath, 'utf8', (err, data) => {
            if (err) {
                console.error('Error reading config:', err);
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Could not read config file' }));
                return;
            }
            try {
                const config = JSON.parse(data);
                const primary = config.agents?.defaults?.model?.primary || 'Unknown';
                const models = config.agents?.defaults?.models || {};
                
                // Format configured models nicely
                const configured = Object.entries(models).map(([id, details]) => {
                    return details.alias ? `${details.alias} (${id})` : id;
                });

                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({
                    currentModel: primary,
                    configuredModels: configured
                }));
            } catch (parseErr) {
                console.error('Error parsing config:', parseErr);
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Invalid config file' }));
            }
        });
        return;
    }

    // Handle File Upload
    if (req.method === 'POST' && req.url === '/upload') {
        try {
            const bb = busboy({ headers: req.headers });
            let savedFile = '';

            bb.on('file', (name, file, info) => {
                const { filename } = info;
                const savePath = path.join(UPLOAD_DIR, filename);
                savedFile = savePath;
                console.log(`Saving file to: ${savePath}`);
                file.pipe(fs.createWriteStream(savePath));
            });

            bb.on('close', () => {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: true, path: savedFile }));
            });

            req.pipe(bb);
        } catch (err) {
            console.error('Upload error:', err);
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: err.message }));
        }
        return;
    }

    // Proxy API
    if (req.url.startsWith('/v1/') || req.url.startsWith('/api/')) {
        console.log(`Proxying request: ${req.method} ${req.url}`);
        
        // Strip /v1 prefix if necessary for the internal gateway
        const proxyPath = req.url;

        const options = {
            hostname: '127.0.0.1',
            port: 18789,
            path: proxyPath,
            method: req.method,
            headers: {
                'Content-Type': req.headers['content-type'],
                'Authorization': req.headers['authorization'] || 'Bearer 13df78878223e1c280296d6ec83f2ba92636c36b1c65bb92',
                'x-openclaw-agent-id': req.headers['x-openclaw-agent-id'] || 'main',
                'host': '127.0.0.1:18789'
            }
        };

        const proxyReq = http.request(options, (proxyRes) => {
            console.log(`Gateway response: ${proxyRes.statusCode}`);
            res.writeHead(proxyRes.statusCode, proxyRes.headers);
            proxyRes.pipe(res);
        });

        proxyReq.on('error', (err) => {
            console.error('Proxy request error:', err);
            res.writeHead(502);
            res.end(JSON.stringify({ error: 'Proxy Error: ' + err.message }));
        });

        if (req.method === 'POST') {
            req.pipe(proxyReq);
        } else {
            proxyReq.end();
        }
        return;
    }

    res.writeHead(404);
    res.end('Not Found');
});

console.log(`Server running at http://127.0.0.1:${PORT}/`);
server.listen(PORT);
