'use strick'

// let week = [
//     ["Mon", "", "", "", ""],
//     ["Tue", "Database I", "Database I", "", ""],
//     ["Wed", "", "", "Application Development for Mobile Devices", "Application Development for Mobile Devices"],
//     ["Thu", "Unix Tools and System Administration", "Unix Tools and System Administration", "Human and Computer Interaction", "Human and Computer Interaction"],
//     ["Fri", "", "", "", ""],
// ];
let week = {
    'Mon': [{ text: "" }, { text: "" }, { text: "" }, { text: "" }],
    'Tue': [{ text: "Database I", attribute: "colspan='2'" }, { text: "" }, { text: "" }],
    'Wed': [{ text: "" }, { text: "" }, { text: "Application Development for Mobile Devices", attribute: "colspan='2'" }],
    'Thu': [{ text: "Unix Tools and System Administration", attribute: "colspan='2'" }, { text: "Human and Computer Interaction", attribute: "colspan='2'" }],
    'Fri': [{ text: "" }, { text: "" }, { text: "" }, { text: "" }],
}

let tbody = document.querySelector('#table > tbody');
for (let day in week) {
    let tr = document.createElement('tr');
    tr.innerHTML += `<th>${day}</th>`;
    for (let td of week[day])
        tr.innerHTML += `<td ${td.attribute}>${td.text}</td>`;

    tbody.append(tr);
}
let tr = document.querySelector('#table > tbody > tr');
let nth = document.querySelector('#table > tbody > tr :nth-child(4)');
let td = document.createElement("td");
td.rowSpan = 6;
td.className = "lunch";
td.textContent = "Lunch";
td.innerHTML = `<div>Lunch</div>`;
tr.insertBefore(td, nth);

