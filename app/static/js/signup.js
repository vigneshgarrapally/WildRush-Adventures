function validatePassword() {
  const password = document.getElementById("password").value;
  const message = document.getElementById("message");
  const letter = document.getElementById("letter");
  const capital = document.getElementById("capital");
  const number = document.getElementById("number");
  const length = document.getElementById("length");
  message.style.display = "none";
  // Show the message div only if the password field is not empty
  if (password !== "") {
    message.style.display = "block";
  }
  // Reset the validity icons
  const icons = message.querySelectorAll(".icon");
  icons.forEach((icon) => (icon.innerHTML = "&#10005;"));

  const hasLowercase = /[a-z]/.test(password);
  const hasUppercase = /[A-Z]/.test(password);
  const hasNumber = /\d/.test(password);
  const hasSpecialChar = /\W/.test(password);
  const isAtLeast8Chars = password.length >= 8;
  // Validate lowercase letter
  if (hasLowercase) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
    letter.querySelector(".icon").innerHTML = "&#10003;";
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }

  // Validate uppercase letter
  if (hasUppercase) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
    capital.querySelector(".icon").innerHTML = "&#10003;";
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate number
  if (hasNumber) {
    number.classList.remove("invalid");
    number.classList.add("valid");
    number.querySelector(".icon").innerHTML = "&#10003;";
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  // Validate length
  if (isAtLeast8Chars) {
    length.classList.remove("invalid");
    length.classList.add("valid");
    length.querySelector(".icon").innerHTML = "&#10003;";
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }

  // Validate special characters
  if (hasSpecialChar) {
    special.classList.remove("invalid");
    special.classList.add("valid");
    special.querySelector(".icon").innerHTML = "&#10003;";
  } else {
    special.classList.remove("valid");
    special.classList.add("invalid");
  }

  // Validate password
  if (
    hasLowercase &&
    hasUppercase &&
    hasNumber &&
    hasSpecialChar &&
    isAtLeast8Chars
  ) {
    message.classList.remove("invalid");
    message.classList.add("valid");
    message.querySelector(".icon").innerHTML = "&#10003;";
  }
}

// function validateConfirmPassword() {
//   const password = document.getElementById("password").value;
//   const confirmPassword = document.getElementById("confirmPassword").value;
//   const confirmMessage = document.getElementById("confirmMessage");
//   confirmMessage.style.display = "none";

//   if (confirmPassword !== "") {
//     confirmMessage.style.display = "block";
//   }

//   if (password === confirmPassword) {
//     confirmMessage.classList.remove("invalid");
//     confirmMessage.classList.add("valid");
//     confirmMessage.querySelector(".icon").innerHTML = "&#10003;";
//   }

//   if (password !== confirmPassword) {
//     confirmMessage.classList.remove("valid");
//     confirmMessage.classList.add("invalid");
//   }

//   if (confirmPassword === "") {
//     confirmMessage.classList.remove("valid");
//     confirmMessage.classList.remove("invalid");
//   }

//   if (password === "") {
//     confirmMessage.style.display = "none";
//   }
// }
