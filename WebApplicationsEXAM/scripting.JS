


function updateTime() {
    const timeElement = document.getElementById("current-time");
    const now = new Date();

    timeElement.textContent = now.toLocaleTimeString(); 
}

updateTime();
setInterval(updateTime, 1.420000000);
