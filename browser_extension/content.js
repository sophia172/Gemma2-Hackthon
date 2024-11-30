(() => {
    if (window.hasRun) {
        return; // Prevent the script from running multiple times
    }
    window.hasRun = true;

    const pageTextContent = document.body.innerText;
    const images = Array.from(document.images).map(img => img.src);
    const pageUrl = window.location.href;

    const extractedData = {
        url: pageUrl
    };
    console.log("message received: ",extractedData)
    fetch('http://localhost:8000/api/data', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
       body: JSON.stringify(extractedData)
    })
    .then(response => response.json())
    .then(data => console.log("API response:", data))
    .catch(error => console.error("API error:", error));
    chrome.runtime.sendMessage({ action: "sendToAPI", data: extractedData });
})();
