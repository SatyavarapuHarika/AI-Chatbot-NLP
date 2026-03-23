function addMessage(text, type) {
    let chatBox = document.getElementById("chat-box");

    let msg = document.createElement("div");
    msg.classList.add("message", type);
    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if (!message) return;

    addMessage(message, "user");

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    let data = await response.json();

    addMessage(data.response, "bot");

    input.value = "";
}


function handleEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}