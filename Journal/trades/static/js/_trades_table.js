
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
// document.getElementById("tradeForm").addEventListener("submit", function(event) {
//   event.preventDefault(); // Prevent default form submission

//   // Get trade data from input fields
//   var entry = document.querySelector('input[name="entry"]').value;
//   var exit = document.querySelector('input[name="exit"]').value;
//   var dateTime = document.querySelector('input[name="date_time"]').value;

//   // Create trade object
//   var trade = {
//     entry: entry,
//     exit: exit,
//     date_time: dateTime
//   };

//   // Send trade data via AJAX
//   axios.post("/home_page/", trade)
//     .then(function(response) {
//       // Handle success response
//       console.log("Trade uploaded successfully");
//     })
//     .catch(function(error) {
//       // Handle error response
//       console.error("Error uploading trade:", error);
//     });
// });
