const burgerOpen = document.getElementById('burger-open');
const burgerClose = document.getElementById('burger-close');
const mobileSidebar = document.getElementById('mobile-sidebar');

const loginBtn = document.getElementById('login-btn');
const userProfile = document.getElementById('user-profile');
const userAvatar = document.getElementById('user-avatar');
const userName = document.getElementById('user-name');

if (burgerOpen && mobileSidebar) {
    burgerOpen.addEventListener('click', () => {
        mobileSidebar.classList.add('active');
    });
}

if (burgerClose && mobileSidebar) {
    burgerClose.addEventListener('click', () => {
        mobileSidebar.classList.remove('active');
    });
}

document.querySelectorAll('.mobile-nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        mobileSidebar.classList.remove('active');
    });
});

if (loginBtn) {
    loginBtn.addEventListener('click', () => {
        window.location.href = 'http://localhost:5000/auth/login';
    });
}

window.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const authStatus = urlParams.get('auth');
    const name = urlParams.get('name');
    const avatar = urlParams.get('avatar');

    if (authStatus === 'success' && name && avatar) {
        if (userProfile && userAvatar && userName) {
            userAvatar.src = decodeURIComponent(avatar);
            userName.textContent = decodeURIComponent(name);
            
            userProfile.classList.remove('hidden');
            if (loginBtn) loginBtn.style.display = 'none';
        }
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});

const cryptoIds = ['btcusdt', 'ethusdt', 'solusdt', 'xrpusdt', 'usdcusdt', 'bnbusdt'];
const streams = cryptoIds.map(id => `${id}@ticker`).join('/');
const socketUrl = `wss://stream.binance.com:9443/ws/${streams}`;

const cryptoSocket = new WebSocket(socketUrl);

cryptoSocket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const tickerSymbol = data.s.toLowerCase();
    const currentPrice = parseFloat(data.c);

    const priceElement = document.getElementById(tickerSymbol);
    
    if (priceElement) {
        if (currentPrice > 100) {
            priceElement.textContent = `$${currentPrice.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        } else if (currentPrice > 1) {
            priceElement.textContent = `$${currentPrice.toLocaleString('en-US', { minimumFractionDigits: 3, maximumFractionDigits: 3 })}`;
        } else {
            priceElement.textContent = `$${currentPrice.toFixed(5)}`;
        }
    }
};