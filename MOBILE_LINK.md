# Mobile Link Feature Documentation

## Overview

The Mobile Link feature allows you to access your OpenClaw instance from mobile devices using QR codes and dynamic DNS. This is particularly useful for accessing your personal assistant from your phone or tablet.

## Features

- **IP Detection**: Built-in tool to get your current public IP address
- **No-IP Integration**: Automated setup for dynamic DNS
- **Port Forwarding Guide**: Step-by-step router configuration
- **QR Code Support**: QR codes for easy mobile access
- **Local Network Access**: Quick access from devices on the same network
- **Remote Access**: Access from anywhere via dynamic DNS

## Connection Options

### 1. Local Network Access
For devices on the same network:
```
http://[YOUR-IP]:8000
```

### 2. Internet Access (Dynamic DNS)
For access from anywhere via No-IP:
```
http://your-hostname.ddns.net:8000
```

## Setup Steps

### Step 1: Get Your Connection URL

First, determine your connection URL for mobile access:

#### 1.1 Local Network Access
For devices on the same network:
```
http://[YOUR-IP]:8000
```

#### 1.2 Internet Access (Dynamic DNS)
For access from anywhere via No-IP:
```
http://your-hostname.ddns.net:8000
```

#### 1.3 Get Your Current IP
Run this to get your public IP address:
```
curl ifconfig.me
```

### Step 2: No-IP Dynamic DNS Setup

Set up No-IP dynamic DNS for remote access:

#### 2.1 Install No-IP Client
Install No-IP client for dynamic DNS updates:
```
brew install noip
```

#### 2.2 Configure No-IP Client
Run the configuration wizard to set up your No-IP account:
```
sudo noip2 -C
```

#### 2.3 Start No-IP Service
Start the No-IP service to keep your DNS updated:
```
sudo noip2 -S
```

### Step 3: Router Port Forwarding

Configure your router to forward port 8000 to your computer:

#### 3.1 Port Forwarding Rules
Add these rules to your router:
- **External Port:** 8000
- **Internal Port:** 8000
- **Protocol:** TCP
- **Internal IP:** Your computer's local IP (e.g., 192.168.1.100)
- **Description:** OpenClaw GUI

#### 3.2 How to Access Router Settings
1. Open your browser and go to your router's IP address (usually 192.168.1.1 or 192.168.0.1)
2. Log in with your router credentials
3. Look for "Port Forwarding" or "Virtual Server" settings
4. Add the port forwarding rule as described above
5. Save the settings and restart your router if needed

### Step 4: Mobile Access

#### 4.1 Access from Mobile Device
1. Open your mobile browser
2. Enter your connection URL:
   - Local: `http://[YOUR-IP]:8000`
   - Remote: `http://your-hostname.ddns.net:8000`
3. Bookmark the page for quick access

#### 4.2 QR Code Generation
You can generate a QR code for easy mobile access:
1. Use a QR code generator tool or website
2. Enter your connection URL
3. Scan the QR code with your mobile device's camera
4. The browser will open the guiClaw interface

## Troubleshooting

### Common Issues

#### 1. Cannot Access from Mobile
- **Check IP Address**: Make sure you're using the correct IP address
- **Network Connection**: Ensure your mobile device is connected to the same network (for local access)
- **Firewall**: Check if your firewall is blocking port 8000
- **Router Settings**: Verify port forwarding is correctly configured

#### 2. No-IP Not Working
- **Client Running**: Make sure the No-IP client is running
- **Hostname Configuration**: Verify your hostname is correctly configured
- **DNS Propagation**: Wait a few minutes for DNS changes to propagate

#### 3. Port Forwarding Issues
- **Router Access**: Make sure you can access your router's settings
- **Internal IP**: Verify your computer's internal IP is correct (use `ifconfig` or `ipconfig`)
- **Port Conflict**: Check if another application is using port 8000

### Testing Your Setup

1. **Local Network Test**:
   - From another device on the same network, try accessing `http://[YOUR-IP]:8000`
   - Replace `[YOUR-IP]` with your computer's local IP address

2. **Remote Access Test**:
   - Turn off Wi-Fi on your mobile device and use cellular data
   - Try accessing `http://your-hostname.ddns.net:8000`
   - If it works, your setup is correct

3. **Port Forwarding Test**:
   - Use an online port checker tool
   - Enter your public IP and port 8000
   - Check if the port is open

## Security Considerations

1. **Use HTTPS**: For production use, consider setting up HTTPS with SSL certificates
2. **Strong Authentication**: Ensure your OpenClaw gateway token is kept secure
3. **Firewall Rules**: Configure your firewall to only allow necessary traffic
4. **Regular Updates**: Keep your system and software updated for security patches

## Advanced Configuration

### Custom Port Configuration
If you want to use a different port (e.g., 8080):
1. Update the port in `proxy.js` (line with `const PORT = 8000`)
2. Update port forwarding rules in your router
3. Update connection URLs accordingly

### Multiple Devices
For accessing from multiple devices:
1. Set up port forwarding for each device's IP address
2. Use dynamic DNS for each device
3. Consider using a reverse proxy for multiple services

## Integration with Other Features

### WhatsApp Integration
The Mobile Link feature works seamlessly with WhatsApp integration:
1. Access guiClaw from your mobile device
2. Navigate to the Channel section
3. Configure WhatsApp settings
4. Use WhatsApp from your mobile device

### Multi-Agent Support
Access multi-agent features from mobile:
1. Navigate to the Multi-Agent section
2. Manage agent sessions
3. Use inter-agent chat from mobile

### File Upload
Upload files from mobile devices:
1. Access the file upload feature
2. Select files from your mobile device
3. Upload directly through the web interface

## Performance Tips

1. **Network Speed**: For best performance, use a stable internet connection
2. **Browser Choice**: Use a modern mobile browser (Chrome, Safari, Firefox)
3. **Cache Management**: Clear browser cache if experiencing slow performance
4. **Background Apps**: Close unnecessary apps to free up mobile resources

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the main README.md file
3. Check the OpenClaw documentation
4. Contact the development team

## Version Information

- **Feature Added**: v1.5
- **Date**: 2026-02-22
- **Author**: Riceball Mimo (formerly riceball)
- **Status**: Production Ready

## Related Documentation

- [README.md](README.md) - Main project documentation
- [VERSION.md](VERSION.md) - Version history and changelog
- [INSTALLATION.md](INSTALLATION.md) - Installation instructions
- [CHANGELOG.md](CHANGELOG.md) - Detailed changelog