from flask import Flask, render_template_string

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
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #fce7f3, #f3e8ff, #dbeafe);
            padding: 24px;
            position: relative;
            overflow: hidden;
        }

        .hearts-background {
            position: absolute;
            inset: 0;
            pointer-events: none;
        }

        .floating-heart {
            position: absolute;
            color: #f9a8d4;
            font-size: 24px;
            animation: pulse 3s infinite;
        }

        .initial-screen {
            text-align: center;
        }

        .open-button {
            position: relative;
            padding: 16px 32px;
            border-radius: 12px;
            background: linear-gradient(135deg, #ec4899, #8b5cf6);
            color: white;
            font-weight: 600;
            font-size: 18px;
            border: none;
            cursor: pointer;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .open-button:hover {
            transform: scale(1.05);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }

        .open-button:hover .gift-icon {
            animation: bounce 0.6s ease-in-out infinite;
        }

        .subtitle {
            margin-top: 16px;
            color: #6b7280;
            font-size: 14px;
        }

        .popup-container {
            position: relative;
            background: white;
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            padding: 40px;
            text-align: center;
            max-width: 400px;
            margin: 0 auto;
            animation: slideUp 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            display: none;
        }

        .popup-container.show {
            display: block;
        }

        .teddy-container {
            position: relative;
        }

        .teddy-bear {
            width: 192px;
            height: 192px;
            margin: 0 auto;
            background: linear-gradient(135deg, #60a5fa, #2563eb);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 72px;
            animation: bounce 2s infinite;
            animation-delay: 0.3s;
        }

        .hearts-around-teddy {
            position: absolute;
            inset: 0;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.5s ease;
        }

        .hearts-around-teddy.show {
            opacity: 1;
        }

        .heart-particle {
            position: absolute;
            color: #f87171;
            animation: ping 2s infinite;
        }

        .message-section {
            margin-top: 24px;
        }

        .main-message {
            font-size: 32px;
            font-weight: bold;
            background: linear-gradient(135deg, #db2777, #8b5cf6);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }

        .sub-message {
            color: #6b7280;
            font-size: 18px;
            margin-bottom: 12px;
        }

        .stars {
            display: flex;
            justify-content: center;
            gap: 8px;
            font-size: 24px;
            margin-bottom: 20px;
        }

        .star {
            animation: pulse 1.5s infinite;
        }

        .button-group {
            margin-top: 32px;
            display: flex;
            gap: 12px;
            justify-content: center;
        }

        .close-button, .hearts-button {
            padding: 8px 24px;
            border-radius: 8px;
            border: none;
            font-weight: 500;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .close-button {
            background: #f3f4f6;
            color: #374151;
        }

        .close-button:hover {
            background: #e5e7eb;
        }

        /* Animations */
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(100px) scale(0.8);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        @keyframes bounce {
            0%, 20%, 53%, 80%, 100% {
                transform: translateY(0);
            }
            40%, 43% {
                transform: translateY(-10px);
            }
            70% {
                transform: translateY(-5px);
            }
            90% {
                transform: translateY(-2px);
            }
        }


        @keyframes ping {
            0% {
                transform: scale(1);
                opacity: 1;
            }
            75%, 100% {
                transform: scale(1.5);
                opacity: 0;
            }
        }
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
            <image src="{{ url_for('static', filename='teddy.png') }}" alt="Teddy Banner" style="max-width: 70%; height: auto; margin-bottom: 20px;" />

            <!-- Floating hearts around teddy -->
            <div class="hearts-around-teddy" id="heartsAroundTeddy">
                <div class="heart-particle" style="left: 10%; top: 20%; font-size: 16px; animation-delay: 0s;">❤️</div>
                <div class="heart-particle" style="left: 80%; top: 30%; font-size: 12px; animation-delay: 0.2s;">❤️</div>
                <div class="heart-particle" style="left: 15%; top: 70%; font-size: 18px; animation-delay: 0.4s;">❤️</div>
                <div class="heart-particle" style="left: 85%; top: 60%; font-size: 14px; animation-delay: 0.6s;">❤️</div>
                <div class="heart-particle" style="left: 50%; top: 10%; font-size: 16px; animation-delay: 0.8s;">❤️</div>
                <div class="heart-particle" style="left: 30%; top: 90%; font-size: 13px; animation-delay: 1s;">❤️</div>
                <div class="heart-particle" style="left: 70%; top: 85%; font-size: 17px; animation-delay: 1.2s;">❤️</div>
                <div class="heart-particle" style="left: 90%; top: 15%; font-size: 15px; animation-delay: 1.4s;">❤️</div>
                <div class="heart-particle" style="left: 20%; top: 15%; font-size: 11px; animation-delay: 1.6s;">❤️</div>
                
                <!-- Additional hearts -->
                <div class="heart-particle" style="left: 40%; top: 40%; font-size: 14px; animation-delay: 0.3s;">❤️</div>
                <div class="heart-particle" style="left: 60%; top: 50%; font-size: 18px; animation-delay: 0.5s;">❤️</div>
                <div class="heart-particle" style="left: 25%; top: 35%; font-size: 13px; animation-delay: 0.7s;">❤️</div>
                <div class="heart-particle" style="left: 75%; top: 75%; font-size: 16px; animation-delay: 0.9s;">❤️</div>
                <div class="heart-particle" style="left: 45%; top: 80%; font-size: 12px; animation-delay: 1.1s;">❤️</div>
                <div class="heart-particle" style="left: 55%; top: 25%; font-size: 15px; animation-delay: 1.3s;">❤️</div>
                <div class="heart-particle" style="left: 35%; top: 60%; font-size: 17px; animation-delay: 1.5s;">❤️</div>
                <div class="heart-particle" style="left: 65%; top: 20%; font-size: 14px; animation-delay: 1.7s;">❤️</div>
            </div>
        </div>

        <!-- Message -->
        <div class="message-section">
            <p class="sub-message">Nakita ko lang sa fyp while scrolling, then ginaya ko.</p>
        </div>

        <!-- Action buttons -->
        <div class="button-group">
            <button class="close-button" onclick="closePopup()">Close mo dito</button>
        </div>
    </div>

    <script>
        let heartsVisible = false;

        function openPopup() {
            document.getElementById('initialScreen').style.display = 'none';
            document.getElementById('popupContainer').classList.add('show');

            // Show hearts after delay
            setTimeout(() => {
                document.getElementById('heartsAroundTeddy').classList.add('show');
                heartsVisible = true;
            }, 800);
        }

        function closePopup() {
            document.getElementById('popupContainer').classList.remove('show');
            document.getElementById('initialScreen').style.display = 'block';
            document.getElementById('heartsAroundTeddy').classList.remove('show');
            heartsVisible = false;
        }

        function toggleHearts() {
            const heartsElement = document.getElementById('heartsAroundTeddy');
            if (heartsVisible) {
                heartsElement.classList.remove('show');
                heartsVisible = false;
            } else {
                heartsElement.classList.add('show');
                heartsVisible = true;
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

if __name__ == '__main__':
    print("🧸 Starting Teddy Popup Server...")
    print("💕 Open your browser and go to: http://localhost:5000")
    print("🎁 Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)