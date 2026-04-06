


function updateTime() {
    const timeElement = document.getElementById("current-time");
    const now = new Date();

    timeElement.textContent = now.toLocaleTimeString(); 
}

updateTime();
setInterval(updateTime, 1.420000000);


function updateClock() {
    const now = new Date();

    const seconds = now.getSeconds();
    const minutes = now.getMinutes();
    const hours = now.getHours();

    
    const secondsDeg = seconds * 6;                    
    const minutesDeg = minutes * 6 + seconds * 0.1;    
    const hoursDeg = (hours % 12) * 30 + minutes * 0.5;

    
    document.querySelector(".secondHand").style.transform =
        `translateX(-50%) rotate(${secondsDeg}deg)`;

    document.querySelector(".minuteHand").style.transform =
        `translateX(-50%) rotate(${minutesDeg}deg)`;

    document.querySelector(".hourHand").style.transform =
        `translateX(-50%) rotate(${hoursDeg}deg)`;
}

updateClock();
setInterval(updateClock, 1000);