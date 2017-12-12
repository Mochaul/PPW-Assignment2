// Setup an event listener to make an API call once auth is complete
function onLinkedInLoad() {
    IN.Event.on(IN, "auth", getProfileData);
}

// Use the API call wrapper to request the member's profile data
function getProfileData() {
    IN.API.Profile("me").fields("id", "first-name", "last-name", "headline", "location", "picture-url", "public-profile-url", "email-address").result(displayProfileData).error(onError);
}

function displayProfileData(data){
    var user = data.values[0];
    var id = user.id;
    console.log(id);
    IN.API.Raw("/companies?format=json&is-company-admin=true")
    .method("GET")
    .result(function(response){
      console.log(response.values[0].id)
      getCompanyData(response.values[0].id)
      $.ajax({
        method : "POST",
        url : '/sabibatbet_login/add-session/',
        data : {
          name: user.firstName+" "+user.lastName,
          id:id,
          companyID: response.values[0].id,
          csrfmiddlewaretoken : '{{ csrf_token }}'
        },
        success : function (){},
        error : function (error){
        }
      });
    });
    // $("#gambar").append('<img src="'+user.pictureUrl+'"class="img-circle">');
    $("#tempat").append('<button class="btn btn-primary">Company Profile </button>'+'<br>');
    $("#logout").append("<button class='btn btn-danger' onClick='logout()'>Logout</button>");
    console.log(data);
    console.log();  
    // $("#name").append(
    //   '<p>'+'Logged in as '+user.firstName+' '+user.lastName+'</p>'+
    //   '<button class="btn btn-primary delete">Company Profile</button>');
    // document.getElementById('profileData').style.display = 'block';
}

// Use the API call wrapper to request the company's profile data
function getCompanyData(id) {
	// Masukin ID company lau
    var cpnyID = id;
    localStorage.setItem('companyId', cpnyID);
    console.log(localStorage.getItem('companyId'));
    IN.API.Raw("/companies/" + cpnyID + ":(id,name,ticker,description)?format=json")
      .method("GET")
      .result(displayCompanyData)
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
  window.location.assign("/sabibatbet_login/");
  $.ajax({
      method: "GET",
      url: '/sabibatbet_login/remove-session',
});
}
