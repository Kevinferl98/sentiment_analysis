function send() {
    var input = document.getElementById("input").value;
    var backendHost = 'http://localhost:5000';

    if(!checkText(input)) {
        return;
    }

    fetch(backendHost + '/sentiment_analysis', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: input }) 
    })
    .then(response => response.json())
    .then(data => {
        var response = document.getElementById("result");
        response.innerHTML = "";
        response.innerHTML += "<p><strong>Polarity:</strong> " + data.polarity + "</p>";
        response.innerHTML += "<p><strong>Subjectivity:</strong> " + data.subjectivity + "</p>";
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function checkText(input) {
    if (input === null || input.length === 0) {
        alert('Please, insert some text');
        return false;
    }
    return true;
}