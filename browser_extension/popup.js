const playPauseButton = document.getElementById("playPause");
const playPauseIcon = document.getElementById("playPauseIcon");
const extractButton = document.getElementById("extract");

extractButton.addEventListener("click", () => {    
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            files: ["content.js"]
        });
    });
    extractButton.disabled = true;
});

playPauseButton.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "toggleAudio" });
        toggleIcon();
    });
});

chrome.runtime.onMessage.addListener((message) => {
    if (message.action === "audioCompleted") {
        console.log("Audio playback completed.");
        extractButton.disabled = false;
    }
});

function toggleIcon() {
    if (playPauseIcon.classList.contains("fa-play")) {
        playPauseIcon.classList.remove("fa-play");
        playPauseIcon.classList.add("fa-pause");
        playPauseButton.innerHTML = `<i id="playPauseIcon" class="fas fa-pause icon"></i> Pause`;
    } else {
        playPauseIcon.classList.remove("fa-pause");
        playPauseIcon.classList.add("fa-play");
        playPauseButton.innerHTML = `<i id="playPauseIcon" class="fas fa-play icon"></i> Play`;
    }
}
