function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId());
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail());
    console.log('Token ID: ' + id_token);

    var requestAJAX = $.ajax('/login/?id_token=' + id_token);

    requestAJAX.done(function (data) {
        if (data['user_authenticated']) {
            $('#login_google').toggle(500);
            $('#signout').toggle(500);
            console.log('Logged in')

            $('.login_box').append("<li><img src=\"" + profile.getImageUrl() + "\"> " + profile.getName() + " </li>")
        } else {
            console.log('Not logged in')
        }
    });
}