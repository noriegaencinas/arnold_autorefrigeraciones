var table = document.getElementById("tabla_empleados");

// Add an event listener to listen for clicks on table cells
table.addEventListener("click", function(event) {
  // Check if the clicked element is a table cell
  if (event.target.tagName === 'TD') {
    // Set the background color of the card to red
    var card = document.getElementById("details_card");
    card.style.backgroundColor = "red";
  }
});

