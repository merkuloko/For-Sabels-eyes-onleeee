from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# HTML template with embedded CSS and JavaScript
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I Miss You - Teddy Popup</title>
    <style>
        /* your existing CSS stays here */
    </style>
</head>
<body>
    <!-- Initial screen -->
    <div class="initial-screen" id="initialScreen">
        <button class="open-button" onclick="openPopup()">
            Click this
            <span class="gift-icon">🎁</span>
        </button>
        <p class="subtitle">Got a message for you...</p>
    </div>

    <!-- Popup container -->
    <div class="popup-container" id="popupContainer">
        <!-- Teddy Bear -->
        <div class="teddy-container">
            <!-- Updated image path -->
            <img src="/Teddy.png" alt="Survey Banner" style="max-width: 70%; height: auto; margin-bottom: 20px;" />

            <!-- Floating hearts around teddy -->
            <div class="hearts-around-teddy" id="heartsAroundTeddy">
                <!-- your existing hearts here -->
            </div>
        </div>

        <!-- Message -->
        <div class="message-section">
            <p class="sub-message">Nakita ko lang sa fyp while scrolling, then ginaya ko.</p>
            <div class="stars">
                <span class="star">🌟</span>
                <span class="star" style="animation-delay: 0.2s;">✨</span>
                <span class="star" style="animation-delay: 0.4s;">💫</span>
            </div>
        </div>

        <!-- Action buttons -->
        <div class="button-group">
            <button class="close-button" onclick="closePopup()">Close mo dito</button>
        </div>
    </div>

    <script>
        // your existing JS stays here
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

# New route to serve teddy.png from the same folder
@app.route('/teddy.png')
def serve_teddy():
    return send_from_directory(os.path.dirname(__file__), 'teddy.png')

if __name__ == '__main__':
    print("🧸 Starting Teddy Popup Server...")
    print("💕 Open your browser and go to: http://localhost:5000")
    print("🎁 Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
