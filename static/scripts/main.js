var submit_btn = document.getElementById("submit_btn");
var loader = document.getElementById("loader");
var fader = document.getElementById("fader");
var init = document.getElementById("init");
var msg = document.getElementById("message");

submit_btn.addEventListener("click", function (event) {
    submit_btn.disabled = true;
    loader.style.display = "block";
    fader.style.opacity = 0;
    init.style.display = "none";


    // Ajax call to fetch the data from the server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
        if (xhr.status === 200) {
            setTimeout(function () {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    commonName = response.result.commonName;
                    description = response.result.description;
                    imgName1 = response.result.imgName1;
                    imgName2 = response.result.imgName2;
                    audioName = response.result.audioName;
                    wikiLink = response.result.wikiLink;
                    confidence = response.result.confidence;

                    update_display(commonName, description, imgName1, imgName2, audioName, wikiLink, confidence);
                    submit_btn.disabled = false;
                    loader.style.display = "none";
                    fader.style.opacity = 1;
                }
            }, 700);
        } else {
            alert('An Internal error occurred.');
            submit_btn.disabled = false;
            loader.style.display = "none";
            fader.style.opacity = 1;
        }
    };

    xhr.send(JSON.stringify({
        description: document.getElementById("description").value.trim()
    }));
});

// onload event
window.onload = function () {
    description = document.getElementById("description").value.trim();
    document.getElementById("description").focus();
    if (description === "" || description === null) {
        submit_btn.disabled = true;
    }
};

// oninput event
document.getElementById("description").oninput = function () {
    description = document.getElementById("description").value.trim();
    if (description.split(' ') == "") {
        msg.style.opacity = 0;
    } else if (description === "" || description === null || description.split(' ').length < 3) {
        submit_btn.disabled = true;

        msg.style.opacity = 1;
        msg.innerHTML = "Please enter " + (3 - description.split(' ').length) + " more words.";
    } else {
        submit_btn.disabled = false;
        msg.style.opacity = 0;
    }
};

function update_display(name, description, imgName1, imgName2, audioName, wikiLink, confidence) {
    document.getElementById("bird-name").innerHTML = name;
    document.getElementById("bird-description").innerHTML = description;
    document.getElementById("bird-img1").src = "/static/images/" + imgName1;
    document.getElementById("bird-img2").src = "/static/images/" + imgName2;
    document.getElementById("bird-wiki-link").href = wikiLink;
    document.getElementById("confidence").innerHTML = confidence + "% Confidence";

    audio = document.getElementById("bird-audio");
    audio.src = "/static/audios/" + audioName;
    audio.load();
}