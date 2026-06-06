function add(){
    let a = Number(document.getElementById('num1').value)
    let b = Number(document.getElementById('num2').value)
    let op = document.getElementById('operator').value

    let result;

    if (op=="add"){
        result = a+b
    }
    else if (op=="sub"){
        result =a-b
    }
    else if (op=="mul"){
        result = a*b
    }
    else if (op=="div"){
        if (b!=0){
            result = a/b
        }
        else {
            result = "cannot divided by zero"
        }
    }
    document.getElementById('result1').innerText="Result :"+result
}