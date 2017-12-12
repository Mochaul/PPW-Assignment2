function checkLoggedIn() {
  if (IN.User.isAuthorized() === true) {
      IN.User.authorize(onLinkedInLoadCompany);
  } else {
      window.location = "/";
  }
}

// Use the API call wrapper to request the company's profile data
function getCompanyData() {
    var cpnyID = localStorage.getItem('companyId');
    console.log(cpnyID);
    IN.API.Raw("/companies/" + cpnyID + ":(id,name,ticker,description,company-type,website-url,specialties)?format=json")
      .method("GET")
      .result(displayCompanyData)
      .error(onError);
}

function onLinkedInLoadCompany() {
    IN.Event.on(IN, "auth", getCompanyData);
}

function displayCompanyData(data){
    console.log(data);
    console.log(data.companyType.name);
    $('html').css("display", "inline")
    $('#companyName').append(data.name + '"');
    $('#about').append(data.description);
    $('#companyType').append(data.companyType.name);
    $('#companyWeb').append("<a href='" + data.websiteUrl + "'>" + data.websiteUrl + "</a>");
    $('#companySpecialty').append(data.specialties.values);
    $("#space-logout").append('<li class="nav-item"><a class="btn btn-danger" onclick="logout()">Logout</a></li>');
}

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
