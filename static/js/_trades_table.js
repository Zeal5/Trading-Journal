
function toggle_comments(row) {
    const notSelected = row.querySelector("#comment");
    const selected = row.querySelector("#highlighted-comment");

    if (notSelected) {
        notSelected.id = "highlighted-comment"
    }
    else if (selected) {
        selected.id = "comment";
    }


}
document.getElementById("tradeForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission
    const tbody = document.querySelector(".entries-table-body")

    var entry = tbody.querySelector('input[name="entry_price"]').value;
    var exit = tbody.querySelector('input[name="exit_price"]').value;
    var ticker = tbody.querySelector('input[name="ticker"]').value;
    var side = tbody.querySelector('select').value;
    var stop_loss = tbody.querySelector('input[name="stop_loss"]').value;
    var take_profit = tbody.querySelector('input[name="take_profit"]').value;
    var pnl = tbody.querySelector('input[name="pnl"]').value;
    var rr = tbody.querySelector('input[name="rr"]').value;
    var tags = tbody.querySelector('input[name="tags"]').value;
    // var images = document.querySelector('input[name="images"]').value;
    var comment = tbody.querySelector('input[name="comment"]').value;

    // Check for errors
    some_data = {
        'entry': entry,
        'exit': exit,
        'ticker': ticker,
        'side': side,
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'pnl': pnl,
        'rr': rr,
        'tags': tags,
        'comment': comment
    }
    // error display
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    // console.log(`csrf = ${csrfToken}`)
    fetch("/upload/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(some_data)
    })
        .then(response => {
            if (response.ok) {
                console.log('woking')
                // adding new row
                const newRow = document.createElement('tr');
                newRow.className = 'table-rows';
                newRow.onclick = function () {
                    toggle_comments(this)
                }

                // Create table data cells and populate them with"data"
                const td1 = document.createElement('td');
                td1.textContent = "data";

                const td2 = document.createElement('td');
                td2.textContent = "data";

                const td3 = document.createElement('td');
                td3.textContent = "data";

                const td4 = document.createElement('td');
                td4.textContent = "data";

                const td5 = document.createElement('td');
                td5.textContent = "data";

                const td6 = document.createElement('td');
                td6.textContent = "data";

                const td7 = document.createElement('td');
                td7.textContent = "data";

                const td8 = document.createElement('td');
                td8.textContent = "data";

                const td9 = document.createElement('td');
                td9.textContent = "data";

                const td10 = document.createElement('td');
                const img = document.createElement('img');
                img.alt = 'None';
                // add link to image url here
                // img.src = "data";  
                td10.appendChild(img);

                const td11 = document.createElement('td');
                td11.id = 'comment';
                td11.textContent = "data dhjfosd jsjdf hjweio fewncindsjfn weonfjsda;f uewnfjds;fh wenfdjas;sd huwendfj wefnhsjfh uwenfju";

                // Append the table data cells to the new row
                newRow.appendChild(td1);
                newRow.appendChild(td2);
                newRow.appendChild(td3);
                newRow.appendChild(td4);
                newRow.appendChild(td5);
                newRow.appendChild(td6);
                newRow.appendChild(td7);
                newRow.appendChild(td8);
                newRow.appendChild(td9);
                newRow.appendChild(td10);
                newRow.appendChild(td11);

                const last_child = tbody.lastElementChild;
                tbody.insertBefore(newRow, last_child)

            }
            else {
                return response.text()
                    .then(errorMsg => {
                        throw errorMsg;
                    });
            }
        })
        .catch(error => {
            showError(error)
        })


    function showError(message) {
        let err = JSON.parse(message)
        let error_message = ""
        for (var key in err) {
            if (err.hasOwnProperty(key)) {
                var value = err[key];
                error_message += (key.toUpperCase() + " " + value + "<br>");
            }
        }




        const errorPopup = document.getElementById('error_popup');
        console.log(error_message)
        errorPopup.innerHTML = error_message;
        errorPopup.style.backgroundColor = "red";
        errorPopup.style.color = "white";
        errorPopup.style.display = 'flex';

        setTimeout(() => {
            errorPopup.style.display = 'none';
        }, 3000);
    }

});

