const togglePassword1 = document.querySelector('#togglePassword1');

const togglePassword2 = document.querySelector('#togglePassword2');

const password1 = document.querySelector('#id_password1');

const password2 = document.querySelector('#id_password2');


togglePassword1.addEventListener('click', function (e) {

	// Toggle the type attribute
	const type = password1.getAttribute(
		'type') === 'password' ? 'text' : 'password';
	password1.setAttribute('type', type);
	

	// Toggle the eye slash icon
	if (togglePassword1.src.match(
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917145551/eye.png")) {
		togglePassword1.src =
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917150049/eyeslash.png";
	} else {
		togglePassword1.src =
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917145551/eye.png";
	}
});


togglePassword2.addEventListener('click', function (e) {

	// Toggle the type attribute
	const type = password2.getAttribute(
		'type') === 'password' ? 'text' : 'password';
	password2.setAttribute('type', type);
	

	// Toggle the eye slash icon
	if (togglePassword2.src.match(
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917145551/eye.png")) {
		togglePassword2.src =
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917150049/eyeslash.png";
	} else {
		togglePassword2.src =
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917145551/eye.png";
	}
});
