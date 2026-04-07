


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


function calculateAge() {
    const dobValue = document.getElementById('DOBinput').value;
    const currentValue = document.getElementById('DATEinput').value;

    if (!dobValue) {
        document.getElementById('result').innerText = "Please enter your Date of Birth";
        return;
    }

    const dob = new Date(dobValue);
    const current = currentValue ? new Date(currentValue) : new Date(); // fallsback to today through new data

    const diffInMs = current - dob;
    const diffInDays = diffInMs / (1000 * 60 * 60 * 24);

    const years = Math.floor(diffInDays / 365.25);
    const months = Math.floor((diffInDays % 365.25) / 30);
    const days = Math.floor((diffInDays % 365.25) % 30);

    document.getElementById('result').innerText = 
        `Age: ${years} year(s), ${months} month(s), ${days} day(s)`;
}