(() => {
    if (window.hasRun) {
        return; // Prevent the script from running multiple times
    }
    window.hasRun = true;

    const pageTextContent = document.body.innerText;
    const images = Array.from(document.images).map(img => img.src);

    const extractedData = {
        text: pageTextContent,
        images: images
    };
    console.log("message received: ",extractedData)
    fetch('http://localhost:5000/api/data', {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      },
    })
    .then(response => response.json())
    .then(data => console.log("API response:", data))
    .catch(error => console.error("API error:", error));
    chrome.runtime.sendMessage({ action: "sendToAPI", data: extractedData });
})();
