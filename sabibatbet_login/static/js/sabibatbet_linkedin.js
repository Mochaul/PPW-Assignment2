// Setup an event listener to make an API call once auth is complete
function onLinkedInLoad() {
    IN.Event.on(IN, "auth", getProfileData);
}

// Use the API call wrapper to request the member's profile data
function getProfileData() {
    IN.API.Profile("me").fields("id", "first-name", "last-name", "headline", "location", "picture-url", "public-profile-url", "email-address").result(displayProfileData).error(onError);
}

// Handle the successful return from the API call
function displayProfileData(data){
    var user = data.values[0];
    $("#name").append(
      '<p>'+'Logged in as '+user.firstName+' '+user.lastName+'</p>'+
      '<button class="btn btn-primary delete">Company Profile</button>');
    document.getElementById('profileData').style.display = 'block'; 
}

// Use the API call wrapper to request the company's profile data
function getCompanyData() {     
	// Masukin ID company lau
    var cpnyID = 13600614;

    IN.API.Raw("/companies/" + cpnyID + ":(id,name,ticker,description)?format=json")
      .method("GET")
      .result(dipslayCompanyData)
      .error(onError);
}

function displayCompanyData(data){
    // To do
}

// Handle an error response from the API call
function onError(error) {
    console.log(error);
}

// Destroy the session of linkedin
function logout(){
    IN.User.logout(removeProfileData);
}

// Remove profile data from page
function removeProfileData(){
    document.getElementById('profileData').remove();
}