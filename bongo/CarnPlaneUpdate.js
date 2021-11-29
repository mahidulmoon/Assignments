class Vehical {
    constructor(wheels, passengers, gas) {
      this.wheels = wheels;
      this.passengers = passengers;
      this.gas = gas;

    }
    set_num_of_wheels(value){
        return "Number of wheels: ",value
    }
    set_num_of_passengers(value){
        return "Number of passengers: ",value
    }
    has_gas(value){
        return "Number of gas: ",value
    }
}


let car = new Vehical()
console.log("Car Wheels",car.set_num_of_wheels(35))
console.log("Car Passengers",car.set_num_of_passengers(100))
console.log("Car Gas",car.has_gas(true))

console.log("++++++++++++++++++++++++++++++");

let Plan = new Vehical()
console.log("Plan Wheels",Plan.set_num_of_wheels(50))
console.log("Plan Passengers",Plan.set_num_of_passengers(200))
console.log("Plan Gas",Plan.has_gas(false))