function updateBatteryStatus(batt) {
    const level = Math.floor(batt.level * 100);
    const isCharging = batt.charging;

    // Update battery percentage display
    batteryPercentage.innerHTML = `${level}%`;

    // Update battery liquid height
    batteryLiquid.style.height = `${level}%`;

    // Determine battery status and icon
    if (level === 100) {
        batteryStatus.innerHTML = `Full battery <i class="ri-battery-2-fill green-color"></i>`;
        batteryLiquid.style.height = '103%'; // Slight adjustment for visual
    } else if (level <= 20 && !isCharging) {
        batteryStatus.innerHTML = `Low battery <i class="ri-plug-line animated-red"></i>`;
    } else if (isCharging) {
        batteryStatus.innerHTML = `Charging... <i class="ri-flashlight-line animated-green"></i>`;
    } else {
        batteryStatus.innerHTML = '';
    }

    // Set gradient color based on battery level
    if (level <= 20) {
        batteryLiquid.className = 'battery__liquid gradient-color-red';
    } else if (level <= 40) {
        batteryLiquid.className = 'battery__liquid gradient-color-orange';
    } else if (level <= 80) {
        batteryLiquid.className = 'battery__liquid gradient-color-yellow';
    } else {
        batteryLiquid.className = 'battery__liquid gradient-color-green';
    }

    // Send battery data to Dash app
    fetch('/update_battery', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ level }),
    });
}
