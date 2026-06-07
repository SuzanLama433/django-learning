let balance = 100000; // keep outside so it remembers value

function atm(event) {
    event.preventDefault();
    let mypin = 1234;

    let pin = Number(document.getElementById("pin").value);
    let amount = Number(document.getElementById("amount").value);
    let option = document.getElementById("transaction").value;

    let result = document.getElementById("result");

    if (pin == mypin) {

        if (option == "balance") {
            result.innerText = "Your total balance is Rs " + balance;
        }

        else if (option == "withdraw") {
            if (amount <= balance) {
                balance -= amount;
                result.innerText = "You withdrew Rs " + amount + 
                                   ". Remaining balance: Rs " + balance;
            } else {
                result.innerText = "Insufficient balance!";
            }
        }
        else if (option == "deposit") {
            balance += amount;
            result.innerText = "You deposited Rs " + amount + 
                               ". New balance: Rs " + balance;
        }
    } else {
        result.innerText = "Wrong PIN! Enter correct PIN.";
    }

}