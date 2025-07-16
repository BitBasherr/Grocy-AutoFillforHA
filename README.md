# Grocy-AutoFillforHA

Automatically fills in missing Grocy product names using Open Food Facts.  
Packaged as a native Home Assistant add-on.

## 📦 Features

✅ Monitors Grocy for products with no name but a barcode  
✅ Queries Open Food Facts for the barcode  
✅ Updates the product name in Grocy  
✅ Runs as a native Home Assistant add-on  
✅ Configurable poll interval

## 🔧 Installation

1. In Home Assistant:  
   **Settings → Add-ons → Add-on Store → … → Repositories**

2. Add this URL:
    https://github.com/BitBasherr/Grocy-AutoFillforHA


3. Look for **Grocy AutoFill for HA** in the Add-on Store and install.

4. Configure your Grocy URL and API key in the add-on options.

5. Start the add-on and enjoy!

## ⚙️ Configuration

Options:
- `grocy_url`: URL to your Grocy instance (e.g., `http://homeassistant.local:9192`)
- `api_key`: API key from Grocy (create one in Grocy’s web UI)
- `poll_interval`: Poll interval in seconds (default: 30)

Example:
```json
{
  "grocy_url": "http://homeassistant.local:9192",
  "api_key": "your_api_key",
  "poll_interval": 30
}
```
