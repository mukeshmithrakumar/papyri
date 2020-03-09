// ----------------------- Advanced Filter Box -----------------------

let showFilters = false;
if (showFilters) {
    document.getElementById("FiltersBox").style.display = "grid";
} else {
    document.getElementById("FiltersBox").style.display = "none";
}

function toggleFilters() {
    showFilters = !showFilters;

    if (showFilters) {
        document.getElementById("FiltersBox").style.display = "grid";
    } else {
        document.getElementById("FiltersBox").style.display = "none";
    }
}


// ----------------------- Research Paper Basic Search Results -----------------------

// Get Paper Name from storage and remove it
var _paper_name = sessionStorage.getItem('_search_text');
console.log(_paper_name);

sessionStorage.removeItem('_search_text');

// Call Basic Search
if (_paper_name !== null) {
    basicSearch(_paper_name);
}

function basicSearch(query) {
    // Sluggify User query
    var clean_query = sluggify(query);

    // Call ajax to retrieve advanced search results
    getResults(clean_query);
}

// Function to remove special characters from name
function sluggify(raw_name) {
    var clean_name = raw_name.match(/\w+/g).join('+');
    return clean_name;
}


// ----------------------- Research Paper Advanced Search Results -----------------------

// Function for the advanced search.
function advancedSearch() {
    // Clear Screen if they start advanced search
    $('.post').hide();

    // Get User Input
    var query = $('.advancedInput').val();
    var start = 0;
    var sortBy = $("#sortBy :selected").text();
    var sortOrder = $("#sortOrder :selected").text();
    var max_results = $("#maxResults").val();

    // Sluggify User query
    var clean_query = sluggify(query);

    // Call ajax to retrieve advanced search results
    getResults(clean_query, start, max_results, sortBy, sortOrder);

}


// ----------------------- Get Search Results -----------------------

// Function to get search results
function getResults(query, start=0, max_results=1, sortBy="relevance", sortOrder="descending") {

    // Add parameters for advanced search
    var fullUrl = getUrl(query, start, max_results, sortBy, sortOrder);

    // Ajax call
    $.ajax({
        url: fullUrl,
        type: "GET",
        dataType: "xml",
        success: function (xml) {
            loadResults(xml, max_results);
        },
        error: function (status) {
            console.log("Request error " + status + "for url: " + fullUrl);
        }
    });
}

// TODO: Need to write so you can use the date to search
function getUrl(query, start, max_results, sortBy, sortOrder) {
    var baseUrl = "http://export.arxiv.org/api/query?search_query=all:";

    // Add advanced parameters to base url
    if (query) {
        baseUrl += query;
    }

    if (start) {
        baseUrl += "&" + "start=" + start;
    }

    if (max_results) {
        baseUrl += "&" + "max_results=" + max_results;
    }

    if (sortBy) {
        baseUrl += "&" + "sortBy=" + sortBy;
    }

    if (sortOrder) {
        baseUrl += "&" + "sortOrder=" + sortOrder;
    }
    return baseUrl;
}

// Function to load results and call the create post function
// TODO: See if you can write code to make the load async
function loadResults(xml) {

    $(xml).find('entry').each(function() {
        var $paper = $(this);
        var title = $paper.find('title').text();

        var authors = [];
        $paper.find('author').each(function() {
            authors.push($(this).find('name').text().trimEnd());
        });

        var date = $paper.find('published').text().split("T")[0];
        var summary = $paper.find('summary').text();
        var url = $paper.find('link').text();

        createPost(title, authors, date, summary, url);
    });
}

// Function to create post
function createPost(title, authors, date, summary, url) {
    var str_url = "'" + url + "'";

    const post = document.createElement('div');
    post.classList.add('post');
    post.innerHTML = `
    <div class="try-it">
        <img src="../static/images/logo_red.svg" style="width:50px;height:50px;">
        <button class="btn summarize-button" onclick="summaryUrl(${str_url})">Summarize</button>
    </div>
    <div class="post-info">
        <h2 class="post-title">${title}</h2>
        <p class="post-author">by ${authors}</p>
        <small class="post-date">${date}</small>
        <p class="post-abstract">${summary}</p>
    </div>
    `;

    container.appendChild(post);
}

// Function to store URL to be summarized which can be later extracted by Flask
function summaryUrl(raw_url) {
    // Store URL
    sessionStorage.setItem('_summary_url', raw_url);

    // Change Page to summary
    location.href = "./summary.html";
}
