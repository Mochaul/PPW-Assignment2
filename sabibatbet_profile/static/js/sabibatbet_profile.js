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
    console.log(data);
    var user = data.values[0];
    $("#baton").append('<a class="btn btn-primary btn-lg" href="/profile/" role="button">Company Dashboard &raquo;</a>')
    $("#name").append('Logged in as '+user.firstName+' '+user.lastName);
    $("#space-logout").append('<li class="nav-item"><a class="btn btn-danger" onclick="logout()">Logout</a></li>');
    document.getElementById('profileData').style.display = 'block';
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
    window.location = "/";
}
