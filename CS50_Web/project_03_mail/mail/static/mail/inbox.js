document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Button to send email
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function view_email(email_id){
  // loads the email based on the id
  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
    // Hide other divs
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';

    // Make div email  visible
    document.querySelector("#email-singular").style.display="block";
    document.querySelector("#email-singular").className = "card rounded-3xl px-4 py-8 p-lg-10 mb-6 p-3";

    // Add the content of the email
    document.querySelector('#email-singular').innerHTML = `
    <div class="container ">
        <h3 class="text-center">Subject: ${email.subject}</h3>
        <table class="p-2 w-full">
          <tbody>
            <tr>
              <td class="text-left"><b>From</b></td>
              <td class="text-right">${email.sender}</td>
            </tr>
            <tr>
              <td class="text-left"><b>To</b></td>
              <td class="text-right">${email.recipients}</td>
            </tr>
            <tr>
              <td class="text-left"><b>Sent on</b></td>
              <td class="text-left">${email.timestamp}</td>
            </tr>
          </tbody>
        </table>
        <hr>
        <p class="text-left"> ${email.body}</p>
    </div>
    `

    // ----- Archive button
    //Create the button
    const archived_button = document.createElement('button');
    archived_button.className = "btn btn-secondary"
    if(!email.archived){
      archived_button.innerHTML = 'Archive';}
    else{
      archived_button.innerHTML = "Unarchive";
    }
    // Logic to update value of email archived
    archived_button.addEventListener('click', function() {
      if(!email.archived){

        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: true
          })
        })

        .then(() => {load_mailbox("inbox")
      })

      }
      else{

        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: false
          })

        })
        .then(() => {load_mailbox("inbox")
      })

      }});
    // Appends button to div
    document.querySelector('#email-singular').append(archived_button);

    // ----- Reply button
    // Create the button, change text and add class
    const reply_button = document.createElement('button');
    reply_button.innerHTML = "Reply";
    reply_button.className = "btn btn-primary";

    reply_button.addEventListener('click', function(){
      compose_email();

      document.querySelector('#compose-recipients').value = email.sender;

      document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} sent: ${email.body}`;

      //Check if Subject contain Re: for Reply
      let subject = email.subject;
      if(subject.split(" ",1)[0] != "Re:"){
        subject = "Re: " + email.subject;
      }
      document.querySelector('#compose-subject').value = subject;
    });

     // Appends button to div
     document.querySelector('#email-singular').append(reply_button);



    // Mark the email as read
    if (!email.read){
      fetch(`/emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
    }


  });
}

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector("#email-singular").style.display="none";

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

}

function send_email(event){

  // Prevent the default form submission
  event.preventDefault();

  // Store form values in local variables
  let form = document.querySelector("#compose-form");
  let recipients = form.querySelector("#compose-recipients").value;
  let subject = form.querySelector("#compose-subject").value;
  let body = form.querySelector("#compose-body").value;

  // Try to send email using our own API
  fetch(`/emails`, { //Open de emails route, set in URL
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      //console.log(result);

      // If result does not return an error
      if (!result.error){
        document.querySelector('#invalid_recipient').style.display = 'none';
        // Alert successful message
        alert(result.message);
        // Load the Sent Mailbox
        load_mailbox('inbox');
      }
      else{
        // Alert with error
        alert(result.error);
        // Load error message
        document.querySelector('#invalid_recipient').innerHTML = result.error;
        document.querySelector('#invalid_recipient').style.display = 'block';
      }
    }

  );



}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector("#email-singular").style.display="none";

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`) // Don't forget to use backticks otherwise it wont work
  .then(response => response.json())
  .then(emails => {
      // Print emails
      //console.log(emails);

      // ... do something else with emails ...
      emails.forEach(email_object => {
        // Create a new div for the email
        const email_div = document.createElement('div');
        // Add a class to the div you created
        email_div.className = "list-group-item";

        email_div.innerHTML = `<h6 class="email_sender"> From: ${email_object.sender} </h6>
                              <span class="email_subject"> Subject: ${email_object.subject} </span>
                              <span class="email_timestamp text-muted"> ${email_object.timestamp} </span>`;


        // Check if email was read or not to add appropriate class
        if (email_object.read) {email_div.className = "email_read_true";}
        else {email_div.className = "email_read_false";}

        // Add event listener to email
        email_div.addEventListener('click', function() {
            //console.log('This element has been clicked!')
            view_email(email_object.id) // Remember the view_email function needs to be declared before this current function
        });

        // Add the email_div to the emails_view
        document.querySelector('#emails-view').append(email_div);
              })
  });

}

