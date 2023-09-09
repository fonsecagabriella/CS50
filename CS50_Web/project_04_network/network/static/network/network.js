document.addEventListener('DOMContentLoaded', function() {
  // addEventListener like notes to all like buttons
  const like_buttons = document.querySelectorAll('#like-note');

  like_buttons.forEach(function(element) {
    element.addEventListener('click', like_note);
  }); // <- Add a closing parenthesis here


  const comment_buttons = document.querySelectorAll('#comment-note');

  comment_buttons.forEach(function(element) {
    element.addEventListener('click', comment);
  }); // <- Add a closing parenthesis here

  const edit_note_buttons = document.querySelectorAll('#edit-note');

  edit_note_buttons.forEach(function(element) {
    element.addEventListener('click', text_edit_note);
  }); // <- Add a closing parenthesis here

  if (document.querySelector("#follow-button")){
    document.querySelector("#follow-button").addEventListener('click', follow);
  }

  document.querySelector("#save_edited_note").addEventListener('click', edit_note);



});

function like_note(){
  let id_note = this.value;
  //console.log("" + id_note);

  // Send a GET request to the URL
  //fetch(`/like_note/${id_note}`)

  // Send a PUT request to the URL
  fetch(`/like_note/${id_note}`, {
    method: 'PUT'
  })

  // Put response into json form
  .then(response => response.json())
  .then(data => {
        // Log data to the console
        //console.log(data);

        // Update the text of the button
            this.innerHTML = ` ❤️  ${data.likers}  `;
    });

}

function follow(){
  let profile_to_follow = this.value;

  // Send a PUT request to the URL
    fetch(`/follow/${profile_to_follow}`, {
      method: 'PUT'
    })

    // Put response into json form
    .then(response => response.json())
    .then(data => {
          // Log data to the console
          //console.log(data);

          // Update the text of the button
          if (this.innerHTML == `UNFOLLOW`) {
            this.innerHTML = `FOLLOW`; }
          else {
            this.innerHTML = `UNFOLLOW`; }
          // Update the followers / followeing count
          document.querySelector("#connections").innerHTML = `FOLLOWERS: ${ data.followers } | FOLLOWING: ${ data.following } `;
      });

}

function comment(){
  let id_note = this.value;

  //console.log("" + id_note);

  const hidden_note_value = document.createElement('input');
  hidden_note_value.setAttribute('type', 'hidden');
  hidden_note_value.setAttribute('name', 'note_id');
  hidden_note_value.setAttribute('value', id_note);

  document.querySelector("#comment-form").append(hidden_note_value);

}

function text_edit_note(){
  let id_note = this.value;
  console.log("" + id_note);

    // Send a GET request to the URL
    fetch(`/edit_note/${id_note}`, {
      method: 'GET'
    })

    // Put response into json form
    .then(response => response.json())
    .then(data => {

          // Update the content of current note
          document.querySelector("#note_edit_id").value = id_note;
          document.querySelector("#edited-note-text").value = data.note_content;

      });

}

function edit_note(){


  // Store form values in local variables
  let edited_note_text = document.querySelector("#edited-note-text").value;
  let note_id = document.querySelector("#note_edit_id").value;

  console.log(`Edited text: ${edited_note_text}`);


  // Try to send edited note using our own API
  fetch(`/save_edit_note`, { //Open de emails route, set in URL
    method: 'PUT',
    body: JSON.stringify({
        edited_note_text: edited_note_text,
        note_id: note_id
    })
  })

  // Put response into json form
  .then(response => response.json())
  .then(data => {
        // Log data to the console
        console.log(data);

        // Update the text of the note
        document.querySelector(`${data.name_id}`).innerHTML = data.note_content;
    });

  document.querySelector("#edited-note-text").value = "";

  // Close the modal after saving.
  const editModal = document.getElementById('editModal'); // Replace 'myModal' with your modal's ID or selector.
  $(editModal).modal('hide'); // Use jQuery's modal method or adapt this code to your JavaScript framework if needed.

}