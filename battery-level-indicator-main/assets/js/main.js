document.addEventListener("DOMContentLoaded", function() {
    const batteryGrid = document.querySelector('.battery-grid');

    for (let i = 0; i < 90; i++) {
        const batteryCard = document.createElement('div');
        batteryCard.classList.add('battery__card');
        batteryCard.innerHTML = `
            <div class="battery__data">
                <h1 class="battery__percentage">0%</h1>
            </div>
            <div class="battery__pill">
                <div class="battery__level">
                    <div class="battery__liquid"></div>
                </div>
            </div>
        `;
        batteryGrid.appendChild(batteryCard);
    }

    initBattery();
});

function initBattery(){
    const batteryCards = document.querySelectorAll('.battery__card');

    batteryCards.forEach((card) => {
        const batteryLiquid = card.querySelector('.battery__liquid'),
              batteryPercentage = card.querySelector('.battery__percentage');

        navigator.getBattery().then((batt) =>{
            updateBattery = () =>{
                /* 1. We update the number level of the battery */
                let level = Math.floor(batt.level * 100);
                batteryPercentage.innerHTML = level + '%';

                /* 2. We update the background level of the battery */
                batteryLiquid.style.height = `${parseInt(batt.level * 100)}%`;

                /* 3. We change the colors of the battery and remove the other colors */
                if(level <= 20){
                    batteryLiquid.classList.add('gradient-color-red');
                    batteryLiquid.classList.remove('gradient-color-orange','gradient-color-yellow','gradient-color-green');
                }
                else if(level <= 40){
                    batteryLiquid.classList.add('gradient-color-orange');
                    batteryLiquid.classList.remove('gradient-color-red','gradient-color-yellow','gradient-color-green');
                }
                else if(level <= 80){
                    batteryLiquid.classList.add('gradient-color-yellow');
                    batteryLiquid.classList.remove('gradient-color-red','gradient-color-orange','gradient-color-green');
                }
                else{
                    batteryLiquid.classList.add('gradient-color-green');
                    batteryLiquid.classList.remove('gradient-color-red','gradient-color-orange','gradient-color-yellow');
                }
            }
            updateBattery();

            /* 4. Battery status events */
            batt.addEventListener('chargingchange', () => { updateBattery() });
            batt.addEventListener('levelchange', () => { updateBattery() });
        });
    });
}
