class Vehical {
    constructor(wheels, passengers, gas) {
      this.wheels = wheels;
      this.passengers = passengers;
      this.gas = gas;

    }
    set_num_of_wheels(){
        return "Number of wheels: ",this.wheels
    }
    set_num_of_passengers(){
        return "Number of passengers: ",this.passengers
    }
    has_gas(){
        return "Number of gas: ",this.gas
    }
}


let car = new Vehical(10,50,true)
console.log("Car Wheels",car.set_num_of_wheels())
console.log("Car Passengers",car.set_num_of_passengers())
console.log("Car Gas",car.has_gas())

console.log("++++++++++++++++++++++++++++++");

let Plan = new Vehical(40,150,false)
console.log("Plan Wheels",Plan.set_num_of_wheels())
console.log("Plan Passengers",Plan.set_num_of_passengers())
console.log("Plan Gas",Plan.has_gas())