class Animal {
    constructor(name) {
        this.name = name;
    }

    move() {
        console.log(`${this.name} is moving`);
    }

    makeSound() {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }

    move() {
        console.log(`${this.name} the ${this.breed} is running happily! 🐕`);
    }

    makeSound() {
        console.log(`${this.name} says: Woof! Woof! 🐶`);
    }
}

class Fish extends Animal {
    constructor(name, species) {
        super(name);
        this.species = species;
    }

    move() {
        console.log(`${this.name} the ${this.species} is swimming gracefully! 🐠`);
    }

    makeSound() {
        console.log(`${this.name} makes bubble sounds... 🫧`);
    }
}

class Bird extends Animal {
    constructor(name, type) {
        super(name);
        this.type = type;
    }

    move() {
        console.log(`${this.name} the ${this.type} is flying high! 🦅`);
    }

    makeSound() {
        console.log(`${this.name} chirps: Tweet! Tweet! 🐦`);
    }
}

const animals = [
    new Dog('Buddy', 'Golden Retriever'),
    new Fish('Nemo', 'Clownfish'),
    new Bird('Sky', 'Eagle')
];

animals.forEach(animal => {
    animal.move();
    animal.makeSound();
    console.log('---');
});
