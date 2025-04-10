class Smartphone {
    constructor(brand, model, os, storageGB) {
        this.brand = brand;
        this.model = model;
        this.operatingSystem = os;
        this.storage = storageGB;
        this.isOn = false;
        this.installedApps = [];
    }

    togglePower() {
        this.isOn = !this.isOn;
        console.log(`${this.brand} ${this.model} is now ${this.isOn ? 'on' : 'off'}`);
    }

    installApp(appName) {
        if (this.isOn) {
            this.installedApps.push(appName);
            console.log(`Installed ${appName} on ${this.brand}`);
        } else {
            console.log('Cannot install app - phone is off');
        }
    }

    displaySpecs() {
        console.log(`
        ${this.brand} ${this.model}
        OS: ${this.operatingSystem}
        Storage: ${this.storage}GB
        Apps: ${this.installedApps.length} installed
        `);
    }
}

class GamingPhone extends Smartphone {
    constructor(brand, model, os, storageGB, gpuModel) {
        super(brand, model, os, storageGB);
        this.gpu = gpuModel;
        this.gamingMode = false;
    }

    toggleGamingMode() {
        this.gamingMode = !this.gamingMode;
        console.log(`Gaming mode ${this.gamingMode ? 'activated' : 'deactivated'}`);
    }

    displaySpecs() {
        super.displaySpecs();
        console.log(`GPU: ${this.gpu}`);
    }
}

const myPhone = new Smartphone('Apple', 'iPhone 15', 'iOS', 128);
myPhone.togglePower();
myPhone.installApp('Twitter');
myPhone.displaySpecs();

const gamingPhone = new GamingPhone('ASUS', 'ROG Phone 6', 'Android', 256, 'Adreno 660');
gamingPhone.togglePower();
gamingPhone.toggleGamingMode();
gamingPhone.displaySpecs();
