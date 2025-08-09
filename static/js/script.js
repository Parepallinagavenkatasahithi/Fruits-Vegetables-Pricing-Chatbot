document.getElementById("send-btn").addEventListener("click", function() {
    let input = document.getElementById("user-input").value;
    let category = document.querySelector('input[name="category"]:checked').value;
    if (input.trim() === "") return;

    let chatBox = document.getElementById("chat-box");

    let userMsg = document.createElement("div");
    userMsg.className = "user-message";
    userMsg.innerText = input;
    chatBox.appendChild(userMsg);

    fetch("/get_price", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({item: input, category: category})
    })
    .then(res => res.json())
    .then(data => {
        let botMsg = document.createElement("div");
        botMsg.className = "bot-message";
        botMsg.innerText = `The price of ${data.item} is ${data.price}`;
        chatBox.appendChild(botMsg);
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById("user-input").value = "";
});
