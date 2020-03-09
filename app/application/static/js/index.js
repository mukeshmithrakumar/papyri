// ----------------------- Store Paper Name -----------------------


// Watch for enter when trying to search for the paper
$(".searchInput").on('keypress', function(e) {
    if (e.which === 13) {
        storePaper();
    }
});


// Function that reads the input and stores it
function storePaper() {

    // Get the user input from the index.html
    var _name = $('.searchInput').val();
    sessionStorage.setItem('_search_text', _name);

    // Move to next page
    location.href = "./search.html";
}
