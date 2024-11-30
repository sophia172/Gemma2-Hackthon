(() => {
    // if (window.hasRun) {
    //     return; // Prevent the script from running multiple times
    // }
    // window.hasRun = true;

    let audio = null; // Global variable to store the Audio object

    const playAudio = (audioBlob) => {      
        const audioUrl = URL.createObjectURL(audioBlob);
        if (audio) {
            audio.pause(); 
            audio.currentTime = 0;
        }
        audio = new Audio(audioUrl);
        isAudioPlaying = true;
        audio.addEventListener("ended", () => {
            console.log("Audio playback completed.");
            isAudioPlaying = false; 
            chrome.runtime.sendMessage({ action: "audioCompleted" });
        });
        audio.play();
    };

    const toggleAudioPlayback = () => {
        if (audio) {
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
        } else {
            console.log("No audio loaded yet.");
        }
    };

    const pageUrl = window.location.href;

    const extractedData = {
        url: pageUrl
    };

    fetch('http://localhost:8000/api/data', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(extractedData)
    })
    .then(async (response) => {
        if (!response.ok) {
            throw new Error(`API error: ${response.statusText}`);
        }
        const audioBlob = await response.blob();
        playAudio(audioBlob); 
    })
    .catch(error => console.error("API error:", error));

    chrome.runtime.onMessage.addListener((message) => {
        if (message.action === "toggleAudio") {
            toggleAudioPlayback();
        }
    });
})();
