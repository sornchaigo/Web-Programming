'use strict'

// let officialName = prompt("What's the “official” name of JavaScript?");
// if ( officialName == "ECMAScript" ) {
//     alert("Right!");
// } else {
//     alert("You don't know? “ECMAScript”!");
// }


// let age = prompt("What is your age?");
// if (age >= 14 && age <= 90) {
//     alert("Your age in range.");
// } else {
//     alert("Your age are not range.");
// }

// if (age >= 14 && age <= 90 && age) {
//     alert(age);
// }

// let userName = prompt("Who's there?");
// if (userName && userName == "Admin") {

//     let pass = prompt('Password?', '');
//     if (pass && pass == 'TheMaster') {
//         alert('Welcome!');
//     } else if (pass) {
//         alert('Wrong password')
//     } else {
//         alert('Canceled');
//     }

// } else if (userName) {
//     alert("I don't know you");
// } else {
//     alert('Canceled');
// }


// let arr = ["Apple", "Orange", "Pear"];
// // for (let i = 0; i < arr.length; i++) {
// //   console.log( arr[i] );
// // }

// // iterates over array elements
// for (let fruit of arr) {
//     console.log(fruit);
// }

// for (let key in arr) {
//     console.log(arr[key], key); // Apple, Orange, Pear
// }

// let arg = prompt("Enter a value?");
// cases = {
//     0: "One or zero",
//     1: "One or zero",
//     2: "Two",
//     3: "Never executes!",
// }

// let operations = {
//     '+': function (x, y) { return x + y },
//     '-': function (x, y) { return x - y },
// }

// let operations2 = {
//     '+': (x, y) => x + y,
//     '-': (x, y) => x - y,
//     '*': (x, y) => x * y,
//     '/': (x, y) => x / y,
// }


// function ask(question, yes, no) {
//     if (confirm(question)) yes();
//     else no();
// }

// ask(
//     "Do you agree?",
//     function () { alert("You agreed."); },
//     function () { alert("You canceled the execution."); }
// );

// let ask2 = (question, yes, no) => confirm(question) ? yes() : no();
// // {
// //     // if (confirm(question)) yes();
// //     // else no();
// //     confirm(question) ? yes() : no();
// // }


// ask(
//     "Do you agree?",
//     () => alert("You agreed."),
//     () => alert("You canceled the execution.")
// );

function checkAge(age) {
    if (age > 18) {
        return true;
    }

    return 'Did parents allow you?';
}

function checkAge2(age) {
    return (age > 18) ?
        true :
        'Did parents allow you?';
}

function checkAge3(age) {
    return (age > 18) || 'Did parents allow you?';
}

let checkAge4 = age => (age > 18) || 'Did parents allow you?';

function min(a, b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

function min2(a, b) {
    return a > b ? a : b;
}

let min3 = (a, b) => a > b ? a : b;

function pow(x, n) {
    let result = x;
    for (let i = 1; i < n; i++) {
        result *= x;
    }
    return x;
}

function pow2(x, n) {
    return x ** n;
}

let pow3 = (x, n) => x ** n;

// let response = checkAge(10);
// console.log(response);
// response = checkAge(20);
// console.log(response);

// กำหนด loop ต่อไปนี้ ค่าสุดท้ายของค่า i ควรเป็นเท่าไร
// let i = 3;
// while (i) {
//     // alert(i--);
//     console.log(i--);   // กอไผ่ 0 1 1 
// }

// กำหนด loop ต่อไปนี้ ควรจะแสดงข้อมูลอะไรบ้าง
// let i = 0;
// while (i++ < 5) console.log( i );

// สอง loop ต่อไปนี้ให้ผลลัพธ์แตกต่างกันหรือไม่ 3 ต่าง 4 ไม่ต่าง
// for (let i = 0; i < 5; i++) console.log( i );
// for (let i = 0; i < 5; ++i) console.log( i );

//Use the for loop to output even numbers from 2 to 10.
//ใช้ลูป for สร้างหาจำนวน เลขคู่ ใน 2-10 
// ให้เขียน code แล้วแปะลง chat นะครับ 
for (let i of [2, 4, 6, 8, 10]) {
    console.log(i);
}
for (let i = 2; i <= 10; i+=2) {
    console.log(i)
}