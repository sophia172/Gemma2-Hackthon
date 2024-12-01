const playPauseButton = document.getElementById("playPause");
const playPauseIcon = document.getElementById("playPauseIcon");
const extractButton = document.getElementById("extract");

playPauseButton.hidden = true;

extractButton.addEventListener("click", () => {    
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            files: ["content.js"]
        });
    });
    extractButton.hidden = true;    
    playPauseButton.hidden = false;
    playPauseButton.disabled = true
    playPauseButton.style.backgroundColor = "#d3d3d3";

});

playPauseButton.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "toggleAudio" });
        toggleIcon();
    });
});

chrome.runtime.onMessage.addListener((message) => {
    if (message.action === "audioStarted") {
        console.log("Audio has started playing.");
        playPauseButton.disabled = false;
        playPauseButton.style.backgroundColor = "#28a745";
    }
    else if (message.action === "audioCompleted") {
        console.log("Audio playback completed.");
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
