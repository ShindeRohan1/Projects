

let video = document.querySelector("video");//collection of frames
let recorder;
let recordbtncont = document.querySelector(".record-btn-cont")
let capturebtncont = document.querySelector(".capture-btn-cont")
let recordbtn = document.querySelector(".record-btn")
let capturebtn = document.querySelector(".capture-btn")
let recordflag = false;


let chunks = [] //media data in chunks

let constraints = {
    audio: true,
    video: true
}
//navigator to get information of browser
navigator.mediaDevices.getUserMedia(constraints)// 1 .mediadevices is a browser api to  connect input devices like camera and microphone , getusermedia to get permision
    .then((stream) => {
        video.srcObject = stream

        recorder = new MediaRecorder(stream);//3. mediaRecorder() function of mediaStreamRecorder api to record a media
        recorder.addEventListener("start", (e) => {
            chunks = [];
        })
        recorder.addEventListener("dataavailable", (e) => {
            chunks.push(e.data)
        })
        recorder.addEventListener("stop", (e) => {
            // coversion of chunks to video formate
            let blob = new Blob(chunks, { type: "video/mp4" });

            let videoUrl = URL.createObjectURL(blob);

            let a = document.createElement("a");
            a.href = videoUrl;
            a.download = "stream.mp4";
            a.click();
        })

    })
recordbtncont.addEventListener("click", (e) => {
    if (!recorder) return
    recordflag = !recordflag;

    if (recordflag) {
        recorder.start();
        recordbtn.classList.add("scale-record");
        startTimer();
    } else {
        recorder.stop();
        recordbtn.classList.remove("scale-record");
        stopTimer();
    }
})

let timerId;
let counter = 0;
let timer = document.querySelector(".timer");
function startTimer() {
    timer.style.display = "block"
    function displaytimer() {
        let totalseconds = counter
        let hours = Number.parseInt(totalseconds / 3600);
        totalseconds = totalseconds % 3600;
        let minutes = Number.parseInt(totalseconds / 60);
        totalseconds = totalseconds % 60;

        second = totalseconds;
        hours = (hours < 10) ? `0${hours}` : hours;
        minutes = (minutes < 10) ? `0${minutes}` : minutes;
        second = (second < 10) ? `0${second}` : second;


        timer.innerText = `${hours}:${minutes}:${second}`

        counter++;

    }
    timerId = setInterval(displaytimer, 1000)
}
function stopTimer() {
    clearInterval(timerId);
    timer.innerText = "00:00:00";
    timer.style.display = "none"
}


// 1 .mediadevices is a browser api to  connect input devices like camera and microphone , getusermedia to get permision
//2 .mediastream api to stream the camera contenoulsy
//3. mediaRecorder() function of mediaStreamRecorder api to record a media

//camera   image is captured from video elements
//4.canvas is browser api and html element for graphics performance
capturebtn.addEventListener("click", (e) => {
    let canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    let tool = canvas.getContext("2d");
    tool.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
    let imageURL = canvas.toDataURL();


    let a = document.createElement("a");
    a.href = imageURL;
    a.download = "image.jpg";
    a.click();

})